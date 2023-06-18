'''#while loop
i=1
while(i<=200):
    print(i)
    i=i+1'''
'''#using while loop print astricks
i=1
while(i<=5):
    print(i*"*")
    i=i+1

i=5
while(i>=0):
    print(i*"$")
    i=i-1

i=1
while(i<=5):
    print(i*"%")
    i=i+1'''
'''# while loop  while(condition) #statement
i=1
while(i<=10):
    print(i)
    i=i+1

#wap t oinput a number and print the sum of its number

num=int(input("enter the num"))
s=0
while(num!=0):
    rem=num%10
    s=s+rem
    num=num//10
print(s)

#wap to input the number and find wheather it is amstrong number or not  153= 1^3+5^3+3^3=153
num=int(input("enter the number"))
c=n
s=1
r=n%10
n=n//10
s=r=r+r
r2=n%10
s+=r2+r2+r2
n=n//10
r3=n%10
s+=r3+r3+r3
if(s==c):
    print("amstrong num")
else:
    print("not")
    
     
    
    




#WAP input a number and check wheather it is palindrome or not'''


'''#break ststement
for i in range(1,11):
        if(i==5):
            break
        else:
            print(i)

for i in range(1,11):
    if(i==5):
        continue
    else:
        print(i)'''


'''# WAP to input the a number and find wheather ir is prime or not
num=int(input("entre the number"))
if(num==1):
        print("not prime")
else:
    for i in range(2,num):
        if(num%1==0):
           print("prime numberr")
           break
    else:
        print("prime number")

#nested loop

for i in range(1,11):
        for j in range(1,11):
                print(i,j)
        print()'''

#WAP to print prime number 15 to 30
#WAP to print multiplication table of all the number from 1 to 10

'''# astricks fomation
for i in range(1,5):
        print(i*'*')
        i=i+1

# table 1 to 10
for i in range(1,11):
        for j in range(1,11):
                print(i*j)
        print()
                
# prime number
n=1
for i in range(15,31):
        if i>1:
                for j in range(2,j):
                        if(num%j==0):
                                print(j)
                                break
                        else:
                                print("not primr")'''
#infinite loop
while(True):
        print("hello")
        break

num=30
while(num==30):
        print("hello")
        break




        





























































    


