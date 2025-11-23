# Zadanie 5


def dzielniki(n):
    n = abs(n)
    wynik = []
    for i in range(1, n + 1):
        if n % i == 0:
            wynik.append(i)
            wynik.append(-i)
    return wynik

def pierwiastki_wymierne(a):
    a0 = a[0]
    an = a[-1]

    p = dzielniki(a0)
    q = dzielniki(an)

    mozliwe = set()
    for licznik in p:
        for mianownik in q:
            mozliwe.add(licznik / mianownik)

    pierwiastki = []
    for r in mozliwe:
        wartosc = 0
        for i in range(len(a)):
            wartosc += a[i] * (r ** i)
        if abs(wartosc) < 1e-9:
            pierwiastki.append(r)

    return sorted(pierwiastki)

a = [6, -11, -3, 2]
print(pierwiastki_wymierne(a))
