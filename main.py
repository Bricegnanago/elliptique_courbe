# Algorithme
# de x3+ax+b
class Point:

    def __init__(self, abs=4, ord=9):
        self.abs = abs
        self.ord = ord

    def setpoint(self, newabs, neword):
        self.abs = newabs
        self.ord = neword


# print(point.ord)


def elliptiquecourbe(a, b, point):
    return point.ord * point.ord - (point.abs ^ 3 + a * point.abs + b)


while 1:

    point = Point()
    point.abs = int(input("Veuillez saisir les cordonnées d'un point : "))
    point.ord = int(input("Veuillez saisir les cordonnées d'un point : "))
    print("***maintenant saisir les coefficient***")
    a = int(input("a = "))
    b = int(input("b = "))

    result = elliptiquecourbe(a, b, point)

    if result == 0:
        print("result " + str(result) + " : ce Point appartient à la courbe")
    else:
        print("result " + str(result) + " : Ce Point n'appartient à la courbe")

