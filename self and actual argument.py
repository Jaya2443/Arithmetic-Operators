#To create Self argument and access an object

class abc:
    var=10
    def display(self):
        print("this is in class")
obj=abc()
print(obj.var)
obj.display()
