# from functions import get_todos, write_todos
import functions
import time

now = time.strftime("%b %d, %Y %H:%M")
print("It is", now)


while True:
    user_action = input("Type add, show, complete, edit or exit: ")
    user_action = user_action.strip().lower()

    if user_action.startswith('add'):
        todo = user_action[4:] + '\n'

        todos = functions.get_todos()

        todos.append(todo)

        functions.write_todos(todos)

    elif user_action.startswith('show'):
        todos = functions.get_todos()

        new_todo = [todo.strip('\n') for todo in todos]
        for index, todo in enumerate(new_todo):
            print(f"{index + 1}. {todo}")

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])

            number = number - 1

            todos = functions.get_todos()

            new_todo = input("Enter a new todo: ")

            todos[number] = new_todo + '\n'

            functions.write_todos(todos)

        except ValueError:
            print("Your command is not valid")
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])
            index = number - 1

            todos = functions.get_todos()

            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            functions.write_todos(todos)

            print(f"Todo {todo_to_remove} was removed from the list.")
        except IndexError:
            print("There is no item with that number")
            continue

    elif user_action.startswith('exit'):
        break
    else:
        print("Command is not valid")
