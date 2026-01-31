from models import users, todos


class UserCRUD:

    def __init__(self, engine):
        self.engine = engine
        
    def create_user(self, name, email, password):
        with self.engine.connect() as conn:
            conn.execute(users.insert().values(name=name, email=email, password=password))
            conn.commit()

class TasksCRUD:
    def __init__(self, engine):
        self.engine = engine

    def create_task(self, title, description, user_id):
        with self.engine.connect() as conn:
            conn.execute(todos.insert().values(title=title, description=description, user_id=user_id))
            conn.commit()

    