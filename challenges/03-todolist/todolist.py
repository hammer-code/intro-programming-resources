class Todo:
    def __init__(self, title, is_done = False):
        self.title = title
        self.is_done = is_done

    def toggle_done(self):
        self.is_done = not self.is_done

class TodoList:
    def __init__(self):
        self.todos = []

    def add(self, todo):
        self.todos.append(todo)

    def clear_done(self):
        filtered_todos = filter(lambda todo: not todo.is_done, self.todos)
        self.todos = list(filtered_todos)

    def toggle(self, index):
        todo = self.todos[index]
        todo.is_done = not todo.is_done

    def get_todos(self):
        return self.todos

    def get_done(self):
        return list(filter(lambda todo: todo.is_done, self.todos))
