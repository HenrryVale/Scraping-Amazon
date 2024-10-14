from tabulate import tabulate
from sqlalchemy import create_engine, text


class ProductosHandler:
    def __init__(self, engine):
        self.engine = engine

 #Crear tabla
    def create_product_tbl(self):
        try:
            with self.engine.connect() as cursor:
                cursor.execute(text("""
                        DROP TABLE productos;
                        CREATE TABLE productos (
                            id SERIAL PRIMARY KEY,
                            img_url VARCHAR(1000) NOT NULL,
                            description VARCHAR(1000) NOT NULL,
                            price_symbol VARCHAR(1000) NOT NULL,
                            price VARCHAR(1000) NOT NULL,
                            price_fraction VARCHAR(1000) NOT NULL,
                            full_price VARCHAR NOT NULL,
                            starts VARCHAR(1000) NOT NULL,
                            valoration VARCHAR(1000) NOT NULL,
                            product_ok VARCHAR(1000) NOT NULL,
                            page_producto VARCHAR(1000) NOT NULL
                                    )
                            """))
                cursor.commit()
                print("Tabla creada productos")
        except Exception as error:
            print(error)

    # Insertar
    def insertar_productos(self, img_url, description, price_symbol, price, price_fraction, full_price, starts, valoration, product_ok):
        try:
            with self.engine.connect() as cursor:
                query = text("""
                    INSERT INTO productos (img_url, description, price_symbol, price, price_fraction, full_price, starts, valoration, product_ok, page_producto)
                    VALUES (:img_url, :description, :price_symbol, :price, :price_fraction, :full_price, :starts, :valoration, :product_ok, 'AMAZON')
                """)
                cursor.execute(query, {
                    'img_url': img_url,
                    'description': description,
                    'price_symbol': price_symbol,
                    'price': price,
                    'price_fraction': price_fraction,
                    'full_price': full_price,
                    'starts': starts,
                    'valoration': valoration,
                    'product_ok': product_ok
                })
                cursor.commit()
                print("[INFO] Producto creado")
        except Exception as error:
            print("Error: ", error)

    # Mostrar
    def mostrar_productos(self):
        try:
            with self.engine.connect() as cursor:
                query = "select * from productos"
                result = cursor.execute(text(query))

                data = result.fetchall()
                column_names = result.keys()

                print(tabulate(data, headers=column_names, tablefmt="github"))
        except Exception as error:
            print("Error: ", error)

