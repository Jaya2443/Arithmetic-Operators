#Program to display the time taken by the compiler to execute a program

from time import*
t1=perf_counter()
i=sum=0
while i<1000000:
    sum+=i
    i+=1
sleep(0)
t2=perf_counter()
print("execution time=%f seconds"%(t2-t1))
