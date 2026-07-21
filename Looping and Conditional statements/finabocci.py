#fibo
n=int(input("Enter the limit:"))
a=0
b=1
print(a)
print(b)
for i in range(n):
    temp=a
    a=b
    b=temp+b
    print(b)
