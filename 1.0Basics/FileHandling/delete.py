import os
if os.path.exists("f3.txt"):
    os.remove("f3.txt")
    print("Deleted Successfully!!!!!!!!!!!")
else:
    print("The file does not exist")
