#Programa que imprima hola mundo
# print("hola mundo")

#Pide dos numeros al usuario y muestra su suma
# num1 = int(input("Ingresa el primer numero: "))
# num2 = int(input("Ingresa el segundo numero: "))

# result = num1 + num2
# print(result)


#Pide un numero y determina si es PAR o IMPAR
# num = int(input("Ingresa un numero: "))
# if num % 2 == 0:
#     print("Numero PAR")
# else:
#     print("Numero IMPAR")


#Pide la edad al usuario y di si es mayor o menor de edad
# edad = int(input("Ingresa tu edad: "))
# if edad >= 18:
#     print("Mayor de edad")

# else:
#     print("Menor de edad")



#INTERMEDIO -------->

#Muestra la tabla del 1 al 10 de un numero ingresado

# num = int(input("Ingresa un numero: "))

# for i in range(1, 11):
#     print(num, "x", i, "=", num * i)



#Pide una palabra y cuenta cuantas vocales tiene

# palabra = input("Ingresa la palabra: ").lower()

# vocales = "aeiou"
# contador = 0

# for letra in palabra:
#     if letra in vocales:
#         contador += 1

# print(contador)


#Pide 5 numeros, guardalos en una lista y muestra:
#mayor
#menor
#promedio

# num1 = int(input("Ingresa el primer numero: "))
# num2 = int(input("Ingresa el segundo numero: "))
# num3 = int(input("Ingresa el tercer numero: "))
# num4 = int(input("Ingresa el cuarto numero: "))
# num5 = int(input("Ingresa el quinto numero: "))

# lista = [num1, num2, num3, num4, num5]

# mayor = max(lista)
# menor = min(lista)
# promedio = sum(lista) / len(lista)


# print("Lista: ", lista)
# print("Mayor: ", mayor)
# print("Menor: ", menor)
# print("Promedio: ", promedio)

#Max devuelve el numero mas grande de una lista
#Min devuelve el numero mas pequeño de una lista
#Sum suma todos los numeros que hay dentro de la lista
#len cuenta cuantos elementos hay dentro de una lista



#Genera un numero aleatorio del 1 al 10 y deja que el usuario lo adivine


# import random #Importamos el modulo random

# #Generamos un numero aleatorio entre el 1 y el 10
# numero_secreto = random.randint(1, 10) #randint genera un numero aleatorio entre el 1 y el 10

# #Pide al usuario que lo adivine 
# adivinanza= int(input("Adivina el numero del 1 al 10: "))

# #Comparamos 
# if adivinanza == numero_secreto:
#     print("Haz adivindado el numero secreto")

# else:
#     print("No haz adivinado el numero")


