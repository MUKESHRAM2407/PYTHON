    #quadratic number
a=int(input("Enter the a value: "))
b=int(input("Enter the b value: "))
c=int(input("Enter the c value: "))
d=b*b-4*a*c
if d==0:
    print("Roots are real & equal and the roots are",-b/2*a)
elif d>0:
    s=d**0.5
    n1=-b+s
    n2=-b-s
    d=2*a
    m1=n1/d
    m2=n2/d   
    print("Roots are real & unequal and the roots are",m1,m2)
else:
    print("Roots are imaginary")
