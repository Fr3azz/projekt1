import sys

sys.stdout.write("Wprowadź liczbę a: ")
a = float(sys.stdin.readline())

sys.stdout.write("Wprowadź liczbę b: ")
b = float(sys.stdin.readline())
sys.stdout.write("Wprowadź liczbę c: ")
c = float(sys.stdin.readline())
sys.stdout.write("a^b + c = %.4f" % ((a ** b) + c))