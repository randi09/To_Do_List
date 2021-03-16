# store dictionaries in a list +++
# make dictionary(ies)+++
# delete something on a list
# add something to a list +++
# view everything on the list +++
# have a way to quit +++
# can't stop won't stop until Q :check +++
# MAKE THEM IN FUNCTIONS check in progress +++


toDoList = []




def adding_task():
    # how do we add to a list
    toDoDictionary = {}
    taskToAdd = input("What task would you like to add?")
    priorityOfTask = input("What priority is this? high, medium, low?")

    # how do we add a "title" key and a "priority" value
    toDoDictionary["title"] = taskToAdd
    toDoDictionary["priority"] = priorityOfTask
    toDoList.append(toDoDictionary)

    return print("I added * %s * to your list of things to do" % taskToAdd)


def view_task():
    count = 1
    print("Here is a list of your todos")
    for task in toDoList:
        print(" %d. %s = %s " % (count, task["title"], task["priority"]))
        count += 1
    return print("Here ya go")


def delete_task():
    print("Here is your todos")
    view_task()
    taskToDelete = int(input("What task would you like to delete"))
    # toDoList.pop(taskToDelete - 1)
    taskToDeleteIndex = taskToDelete - 1
    taskThatIsGettingDeleted = toDoList[taskToDeleteIndex]
    del toDoList[taskToDeleteIndex]
    return print("I deleted %s off your list" % taskThatIsGettingDeleted)


def which_task(userInput):
    whatTheyInput = ""
    if(userInput == "1"):
        whatTheyInput = adding_task()
    elif(userInput == "2"):
        whatTheyInput = delete_task()
    elif(userInput == "3"):
        whatTheyInput = view_task()
    elif(userInput == "q"):
        
    #else:
        print("Wrong Key Pressed")


    whatTheyInput = choice
    return whatTheyInput


choice = ""
while(choice != "q"):
    userChoices = input("What would you like to do?")
    outcome = which_task(userChoices)
    choice = outcome