
from math import sin, pi
# lady+(Ba)*2 questions
sum = 0
for i in range(4, 69):
    sum += i** (1/2) + i ** (1/3)
radians = sum* pi
degrees = sin(radians)
print(degrees)