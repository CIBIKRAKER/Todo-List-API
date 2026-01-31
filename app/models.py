import database
from sqlalchemy import Column, MetaData, Table, Column, Integer, String, Boolean

metadata = MetaData()

users = Table(
            'users', metadata,
            Column('id', Integer, primary_key=True),
            Column('name', String),
            Column('email', String, unique=True),
            Column('password', String)
        )

todos = Table(
            'todos', metadata,
            Column('id', Integer, primary_key=True),
            Column('title', String),
            Column('description', String),
            Column('completed', Boolean, default=False),
            Column('user_id', Integer)
        )

class ModelActions:

    def __init__(self, engine):
        self.engine = engine
        
    def insert_user(self, name, email, password):
        with self.engine.connect() as conn:
            conn.execute(users.insert().values(name=name, email=email, password=password))
            conn.commit()

    def insert_todo(self, title, description, user_id):
        with self.engine.connect() as conn:
            conn.execute(todos.insert().values(title=title, description=description, user_id=user_id))
            conn.commit()
    
        
