# ZADANIE 4

import random

def horner(a, x):
    wynik = a[-1]
    for i in range(len(a)-2, -1, -1):
        wynik = wynik * x + a[i]
    return wynik

n = random.randint(2, 7)
wsp = [random.randint(-10, 10) for _ in range(n+1)]
a = random.randint(-5, 5)

print("Stopień:", n)
print("Współczynniki:", wsp)
print("a =", a)

reszta = horner(wsp, a)
print("Reszta z dzielenia przez (x - a):", reszta)
