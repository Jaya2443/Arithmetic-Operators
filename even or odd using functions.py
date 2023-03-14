#Write a program to check whether the given number is even or odd by using a single stance class,object within attribute following the constructor
'''teest case1=21'''


class number:
    even=0
    def check(self,num):
        if num%2==0:
            self.even=1
    def even_odd(self,num):
        self.check(num)
        if self.even==1:
            print(num,"is even")
        else:
            print(num,"is odd")
n=number()
n.even_odd(21)



