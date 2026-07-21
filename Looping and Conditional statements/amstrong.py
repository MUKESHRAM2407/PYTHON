n=int(input("Enter the number"))
sum=0
temp=n
while temp>0:
    a=temp%10
    sum+=a*a*a
    temp=temp//10
if sum==n:
    print("The given number is amstron")
else:
    print("Not a amstrong")



def arm(n):
    temp=n
    sum=0
    while temp>0:
        a=temp%10
        sum+=a*a*a
        temp=temp/10
