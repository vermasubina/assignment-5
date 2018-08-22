#Q.1-
y= int(input("Enter Year"))
if ((y % 400 == 0) or ((y % 4 == 0) and (y % 100 != 0))):
    print("%d is Leap Year" % y)
else:
    print("%d is Not Leap Year" % y)

#Q.2-
l1=int(input("enter length:"))
b1=int(input("enter breadth:"))
if (l1 == b1):
    print("square")
else:
    print("rectangle")

#Q.3-
a = int(input("enter age of first person"))
b = int(input("enter age of second person"))
c= int(input("enter age of third person"))
if (a > b):
    if (a> c):
        print("a is eldest")
    else:
        print("c is eldest")
else:
    if (b>c):
        print("b is eldest")
    else:
        print("c is eldest")
if (a < b):
    if (a < c):
        print("a is youngest")
    else:
        print("c is youngest")
else:
    if (b < c):
        print("b is youngest")
    else:
        print("c is youngest")


#Q.4-
age=int(input("enter age"))
gender= input("enter gender")
marital= input("enter marital status")
if (gender == 'female'):
    print("she will work only in urban areas")
elif (gender == 'male' and age > 20 and age < 40):
    print("he may work in anywhere")
elif (gender == 'male' and age > 40 and age < 60):
    print("he may work in urban areas only")
else:
    print("error")

# ques-5)
x = int(input("enter quantity "))
price=x*100
discount=10/100
if (price > 1000):
    price=price-discount
    print("cost is",price)
else:
    print("cost is",price)

#LOOPS
    
#Q1-
num=[]
for i in range(10):
    a=int(input('Enter value'))
    num.append(a)
print(num)

#Q2-
'''s=True
while True:
    print("whts up!")'''

#Q.3-
lst=[]
lst2=[]
b=int(input("Enter No of Values"))
for i in range(b):
    c=int(input('Enter element'))
    lst.append(b)
print('List',lst)
for i in range(a):
    c=lst[i]*lst[i]
    lst2.append(c)
print('List of Squared element',lst2)

#Q.4-
list=['subina',1,3.4,'smridhi',2,2.4,'tanmay',4.1,4.2]
a=[]
b=[]
c=[]
for i in list:
    if(type(i)==int):
       a.append(i)
    elif(type(i)==str):
       b.append(i)
    elif(type(i)==float):
       c.append(i)
print(a)
print(b)
print(c)

#Q.5-
n1 = 1
n2 = 100
for num in range(n1, n2 + 1):
    if n1 > 1:
        for i in range(2, num):
            if num % index == 0:
                break
            else:
                print(num)
#Q-6-
for i in range(4):
   print('\n')
   for j in range(0,i+1):
     print('*' , end= ' ')

#ques-7
lst_1=[]
lst_2=[]
a=int(input("Enter  Values"))
for i in range(a):
    b=int(input('Enter digit'))
    lst_1.append(b)
search=int(input("Enter value to search"))
lst_1.remove(search)
print(lst_1)
