import math
a = input("Wprowadź liczbę którą chcesz pierwiastkować:")
b = float(a)
if b>0:
    print("Wynik: %f" % math.sqrt(b))
else:
    print ("Podałeś liczbę ujemną")