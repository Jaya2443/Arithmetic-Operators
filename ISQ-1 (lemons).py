#A girl went to temple and she has to distribute 21 lemons among 3 girls.if the amount of lemons are less print lemons are less and if the amount of lemons  are more print lemons are more and if the amount of lemons are equal print lemons are sufficient




x=int (input("enter a number  :"))
a=21
b="lemons are suufiecient"
c="lemons are less"
d="lemons are more"
e="invalid"
print (b  if (x==a) else c if (x<=a) else d if (x>a) else e)
       
