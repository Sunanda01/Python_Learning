# try:
#     a=10//5
#     print(a)
# except ZeroDivisionError:
#     print("Cannot divide by zero")

# try:
#     num = int(input("Enter a number: "))
#     result = 10 / num
# except ValueError:
#     print("Please enter a valid number.")
# except ZeroDivisionError:
#     print("Cannot divide by zero.")

# try:
#     print(10 / 0)
# except Exception as e:
#     print(f"Error: {e}")

# try:
#     x = 5 / 1
# except ZeroDivisionError:
#     print("Division error!")
# else:
#     print("No error, result is:", x)

# try:
#     file = open("data.txt", "r")
#     print(file.read())
# except FileNotFoundError:
#     print("File not found.")
# finally:
#     print("Execution completed.")

# x = -1
# if x < 0:
#     raise ValueError("Negative value not allowed!")