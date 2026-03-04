
class Error(Exception):
   pass
class invalidAge(Error):
    pass
try:
    age=int(input("Enter your age=> "))
    if(age>=18):
        print("You are eligible")
    else:
        raise invalidAge("Age not valid")
except invalidAge as e:
    print(e)
# else:
#     print("Validation Done")
finally:
    print("Validation Done")

# class Error(Exception):
#    pass
# class invalidAge(Error):
#     pass
# try:
#     age=int(input("Enter your age=> "))
#     if(age>=18):
#         print("You are eligible")
#     else:
#         raise invalidAge
# except invalidAge:
#     print("Invalid Age")
# # else:
# #     print("Validation Done")
# finally:
#     print("Validation Done")
