#Program to make a list of even and odd numbers from the given series
'''  n1=11
     n2=12
     n3=13
     n4=27
     n5=7  '''

class number:
    even=[]
    odd=[]
    def __init__(self,num):
        self.num=num
        if num%2==0:
            number.even.append(num)
        else:
            number.odd.append(num)
n1=number(11)
n2=number(12)
n3=number(13)
n4=number(27)
n5=number(7)
print("even numbers are",number.even)
print("odd numbers are",number.odd)





class Number:
    even=[]
    odd=[]
    def __init__(self,num):
        self.num=num
        if num%2==0:
            Number.even.append(num)
        else:
            Number.odd.append(num)
n1=Number(11)
n2=Number(13)
n3=Number(12)
n4=Number(28)
n5=Number(7)
print(Number.even)
print(Number.odd)
