#nested if
#WAP to input ther the three ni and arrange in acendinh order
num1=int(input("enter the first number"))
num2=int(input("enter the second number"))
num3=int(input("enter the third number"))
if(num1<num2 and num1<num3):
    if(num2<num3):
        print(num1, num2 , num3)
    else:
        print(num1 , num2 , num3)
elif(num2<num1 and num2<num3):
    if(num1<num3):
        print(num2,  num 1 , num3)
    else:
        print(num2, num3 , num3)
else:
    if(num1<num2):
        print(num3, num1, num2)
        else:
            print(num3,num2, num1)
