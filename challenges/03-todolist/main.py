from cli import TodoListCLI
from storage import load
from todolist import TodoList, Todo

todolist = TodoList()

predefined_todos = load()

for todo in predefined_todos:
    todolist.add(todo)

todolist_cli = TodoListCLI(todolist)

if __name__ == "__main__":
    try:
        todolist_cli.run()
    except KeyboardInterrupt:
        pass
