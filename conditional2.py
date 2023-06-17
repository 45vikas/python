#year leap or not
#4
op=input("entre the operators")
a=int(input("ente the first number"))
b=int(input("entre the second number"))
if(op=='+'):
      print(a+b)
elif(op=='-'):
    print(a-b)
elif(op=='*'):
    print(a*b)
elif(op=='/'):
    print(a/b)
elif(op=='**'):
    print(a**b)
elif(op=='%'):
    print(a%b)
elif(op=='//'):
    print(a//b)
else:
    print("invalid operators")

    #i
year=int(input("entre the year"))
if(year%4==0 and year%400==0 and year%100==0):
    print("leap year")
else:
    print("not leap year")
