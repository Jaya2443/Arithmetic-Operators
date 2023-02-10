#split() Method
'''type-1'''
x,y,z=input("enter a three value num").split()
print("total num of students",x)
print("num of boyss",y)
print("num of girls",z)




'''type-2'''
x,y,z=input("enter a three value num").split('*')
print("total num of students",x)
print("num of boyss",y)
print("num of girls",z)

#output is 200 30 40*2 3 4 5 * 9 8 0


'''type-3'''
x,y,z=input("enter a three value num").split('&')
print("total num of students",x)
print("num of boyss",y)
print("num of girls",z)


'''type-4'''
x,y,z=input("enter a three value num").split('0')
print("total num of students",x)
print("num of boyss",y)
print("num of girls",z)
#10020030



#NOTE:DEFAULT SEPERATOR IS A WHITESPACE 
