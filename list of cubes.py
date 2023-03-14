#program to make a list of cubes till the value n

'''using for'''

x=int(input("enter a num"))
for i in range (1,x):
    print("cubes are",i**3)

    

    
   
'''using append list'''

n=int(input("enter a num"))
cubes=[]
for i in range(n):
    cubes.append(i**3)
print(cubes)




    

'''using while'''

x=int(input("enter a num"))
i=1
while(i<=x):
    print("cubes",i**3)



