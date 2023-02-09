#ternary operator to get smallest of two values

a=1000
b=1500
print( a if (a<b ) else b if( b<c  ) else c ) 



#ternary operator to get smallest of three values

a=1000
b=1500
c=400
print( a if (a<b and a<c ) else b if( b<c  ) else c ) 



#ternary operator to get smallest of four values

a=1000
b=1500
c=400
d=20
print( a if (a<b and a<c and a<d ) else b if( b<c and b<d  ) else c if(c<d ) else d)



#ternary operator to get smallest of five values

a=1000
b=1500
c=5000
d=4000
e=2000
print ( a if (a<b and a<c and a<d and a<e ) else b if (b<c and b<d and b<e) else c if (c<d and c<e) else d if (d<e) else f)

