#WAP to input three number and print the largrst number
num1=int(input("enter the first number"))
num2=int(input("enter the second number"))
num3=int(input("enter the third number"))
if(num1>num2):
    if(num1>num3):
        print(f"number {num1} is greater")
elif(num2>num3):
    if(num2>num3):
        print(f'number {num2} is greater')
else:
     print(f'number {num3}is greater')
     
        

