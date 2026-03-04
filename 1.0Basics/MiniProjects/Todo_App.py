print(" ---------- WELCOME TO TASK MANAGEMNET APP ---------- ")
task_num=int(input("Enter how many task you want to add = "))
task_list={}
for i in range(1,task_num+1):
    task=input(f"Enter Task {i} => ")
    task_list[i]=task
print(f"Your Task List is \n{task_list}")
flag=True
while flag:
    choice=int(input('Enter\n1 Add\n2 Update\n3 Delete\n4 View\n0 Exit/Stop\nYour Choice=>  '))
    if choice==1:
        length=len(task_list)
        task=input(f"Enter Task {length+1} => ")
        task_list[length+1]=task
        print("Task Added Successfully")
    elif choice==2:
        task_pos=int(input("Enter the task number you want to update=> "))
        task=input(f"Update Task {task_pos} => ")
        task_list[task_pos]=task
        print("Task Updated Successfully")
    elif choice==3:
        task_pos=int(input("Enter the task number you want to delete=> "))
        del task_list[task_pos]
        print("Task Deleted Successfully")
    elif choice==4:
        if len(task_list)==0:
            print("List is Empty!!!!!!!!!!")
        else:
            print(task_list)
    elif choice==0:
        print("GOOD BYE!!!!!!!!!!")
        flag=False
    else:
        print("INVALID CHOICE!!!!!!!!!!!!!!")
        flag=False