''' Wap to print the weight status of a person using bmi  as shown  in followimg tablle
   BMI                      WEIGHT
   BELOW 18.5               UNDERWEIGHT
   18.5 - 24.9              NORMAL
   25.0-29.9                OVERWEIGHT
   30.0 and above           obese
   note     to calclute BMI:
   input weight (kg) AND HEIGHT (IN CM) AND THEN APPLY THE FORMUL
   weight divided by sqaure root of height'''
weight=float(input("entre the weight"))
height=float(input("entre the height"))
bmi=print(weight/height**2)
if(bmi<18.5):
    print("underweight")
elif(bmi>=18.5 and bmi<=29.5):
    print("normal")
elif(bmi>=25.5 and bmi<=29.5):
    print("overweight")
elif(bmi>30.0):
    print("obease")
else:
    print("false")
