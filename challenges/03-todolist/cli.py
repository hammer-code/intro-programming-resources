from todolist import Todo
from storage import save as save_todolist

class TodoListCLI:
    def __init__(self, todolist):
        self.todolist = todolist
        self.menu = {
            '0': 'Lihat daftar todo',
            '1': 'Lihat daftar selesai',
            '2': 'Tambah todo',
            '3': 'Toggle Todo',
            '4': 'Bersihkan yang selesai',
            '5': 'Simpan daftar todo',
            '6': 'Keluar'
        }

    def print_todos(self):
        print("Daftar todo:")

        if len(self.todolist.todos) == 0:
            print("Daftar todo kosong")
            return

        for i, todo in enumerate(self.todolist.get_todos()):
            done_indicator = "[x]" if todo.is_done else "[ ]"

            print(f"{i} {done_indicator} {todo.title}")

    def print_done(self):
        for i, todo in enumerate(self.todolist.get_done()):
            print(f"{i} [x] {todo.title}")

    def add_todo(self):
        title = input("Judul todo: ")
        todo = Todo(title)
        self.todolist.add(todo)

    def clear_done(self):
        self.todolist.clear_done()
        print("Todo yang selesai telah dibersihkan")

    def toggle_todo(self):
        index = input("masukkan index todo: ")
        self.todolist.toggle(int(index))

    def save_todolist(self):
        save_todolist(self.todolist)
        print("Daftar todo telah disimpan")

    def execute(self, menu_index):
        methods_map = {
            '0': 'print_todos',
            '1': 'print_done',
            '2': 'add_todo',
            '3': 'toggle_todo',
            '4': 'clear_done',
            '5': 'save_todolist',
        }
        method_name = methods_map[menu_index]
        handler = getattr(self, method_name)
        handler()

    def print_menus(self):
        for i in self.menu:
            menu = self.menu[i]
            print(f"{i}) {menu}")

    def run(self):
        print("Selamat datang di aplikasi todolist")

        while True:
            print("Silahkan pilih menu")
            self.print_menus()
            menu_index = input("pilihan: ")

            if menu_index == '6':
                break

            print("----")
            self.execute(menu_index)
            print("====")
