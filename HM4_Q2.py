import math
from math import *
a=input("enter the number1>")
a=int(a)
b=input("enter the number2>")
b=int(b)
z=0

oprat=input("enter the number oprat\n"
      "1_+\n"
      "2_ -\n"
      "3_ *\n"
      "4_ /\n"
      "5_ ^\n"
      "6_ %\n"
            ">>>>>")
if oprat.isdigit():
    oprat = int(oprat)
    c=""
if oprat==1 or oprat=='+':
    z=a+b
    c="+"
elif oprat==2:
    z=a-b
    c = "-"
elif oprat==3:
    z=a*b
    c = "*"
elif oprat==4:
    z=a/b
    c = "/"
elif oprat==5:
    z=a^b
    c = "^"
elif oprat==6:
    z=a%b
    c = "%"
else:print("erorr:enter the number correct")
print(z)
oprat2=input("enter the num oprat\n"
             "1_ceil or floor or round\n"
             "2_ without a decimal point\n"
             "3_Exit\n"
             ">>>>>>")
oprat2=int(oprat2)
if oprat2==1:
    oprat2=input("enter the num oprat\n"
                 "1_cill\n"
                 "2_floor\n"
                 "3_round\n"
                 ">>>>")
    oprat2=int(oprat2)
    if oprat2==1:
        z=math.ceil(z)
    elif oprat2==2:
        z=math.floor(z)
    else:
        z=math.round(z)
elif oprat2==2:
    z=int(z)
else:
    print("exit")
print(a,c,b,'=',z)