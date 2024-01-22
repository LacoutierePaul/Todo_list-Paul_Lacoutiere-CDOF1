class Todo:
    def __init__(self, my_todos, idx, completed=False):
        self.my_todo = my_todos
        self.idx = idx
        self.completed = completed

    def __str__(self):
        return f"{self.idx} - {self.my_todo} - Completed : {self.completed}"

    def change_completed(self):
        self.completed = True # Test


if __name__ == "__main__":
    todo_list = []
    index = 1
    while True:
        print("Welcome to your todo list")
        print("Here are your options:")
        print("1 - Add todo")
        print("2 - Remove todo")
        print("3 - View todo list")
        print("4 - Complete todo")
        print("5 - View completed todo list")
        print("6 - Exit")
        print("Please enter your choice:")

        try:
            choice = int(input())
        except ValueError:
            print("Please enter a number")
            continue

        if choice == 1:
            print("Please enter your todo to add:")
            todo = input()
            my_todo = Todo(todo, index)
            todo_list.append(my_todo)
            index += 1

        elif choice == 2:
            print("Please enter the number of the todo to remove:")
            number = int(input())
            for todo in todo_list:
                if todo.idx == number:
                    todo_list.remove(todo)
                    break
            else:
                print("No todo found with this id")

        elif choice == 3:
            if not todo_list:
                print("No todos found")
            else:
                for todo in todo_list:
                    if not todo.completed:
                        print(todo)
                    else:
                        print("No uncompleted todos found")

        elif choice == 4:
            print("Please enter the number of the completed todo:")
            number = int(input())
            for todo in todo_list:
                if todo.idx == number:
                    todo.change_completed()
                    break
            else:
                print("No todo found with this id")

        elif choice == 5:
            if not todo_list:
                print("No todos found")
            else:
                for todo in todo_list:
                    if todo.completed:
                        print(todo)
                else:
                    print("No completed todos found")

        elif choice == 6:
            print("Thanks for using the todo list. Goodbye!")
            break
        else:
            print("Please enter a valid choice")