def lcm(x, y):
  larger = max(x, y)
  while True:
    if larger % x == 0 and larger % y == 0:
      return larger
    larger += 1

num1 = 12
num2 = 18
result = lcm(num1, num2)
print(f"The LCM of {num1} and {num2} is {result}")


import numpy as np
