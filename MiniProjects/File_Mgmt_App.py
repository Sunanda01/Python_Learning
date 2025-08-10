import os
def create_file(filename):
    try:
        with open(filename,'x'):
            print(f" ~ ~ ~ ~ ~ FileName {filename} created successfully ~ ~ ~ ~ ~ ")
    except FileExistsError:
        print(f'File Already Exists!!!!!!!!!!')
    except Exception as e:
        print(f'Error Occurred {e}!!!!!!!!!!!')

def view_files():
    files=os.listdir()
    if not files:
        print("No File Found!!!!!!!!!")
    else:
        print(" ~ ~ ~ ~ ~ Files in directory ~ ~ ~ ~ ~ ")
        for file in files:
            print(file)

def read_file(filename):
    try:
        with open(filename,'r') as f:
            content=f.read()
            print(f" ~ ~ ~ ~ ~ Content of FileName {filename} ~ ~ ~ ~ ~ \n{content}")
    except FileNotFoundError:
        print(f"{filename} File Not Found!!!!!!!!!")
    except Exception as e:
        print(f'Error Occurred {e}!!!!!!!!!!!')

def write_file(filename):
    try:
        with open(filename,'a') as f:
            content=input('Enter content to add\n')
            f.write(content+"\n")
            print(f" ~ ~ ~ ~ ~ File Updated {filename} successfully ~ ~ ~ ~ ~ ")
    except FileNotFoundError:
        print(f"{filename} File Not Found!!!!!!!!!")
    except Exception as e:
        print(f'Error Occurred {e}!!!!!!!!!!!')

def delete_file(filename):
    try:
        os.remove(filename)
        print(" ~ ~ ~ ~ ~ File Deleted Successfully ~ ~ ~ ~ ~ ")
    except FileNotFoundError:
        print(f"{filename} File Not Found!!!!!!!!!")
    except Exception as e:
        print(f'Error Occurred {e}!!!!!!!!!!!')

def main():
    print("---------- FILE MANAGEMENT APP ---------- ")
    flag=True
    while flag:
        choice=int(input('''
1. Create File
2. View All File
3. Delete File
4. Read File
5. Edit File
0. Exit
Enter your choice => '''))
        if choice==1:
            filename=input("Enter the File Name = ")
            create_file(filename)
        elif choice==2:
            view_files()
        elif choice==3:
            filename=input("Enter the File Name = ")
            delete_file(filename)
        elif choice==4:
            filename=input("Enter the File Name = ")
            read_file(filename)
        elif choice==5:
            filename=input("Enter the File Name = ")
            write_file(filename)
        elif choice==0:
            print(" ~ ~ ~ ~ ~ Good Bye ~ ~ ~ ~ ~ ")
            flag=False
        else:
            print("INVALID INPUT!!!!!!!!!!!!\nTRY AGAIN\n")
            
if __name__=="__main__":
    main()