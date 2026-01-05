import database

db = database.Database()

class todoList:

    #Initialize database
    db.createTasksDb()

    #Add Tasks
    def add_task(self, title:str, description:str):
        try:
            with db.get_connection() as conn:
                with conn.cursor() as cur:
                    cur.execute("INSERT INTO Tasks (title, description) VALUES (%s, %s)", (title, description))
        except Exception as e:
            print("An error occurred while adding a task:", e)
            raise

    #Update Tasks
    def update_task(self, id:int, title:str, description:str):
        try:
            with db.get_connection() as conn:
                with conn.cursor() as cur:
                    cur.execute("UPDATE Tasks SET title = %s, description = %s WHERE id = %s", (title, description,id))
        except Exception as e:
            print("An error occurred while updating a task:", e)
            raise

    #Delete task by id
    def delete_task(self, id: int):
        try:
            with db.get_connection() as conn:
                with conn.cursor() as cur:
                    cur.execute("DELETE from Tasks WHERE id =  %s",(id,))
        except Exception as e:
            print("An error occurred while deleting a task:", e)
            raise

    #Delete all tasks
    def delete_all_tasks(self):
        try:
            with db.get_connection() as conn:
                with conn.cursor() as cur:
                    cur.execute("DELETE from Tasks")
        except Exception as e:
            print("An error occurred while deleting all tasks:", e)
            raise


    #Show all tasks from the table
    def show_tasks(self):
        try:
            with db.get_connection() as conn:
                with conn.cursor() as cur:
                    cur.execute('SELECT * FROM Tasks')
                    rows = cur.fetchall()
            for row in rows:
                print(row)
        except Exception as e:
            print("An error occurred while fetching tasks:", e)
            raise

    
    

