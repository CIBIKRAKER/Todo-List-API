import todo




def main():
    tasks = todo.todoList()

    tasks.update_task(7, "Caine", "Odak aponun orospu anasinda")


    tasks.show_tasks()


if __name__ == "__main__":
    main()
