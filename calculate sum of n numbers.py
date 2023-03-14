#program to calculate sum of n numbers

'''using for '''

n= int(input("enter num"))
sum=0
for i in range(0,n+1):
    sum=sum+i
print("sum is",sum)

    
    


'''using while'''

n=int(input("enter a num"))
i=1
s=0
while(i<=n):
    s=s+i
    i+=1
print("sum is",s)




'''using list'''

num =[0,1,2,3,4,5,6,7,8,9,10]
print(sum(num))
