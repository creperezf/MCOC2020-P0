# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

nombre = "MCOC"
dia = 3

print("Forma 1")
print("hola Jose es el 3 de Agosto")


print("Forma 2")
print("hola " + nombre + " es el " + str(dia) + " de Agosto")

print("Forma 3")
print("hola {nombre} es el {dia} de Agosto".format(dia=dia, nombre=nombre))

print("Forma 4")
print(f"hola {nombre} es el {dia} de Agosto")