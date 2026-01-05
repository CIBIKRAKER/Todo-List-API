import psycopg2

class Database:

    def get_connection(self):
        try:
            return psycopg2.connect(
                    dbname="Todo-App",
                    user="postgres",
                    password="571632gemi",
                    host="127.0.0.1",
                    port=5432)
        except Exception as e:
            print("An error occurred while connecting to the database:", e)
            raise

    def createTasksDb(self):
        try:
            with self.get_connection() as conn:
                with conn.cursor() as cur:
                    cur.execute("""CREATE TABLE IF NOT EXISTS Tasks(
                            id SERIAL PRIMARY KEY,
                            title VARCHAR (50) NOT NULL,
                            description VARCHAR (100) NOT NULL);""")
        except Exception as e:
            print("An error occurred during Tasks table creation:", e)
            raise
        
    def createUsersDb(self):
        try:
            with self.get_connection() as conn:
                with conn.cursor() as cur:
                    cur.execute("""CREATE TABLE IF NOT EXISTS Users (
                                    id SERIAL PRIMARY KEY,
                                    name VARCHAR(100) NOT NULL,
                                    email VARCHAR(255) NOT NULL UNIQUE,
                                    password_hash BYTEA NOT NULL,
                                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP);""")
        except Exception as e:
            print("An error occurred during Users table creation:", e)
            raise