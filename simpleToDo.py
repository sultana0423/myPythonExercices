# Simple To-Do List: Develop a basic to-do list application where users can add, remove, and view tasks.

print("Simple To-Do List")
print("1- View Tasks")
print("2- Add a Task")
print("3- Remove a Task")

tasksList = ["shower", "cook", "workout"]
userInput = int(input("Choose an operation: "))

if userInput == 1:
    if len(tasksList) == 0:
        print("You have no tasks in the list")
    else:
        print("To Do List:")
        for i in range(len(tasksList) - 1):
            print(tasksList[i])
elif userInput == 2:
    tasksToAdd = []
    print("1- One Task")
    print("2- More than one task")
    userInput = int(input("Your choice: "))
    if userInput
     

