import psycopg2

class Database:

    def get_connection(self):
        return psycopg2.connect(
                dbname="todo-list",
                user="postgres",
                password="571632gemi",
                host="127.0.0.1",
                port=5432)

    def init_db(self):
        conn = self.get_connection()

        with conn.cursor() as cur:
            cur.execute("""CREATE TABLE IF NOT EXISTS todo(
                    id SERIAL PRIMARY KEY,
                    title VARCHAR (50) NOT NULL,
                    description VARCHAR (100) NOT NULL);""")

        conn.commit()
        conn.close()        
        
