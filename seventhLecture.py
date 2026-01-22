name = input("Enter your name: ")
math = int(input("Enter your marks in math: "))
science = int(input("Enter your marks in science: "))
english = int(input("Enter your marks in english: "))
total = math + science + english
percentage = (total / 300) * 100
print(f"Name: {name}")
print(f"total marks: {total}")
print(f"percentage: {percentage:.2f}%")

if percentage >= 90:
    print("You are in A grade")
elif percentage >= 80:
    print("You are in B grade")
elif percentage >= 70:
    print("You are in C grade")
else:
    print("You are failed")
print("Thank you for using our program")