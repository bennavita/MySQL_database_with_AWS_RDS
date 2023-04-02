import pymysql
import mariadb as maria
from sqlalchemy import create_engine


class ManageDataBase(object):
    def __init__(self, user:str, password:str, host:str, port:str, input_dict:dict[str, str], database_name:str, db_type:str):

        #First and last key are not columns name (ID and Key of Table)
        self.columns = [key for key in input_dict.keys()][1:-1]
        self.db_type = db_type
        self.user = user
        self.password = password
        self.host = host
        self.dict = input_dict
        self.port = port
        self.database_name = database_name

        try:
            # Attempt to establish a connexion with AWS
            self.engine = self.database_engine()
            self.session = self.connect_database()
            self.cursor = self.session.cursor()
            self.create_database()
            self.select_database()
            print(f"Connexion to {host} as {user} has been successful.")
        except Exception as e:
            print(
                f"Connexion was unsuccessful due to the following error: {e}")

    def connect_database(self):
        if self.db_type == 'mariadb':
            return maria.connect(host=self.host, user=self.user, password=self.password, port=self.port, database=self.database_name)
        else:
            return pymysql.connect(host=self.host, user=self.user, password=self.password)

    def create_database(self):
        sql = f"""CREATE DATABASE IF NOT EXISTS {self.database_name}"""
        self.cursor.execute(sql)

    def select_database(self):
        sql = f"""USE {self.database_name}"""
        self.cursor.execute(sql)

    def show_tables(self):
        sql = """SHOW TABLES"""
        self.cursor.execute(sql)
        print(self.cursor.fetchall())

    def database_engine(self):
        return create_engine(f"mysql+pymysql://{self.user}:{self.password}@{self.host}:{self.port}/{self.database_name}")

    def close_chanel(self):
        try:
            self.session.close()
            self.engine.dispose()
            print("Connection with the database has been successfully closed")
        except Exception as e:
            print(
                f"An error occured while closing the connection with the database: {e}"
            )

class ManageTable(ManageDataBase):
    def __init__(self, user:str, password:str, host:str, port:int, input_dict:dict[str, str], database_name: str, table:str, db_type:str):
        super().__init__(user=user, password=password, host=host, port=port, input_dict=input_dict, database_name=database_name, db_type=db_type)
        self.table_name = table
        self.create_table()

    def create_table(self):
        """
        Create a table in the database if it does not already exists.
        Columns names are created dynamically from the /credentials
        Be aware that any change will create a new table in the database

        """

        parameters = str([f'{key} {value}' for key, value in self.dict.items()])[1:-1]
        sql = f"""CREATE TABLE if not exists {self.table_name} ({parameters})
            """.replace("'", "")
        self.cursor.execute(sql)

    def insert_dataframe(self, df):
        df.to_sql(self.table_name, con=self.engine,
                  if_exists="append", index=False)

    def table_content(self):
        print(self.engine.execute(
            f"SELECT * FROM {self.table_name}").fetchall())

    def drop_table(self, table):
        sql = f"""DROP TABLE {table}"""
        self.cursor.execute(sql)

    def describe_table(self):
        sql = f"""DESCRIBE {self.table_name}"""
        self.cursor.execute(sql)
        print(self.cursor.fetchall())
