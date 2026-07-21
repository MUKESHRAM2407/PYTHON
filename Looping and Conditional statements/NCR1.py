#NCR
fact1=fact2=fact3=1
n=int(input("Enter the element:"))
r=int(input("Enter the element as r:"))
for i in range(1,n+1):
    fact1=fact1*i
for i in range(1,r+1):
    fact2=fact2*i
a=n-r
for i in range(1,a):
    fact3=fact3*i
ncr=fact1/fact2*fact3
print(ncr)

#npr
n=int(input("Enter the element as n:"))
r=int(input("Enter the element as r:"))
fact1=fact2=1
for i in range(1,n+1):
    fact1=fact1*i
a=n-r
for i in range(1,a):
    fact2=fact2*i
npr=fact1/fact2
print(npr)
