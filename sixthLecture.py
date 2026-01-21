# name = input("Enter your name: ")
# age = input("Enter your age: ")
# city = input("Enter your city: ")
# print("sallam!", name, "you are", age, "years old and you live in", city)

# print("Hello", end=" " )
# print("World")

# print("Hello","World", sep="-" )
# print("line1\nline2\nline3") #newline
# print("line1\tline2\tline3") #tab
# print("line1\rline2\rline3") #carriage return
# print("line1\bline2\bline3") #backspace
# print("Quote\"Hello\"")

name = input("Enter your name: ")
marks = int(input("Enter your marks in percentage: "))
# print(f"Hello {name} you have {marks} % marks")
print("Hello {} you have {} % marks".format(name, marks))