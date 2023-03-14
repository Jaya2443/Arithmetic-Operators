#write a program using functions to check whether the given number is krishnamurthy umber or not
'''krishna murthy number is nothing but a strong number'''
'''for example : 145
                 1!+4!+5!=145
                 1+24+120=145
                 145=145
    hence,145 is a strong number '''


import math
num=int(input("enter the number"))
x=num
sum=0
while x>0:
    fact=1
    r=x%10
    fact=math.factorial(r)
    sum=sum+fact
    x=x//10
if sum==num:
    print("it is krishnamurthy number",num)
else:
    print("it is not krishnamurthy number",num)





#using def function

def fact(n):
    if n==1:
        return n
    else:
        return n*fact(n-1)
sum,num=0,0
n=int(input())
num=n
while n!=0:
    r=n%10
    sum=sum+fact(r)
    n=n//10
if sum==num:
     print("it is krishnamurthy number")
else:
    print("it is not krishnamurthy number")



    
