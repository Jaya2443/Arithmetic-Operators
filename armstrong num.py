#to check whether a num is armstrong num or not

n=int(input("enter a number"))
s=n
b=len(str(n))
sum=0
while(n!=0):
    r=n%10
    sum=sum+(r**b)
    n=n//10
if s==sum:
    print("armstrong num")
else:
    print("not armstrong num")    

