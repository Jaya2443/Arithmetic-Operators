#swapping the values of a and b using circumflex

a=12
b=2
a=a//b
b=a*2
a=b//a
print(a)
print(b)



a=11
b=22
print("before swap")
print("a=",a)
print("b=",b)
a=a^b
b=a^b
a=a^b
print("after swap")
print("a=",a)
print("b=",b)
