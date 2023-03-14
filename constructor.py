#Program to check the use of a constructor in a method

class abc:
    def __init__(self,value):
         print("This is in class")
         self.value="value"
         print("the value is",value)
obj=abc(100)
