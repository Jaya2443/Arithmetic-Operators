#global and local variables

var='vijay'
def show():
    global var1
    var1='tall'
    print("in function variable is ",var)
show()
print("outside function",var1)
print("variable is",var)
    
