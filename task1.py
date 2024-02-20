tasks=[]

def addTask():
    task=input("please enter a task:")
    tasks.append(task)
    print("TASK ADDED SUCCESSFULLY")

def deleteTask():
    listTasks()
    try:
        taskToDelete=int(input("enter the no of task to delete in the sequence"))
        if taskToDelete>=0 and taskToDelete<len(tasks):
            tasks.pop(taskToDelete)
            print("TASK DELETED SUCCESSFULLY")
    except:
            print("TASK NOT FOUND")    

def listTasks():
    if not tasks:
        print("THERE ARE NO TASKS IN THE LIST")
        
print("WELCOME TO THE TO DO APPLICATON ")
print("- - - - - - - - - - - - - - - \n")
print("please select any of the options below \n")
print("- - - - - - - - - - -")
print("- - - - - - - - - - -")
print("1. Add new task")
print("2. Delete existing task")
print("3.Exit")
print("- - - - - - - - - - -")
print("- - - - - - - - - - -")

while True:
    select=int(input("Select the option from above \n"))

    if(select==1):
        addTask()


    elif(select==2):
        deleteTask()
    

    elif(select==3):
        print("thank you , visit again!!")        

    else:
        print("invalid input")




