#Geometric Series

'''0,0,7,6,14,12,21,18,28,24,.........'''


term=int(input("enter a num"))
if term%2==0:
    print(6*(term//2-1))
else:
    print(7*(term//2-1))
