import math

def triangulo(medida1, medida2):
	area = (medida1 * medida2) / 2
	return area

def rectangulo(medida1, medida2):
        area = medida1 * medida2
        return area

def circulo(medida1):
        area = math.pi * (medida1**2)
        return area
