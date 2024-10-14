from sqlalchemy import create_engine, text


class PostgresSQLDatabase:
  def __init__(self, host, user, password, database):
    self.engine  = self.connect_to_db(host, user, password, database)


  def connect_to_db(self, host, user, password, database):

    try:
      engine = create_engine(f"postgresql+psycopg2://{user}:{password}@{host}:5432/{database}")

      engine.connect()
      print("Conexion exitosa")
      return engine
    except Exception as error:
      print("Error: ", error)

  def close_conn(self):
      if self.engine:
          self.engine.dispose()