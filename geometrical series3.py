#Geometrical series

'''0,0,2,1,4,2,6,3,8,4,10,5,12,6,......'''


term=int(input("enter a num"))
if term%2==0:
    term=term//2
    print(1*(term-1))
else:
    term=term//2+1
    print(2*(term-1))

