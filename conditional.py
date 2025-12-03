day_of_week = input("enter day of the week: ").lower()

print(day_of_week)
#print(day_of_week2)

if day_of_week == "saturday" or day_of_week == "sunday":
    print("I will practice live ")
else:
    print("I will practice offline ")

num1 = int(input("Enter your first number"))
num2 = int(input("Enter your second number"))

choice = input("Enter the operation : (option are +,-,/,*,%)")

if choice == "+":
    add = num1 + num2
    print("additon: ", add)
elif choice == "-":
    sub = num1-num2
    print("substraction: ", sub)
elif choice == "/":
    division= num1/num2
    print("Division: ", division)
elif choice == "*":
    multiple=num1*num2
    print("Multiplication: ", multiple)
elif choice == "%":
    percentage=num1%num2
    print("Remainder: ", percentage)
else:
    print("invalid choice")

    




