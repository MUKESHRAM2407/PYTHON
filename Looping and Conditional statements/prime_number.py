n=int(input("Enter the number:"))
prime=True
for i in range(2,n):
    if n%i==0:
        prime=False
if prime is True:
    print("Given is prime number:")
else:
    print("Not a prime number:")
    
