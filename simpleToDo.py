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
    print("1- One Task")
    print("2- More than one task")
    userInput = int(input("Your choice: "))
    if userInput == 1:
        userInput = str(input("Task"))
        tasksList.append(userInput)
    elif userInput == 2:
        print("Note: make sure there is space between each task")
        userInput = str(input("Tasks: "))
        tasksToAdd = userInput.split()
        for i in range(len(tasksToAdd) - 1):
            tasksList.append(i)
        print("Tasks added to the list.")
    else:
        print("Choose from the above options")
elif userInput == 3:
    print("1- One Task")
    print("2- More than one task")
    userInput = int(input("Your choice: "))
    if userInput == 1:
        userInput = str(input("Task"))
        tasksList.remove(userInput)
    elif userInput == 2:
        print("Note: make sure there is space between each task")
        userInput = str(input("Tasks: "))
        tasksToRemove = userInput.split()
        for i in range(len(tasksToRemove) - 1):
            tasksList.remove(i)
        print("Tasks removed from the list.")
    else:
        print("Choose from the above options")
    
        
     
