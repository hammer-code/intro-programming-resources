import csv
from todolist import Todo

def save (todolist):
    with open('db.csv', 'w+') as file:
        for todo in todolist.todos:
            file.write(f"{todo.title},{todo.is_done}\n")

def _csv_row_to_todo(row):
    return Todo(
        row[0],
        True if row[1] == "True" else False
    )

def load ():
    todos = []
    try:
        with open('db.csv', 'r') as file:
            reader = csv.reader(file, delimiter=',')
            for row in reader:
                todos.append(_csv_row_to_todo(row))
    except FileNotFoundError:
        pass

    return todos
