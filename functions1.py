#functions
#syntax : def(user-defined variable name)(parameters/arguments)


'''basic program to perform arithmetic operations using function'''

def total(a,b):
    result=a+b
    print("result is",result)
def diff(a,b):
    result1=a-b
    print("result is",result1)
def mul(a,b):
    result2=a*b
    print("result is",result2)
def div(a,b):
    result3=a/b
    print("result is",result3)
a=int(input("enter the value of a is:"))
b=int(input("enter the value of b is:"))
total(a,b)
diff(a,b)
mul(a,b)
div(a,b)


