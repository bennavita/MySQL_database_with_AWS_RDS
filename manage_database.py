import pymysql
from sqlalchemy import create_engine
from credentials import user, password, host, port, database, input_dict


class ManageDataBase(object):
    def __init__(self, database_name):
        try:
            # Attempt to establish a connexion with AWS
            self.engine = self.database_engine()
            self.db = self.connect_database()
            print(f"Connexion to {host} as {user} has been successful.")
        except Exception as e:
            print(
                f"Connexion was unsuccessful due to the following error: {e}")

        finally:
            self.columns = [key for key in input_dict.keys()][1:-1]
            self.cursor = self.db.cursor()
            self.database_name = database_name
            self.create_database()
            self.select_database()

    def connect_database(self):
        return pymysql.connect(host=host, user=user, password=password)

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
        return create_engine(
            url="mysql+pymysql://{0}:{1}@{2}:{3}/{4}".format(
                user, password, host, port, database
            )
        )

    def close_chanel(self):
        try:
            self.db.close()
            self.engine.dispose()
            print("Connection with the database has been successfully closed")
        except Exception as e:
            print(
                f"An error occured while closing the connection with the database: {e}"
            )

class ManageTable(ManageDataBase):
    def __init__(self, database_name, table):
        super().__init__(database_name)
        self.table_name = table
        self.columns = [key for key in input_dict.keys()][1:-1]
        self.create_table()

    def create_table(self):
        """
        Create a table in the database if it does not already exists.
        Columns names are created dynamically from the /credentials
        Be aware that any change will create a new table in the database

        """
        parameters = str([f'{key} {value}' for key, value in input_dict.items()])[1:-1]
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
