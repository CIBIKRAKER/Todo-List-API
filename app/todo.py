import database

db = database.Database()

class todoList:

    #Initialize database
    db.createTasksDb()

    #Add Tasks
    def add_task(self, title:str, description:str):
        with db.get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("INSERT INTO Tasks (title, description) VALUES (%s, %s)", (title, description))

    #Update Tasks
    def update_task(self, id:int, title:str, description:str):
        with db.get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("UPDATE Tasks SET title = %s, description = %s WHERE id = %s", (title, description,id))


    #Delete task by id
    def delete_task(self, id: int):
        with db.get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("DELETE from Tasks WHERE id =  %s",(id,))
    #Delete all tasks
    def delete_all_tasks(self):
        with db.get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("DELETE from Tasks")

    #Show all tasks from the table
    def show_tasks(self):
        with db.get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute('SELECT * FROM Tasks')
                rows = cur.fetchall()
        for row in rows:
            print(row)

    
    

