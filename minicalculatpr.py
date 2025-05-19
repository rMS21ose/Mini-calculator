print("Your choices are : +, -, *, /, %")
choice = input("Enter your choice:")
a = int(input("enter num1:"))
b = int(input("enter num1:"))
if(choice=="+"):
    print("YOUR NUMBER HAS BEEN ADDED",a+b)
elif(choice=="-"):
    print("YOUR NUMBER HAS BEEN SUBRACTED",a-b)
elif(choice=="*"):
    print("YOUR NUMBER HAS BEEN MULTIPLIED",a*b)
elif(choice=="/"):
    print("YOUR NUMBER HAS BEEN DIVIDED",a/b)
elif(choice=="%"):
    print("YOUR NUM'S REMINDER HAS BEEN FOUND",a%b)
else:
    print("you have entered a wrong input")
