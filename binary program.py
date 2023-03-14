'''case-1: input1=6 , input2=101000
           output=1

   case-2: input1=9 , input2=101111110'''

size=int(input("enter the size"))
max=count=flag=0
binput=input()
arr=list(binput)
for i in range(0,size):
    if arr[i]=='1':
        count+=1
        flag=1
    elif(arr[i]=='0' and flag==1):
        count=0
        flag=0
    if count>max:
        max=count
