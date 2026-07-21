#Using math module also provide this option
#Logical program
def find_gcd_loop(a, b):
    gcd = 1
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            gcd = i
    return gcd
a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
res=find_gcd_loop(a,b)
print(res)

