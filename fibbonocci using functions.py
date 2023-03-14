#write a program to print fibbonocci series using recursion by functions till 7 terms

def fb(n):
    if n<2:
        return 1
    return (fb(n-1)+fb(n-2))
n=int(input())
for i in range (n):
    print("fibbonocci(",i,")",fb(i))
