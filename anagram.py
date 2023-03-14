#to check whether the given input is anagram or not

'''test case-1: input1=listen , input2=silent
                output=true
   test case-2: input1=race , input2=acer
                outut=true                 '''


str1=input("enter 1")
str2=input("enter 2")
n=len(str1)
m=len(str2)
if n==m:
    if sorted(str1)==sorted(str2):
        print("anagram")
    else:
        print("not anagram")
else:
    print("not anagram as length differs")
    
