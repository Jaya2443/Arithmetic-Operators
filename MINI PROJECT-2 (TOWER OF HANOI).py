#Tower Of Hanoi

'''Tower of Hanoi is a mathematical puzzle where we have three rods (A, B, and C) and N disks. Initially, all the disks are stacked in decreasing value of diameter i.e., the smallest disk is placed on the top and they are on rod A. The objective of the puzzle is to move the entire stack to another rod (here considered C), obeying the following simple rules: 

   - Only one disk can be moved at a time.
   - Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack i.e. a disk can only be moved if it is the uppermost disk on a stack.
   - No disk may be placed on top of a smaller disk'''

def hanoi(n,a,b,c):
    if n>0:
        hanoi(n-1,a,c,b)
        if a:
            c.append(a.pop())
        hanoi (n-1,b,a,c)
a=[1,2,3,4]
b=[]
c=[]
print ("before puzzle",a,b,c)
hanoi(len(a),a,b,c)
print("after puzzle",a,b,c)
