#Patterns
'''pattern prblm depends on rows and columns.
for pattern based we use double iteration.
outer for is considered as rows and inner for considered as colums.
for i=1 j will have 5 stars likewise for i=5,j will execute 25 stars
each and every tym your outer for iteration was initialize.
each and every tym your inner for iteration was reinitialized
for increment we doesnt need to give step size
for decrement we have to give step size'''


#pattern using *
for i in range(1,6):
    for j in range(1,i+1):
        print("*",end=" ")
    print("\n")



    


#pattern using nums
for i in range(1,6):
    for j  in range(1,i+1):
        print(i,end=" ")
    print("\n")

    

    

#pattern using alphabets
for i in range(97,123):
    for j  in range(97,i+1):
        print(chr(i),end=" ")
    print("\n")

    



