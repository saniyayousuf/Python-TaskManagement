def task():
    tasks = []  # empty List
    print("-----welcome To The Task Management App--------")

    total_task =int(input("Enter How many tasks you want to add = ")) #any integer eg 5
    for i in range(1, total_task+1):
        task_name =  input(f"Enter task {i} = ") #enter task 3 =
        tasks.append(task_name)

    print(f"Todays Tasks are \n{tasks}") 

    while True:
        Operation = int(input("Enter \n1-Add Task\n2-Update Task\n3-Delete Task\n4-View Task\n5-Exit")) 
        if Operation == 1:
            add = input("Enter task you want to add = ")
            tasks.append(add)
            print(f"Task {add} has been successfully added....")

        elif Operation == 2:
            updated_val = input("Enter the task name you want to update = ")
            if updated_val in tasks:
                up = input("Enter new task = ")
                ind = tasks.index(updated_val)
                tasks[ind] = up
                print(f"Updated task {up}....")

        elif Operation == 3:
            del_val = input("which task you want to delete = ")
            if del_val in tasks:
                ind = tasks.index(del_val)
                del tasks[ind]
                print(f"Task {del_val} has been deleted....")

        elif Operation == 4:
            print(f"Total task = {tasks}")

        elif Operation == 5:
            print("Closing the Progress") 
            break

        else:
            print("Invalid Input")
task()