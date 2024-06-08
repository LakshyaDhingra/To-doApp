def get_todos(filepath):
    """Read a text file and return a list of
    to-do items.
    """
    with open(filepath, "r") as file:
        todos = file.readlines()
        return todos


def writelines_todos(filepath, todos_list):
    """Write the list to-do items in a text file."""
    with open(filepath, "w") as file:
        file.writelines(todos_list)


def print_todos():
    """Printing the to-do items from the text file"""
    # Using list comprehension to remove extra breaks from showing to dos
    todos = get_todos("userdatafiles/todos.txt")
    new_todos = [item.strip("\n") for item in todos]
    for index, item in enumerate(new_todos):
        item = item.title()
        row = f"{index + 1}. {item}"
        print(row)


if __name__ == "__main__":
    print("Hello")
    print(get_todos())
