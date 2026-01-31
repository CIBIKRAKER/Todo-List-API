from sqlalchemy import create_engine


class DatabaseURL:

    DATABASE_URL = "sqlite:///./todos.db"

    def get_connection(self):
        engine = create_engine(self.DATABASE_URL, connect_args={"check_same_thread": False})
        return engine