import os
from dotenv import load_dotenv
import tabulate
from PostgresSQL import *
from ProductosHandler import *
from  Extractproducts import *
from prefect import task, flow

# Cargar variables de entorno desde .env
load_dotenv()

USERNAME = os.getenv("USERNAME_BD")
PASSWORD = os.getenv("PASSWORD_BD")
HOST = os.getenv("HOST_BD")
BD = os.getenv("BD")

config = {
    "USERNAME": USERNAME,
    "PASSWORD": PASSWORD,
    "HOST": HOST,
    "BD": BD
}
db = PostgresSQLDatabase(HOST,USERNAME,PASSWORD,BD)
productosHandler = ProductosHandler(db.engine)

@task(name="Crear tablas productos para Amazon")
def task_crear_tabla():
  productosHandler.create_product_tbl()

@task(name="Obtener productos de Amazon")
def task_obtener_productos(URL):
  products = main(URL)

  if len(products) == 0:
     products = mainV2(URL)

  return  products

@task(name="Fuardar productos de Amazon")
def task_guardar_productos(products):
  for product in products:
      productosHandler.insertar_productos(**product)


@task(name="Mostrar productos de Amazon")
def task_mostrar_productos():
  productosHandler.mostrar_productos()


@flow(name="ETL Productos")
def main_flow(search_value):
    URL =f"https://www.amazon.com/s?k={search_value}"
    print(f"[URL] {URL}")
    task_crear_tabla()
    products = task_obtener_productos(URL)
    task_guardar_productos(products)
    task_mostrar_productos()
    db.close_conn()


if __name__ == '__main__':
    search_value = input("Ingrese un valor a buscar: ")
    main_flow(search_value.replace(" ", "+"))
