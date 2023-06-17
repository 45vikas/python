# build a calculator using pythin language
first=int(input("enter the first num"))
operator=input("entre the operators (+,-,%,/,*)")
second=int(input("entre the second nnum"))
if(operator=='+'):
    print(first+second)
elif(operator=='-'):
    print(first-second)
elif(operator=='*'):
    print(first*second)
elif(operator=='%'):
    print(first%second)
elif(operator=='/'):
    print(first/second)
else:
    print("invlid operation")
