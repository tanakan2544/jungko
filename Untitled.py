#!/usr/bin/env python
# coding: utf-8

# In[2]:


#ข้อ1 ผมมีลูกบอล10ลูกมีลูกปิงปองอีก20ลูกเอาไปแบ่งน้อง5คนคนละเท่าๆกันน้องจะได้รับคนละกี่ลูก
a=int(input("ผมมีลูกบอล"))
b=int(input("มีลูกปิงปอง"))
c=int(input("เอาไปแบ่งน้อง"))
print("ผมมีลูกบอลและลูกปิงปองทั้งหมด",a+b,"ลูก")
print("เอาไปแบ่งน้อง",(a+b)/c,"ลูก")


# In[4]:


#ข้อ2 ร้านขายมือถือแห่งหนึ่งมีโปรโมชั่นซื้อ 2 เครื่องขึ้นไปจะลดราคาให้40%
n=int(input("จำนวนมือถือ:"))
money=int(input("ราคา:"))
total= 0
if n> 2:
    total= money-(money*0.4)
    print("ราคาที่ต้องจ่าย",total)
else:
    print("ราคาที่ต้องจ่าย:",money,"บาท")


# In[5]:


#ข้อ3ซื้อปืน6กระบอกราคากระบอกละ20000บาทจะต้องจ่ายเงินกี่บาท
a=int(input("ซื้อปืน"))
b=int(input("ราคากระบอกละ"))
print("ปืน6กระบอกราคา",a*b,"บาท")


# In[6]:


#ข้อ4 เขียนโปรแกรมรับจำนวนเต็มบวก 1 จำนวน จากนั้นให้แสดงผลลัพธ์เป็นจำนวนเต็มดังกล่าวที่เขียนอยู่ในรูปของตัวเลขฐาน สอง
x = int(input("Enter number: "))
x0 = x
sum = ''
d = 0
z = 0
while True:
   y = int(x%2)
   x = int(x/2)
   sum = str(y)+sum
   if y==1:
      z = z+2**d
   if z==x0:
      break
   d = d+1
z = int(sum)
print(z)


# In[1]:


#ข้อ5หาพื้นที่วงกลม
import math
radius = int(input("ค่ารัศมี:"))
result = 2*math.pi*radius
print("พืนที่วงกลม=",result)

        


# In[2]:


#ข้อ6 หาว่าเลขที่หารจำนวนที่กำหนดนั้นหารลงตัวหรือไม่
number =int(input("ตัวตั้งหาร:"))
n= int(input("ตัวหาร:"))
if n % number ==0:
    print("หารลงตัว")
else:
    print("หารไม่ลงตัว")


# In[3]:


#ข้อที่7 ร้านขายหนังสือร้านหนึ่ง พยายามเพิ่มยอดขายโดยการเสนอโปรโมชั่นพิเศษ ถ้าคุณซื้อหนังสือมากกว่า 3 เล่ม ที่มีมูลค่ารวมเกิน 500 บาท คุณจะได้ส่วนลด 10%
count = int(input("How many books: "))
money = int(input("How much: "))
if count > 3 and money > 500:
   s = money-money*0.1
else:
   s = money
print("You have to pay",int(s),"bath.")


# In[6]:


#ข้อ8 กำหนดองศาแล้วนำไปหาค่าsin cos tan
import math
degree = float(input("ใส่องศา:"))
sin      = math.sin(degree)
cos     = math.cos(degree)
tan     = math.tan(degree)
print("sin = ", sin, "cos =",cos, "tan = ",tan)


# In[7]:


#ข้อ9 จงหาผลบวกตั้งแต่ 1ถึง ก 
sum= 0
n = int(input("กรกำหนดค่า ก="))
for i in range (1,n+1):
    sum +=i
print("ผลรวม = ", sum)   


# In[8]:


#ข้อที่10 กำหนดให้1 เมตรเท่ากับ 3.281ฟุต ผ้าผืนหนึ่งยสว กำหนดเอง เมตร จะยาวกี่ฟุต
print("ใช้หน่วยเป็นเมตร")
m=int(input("ผ้ายาว:"))
foot = 3.281
result = m*foot
print("ผ้ายาวทั้งหมด:",result, "ฟุต")


# In[ ]:




