try:
    with open("todos.txt", "r") as f:
        content = print(f.read())
        todoList = content.split("\n")

except FileNotFoundError:
    with open("todos.txt", "w") as f:
        f.write("")

remaining = []

for todo in todoList:
    print(todo)
    userInput = input("Completed? (y/n)")
    if userInput != "y":
        remaining.append(todo)

print(remaining)

while True:
    newItem = input("Add new item? (q to quit)")
    if newItem  == "q":
        break
    else:
        remaining.append(newItem)

with open("todos.txt", "w"):
    output = "\n".join(remaining)
    f.write(output)