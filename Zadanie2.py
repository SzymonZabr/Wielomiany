# Zadanie 2

def horner(n, x):
    wynik = 1
    for i in range(n):
        wynik = wynik * x + 1
    return wynik

print(horner(5, 2))
