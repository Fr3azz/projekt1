lista = []
i = 10

while i != 0:
    wartosc = input("Wprowadź liczbę: ")
    liczba = float(wartosc)
    if liczba % 2 == 0:
        lista.append(liczba)
    i -= 1

