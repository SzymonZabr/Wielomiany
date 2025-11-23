# zAdanie 6

import math

a = float(input("Podaj a: "))
b = float(input("Podaj b: "))
c = float(input("Podaj c: "))
d = float(input("Podaj d: "))

A = 3 * a
B = 2 * b
C = c

delta = B * B - 4 * A * C

if delta < 0:
    print("Brak ekstremów")
else:
    x1 = (-B + math.sqrt(delta)) / (2 * A)
    x2 = (-B - math.sqrt(delta)) / (2 * A)

    w1 = a*x1**3 + b*x1**2 + c*x1 + d
    w2 = a*x2**3 + b*x2**2 + c*x2 + d

    if x1 < x2:
        print("Maksimum w:", x1, "wartość:", w1)
        print("Minimum w:", x2, "wartość:", w2)
    else:
        print("Maksimum w:", x2, "wartość:", w2)
        print("Minimum w:", x1, "wartość:", w1)

