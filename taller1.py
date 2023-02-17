# Construya un algoritmo en Python, que permita ingresar la
# información de un empleado e imprima el nombre, los
# apellidos y la antigüedad. Los datos que se deben solicitar
# son los siguientes:
# *Nombre * Teléfono *Año de ingreso a la empresa
# *Apellidos *Edad.

nombre = input("Digite su nombre ")
apellido = input("Digite su apellido ")
telefono = int(input("Digite su numero de telefono "))
edad = int(input("Digite su edad "))
año_ingreso = int(input("Digite el año en que ingreso a la empresa "))
año_actual = 2023

print(f"{nombre.upper()} {apellido.upper()} tienes una antiguedad en la empresa de {año_ingreso - año_actual} años")

