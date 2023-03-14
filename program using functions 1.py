#write a program with a user defined function which returns an integer value to the caller
'''method-1'''


def cube(x):
    result= x**3  #[x*x*x or pow(3,x)]
    print("value is",result)
cube(3)





'''method-2'''


def cube(x):
    return (x*x*x)
num=10
result=cube(num)
print("output of evaluation is ",result)
