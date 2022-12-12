import math
def triangle60(x):
    pole = (x**2)*(math.sqrt(3))
    return pole

a = input("Podaj bok trojkata rownobocznego, a ja policze polę. ")
a = float(a)
print(triangle60(a))
