

while True:
    print(" 1 Addition")
    print(" 2 substraction")
    print(" 3 multiplicatio")
    print(" 4 Division")
    print(" 5 Enter q or Q to exit")

    choice = input("Enter your choice:")

    if choice == 'q' or choice == 'Q':
        break
    num1 = float(input("Enter number 1:"))
    num2 = float(input("Enter number 2:"))

    if choice =='1':
        print(num1, "+" , num2, "=",(num1+num2))
    elif choice =='2':
        print(num1, "-" , num2, "=" ,(num1-num2))
    elif choice =='3':
        print(num1, "*", num2, "*", (num1*num2))
    elif choice =='4':
        print(num1, "/", num2, "/", (num1/num2))
    else:
        print("error")
    print()
