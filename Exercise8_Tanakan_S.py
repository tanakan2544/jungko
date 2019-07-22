#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''นาย ธนาคาร สายรีรักษ์ 362515241006 EE36241N '''
a=input("Username :")
b=input("Password :")
if a=="4567" and b=="2587":
    print("Welcome to Icecream Shop.")
    print("-------------------Menu-------------------")
    print("Welcome to Icecream Shop")
    print("1. Strawberry 80 THB")
    print("2. Vanila 50 THB")
    print("3. Chocolate 40 THB")
    print("4. Lemon 90 THB")
    print("5. Milk 10 THB")
    hhe =int(input("What do you want?(1-5) : "))
    toy=int(input("How many do you want? : "))
    if hhe==1:
        print("You order ",toy," of Strawberry ",S*toy, " THB")
    elif hhe==2:
        print("You order ",toy," of Vanila ",V*toy, " THB")
    elif hhe==3:
        print("You order ",toy," of Chocolate ",C*toy, " THB")
    elif hhe==4:
        print("You order ",toy," of Lemon ",L*toy, " THB")
    elif hhe==5:
        print("You order ",toy," of Milk ",M*toy, " THB")
    
else :
    print("Error ,please try again.")
S=80
V=50
C=40
L=90
M=10

