#ncr
def fact(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f

n=int(input("Enter the n value: "))
r=int(input("Enter the r value: "))

c=n-r
factn=fact(n)
factr=fact(r)
factc=fact(c)
ncr=factn//factr*factc

print("Your result is",ncr)
