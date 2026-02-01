#Loops while
#Bucles while
#permite ejecutar un bloque de codigo repetidamente 
# mientras se cumple una condicion

#Bucle con una simple condicion

"""contador = 0
while contador < 5:
    print(contador)
    contador += 1
"""


#Bucle con while True break

"""contador = 0
while contador < 5:
    print("hola")
    contador += 1"""

#Imprime los números del 1 al 10 usando un bucle while.
#💡 Pista: Necesitarás un contador que aumente en cada vuelta.

"""contador = 1
while contador <= 10:
    print(contador)

    contador += 1"""


# Ejercicio 2: Sumar números
# Pide al usuario que ingrese números hasta que ingrese 0.
# Al final, muestra la suma de todos los números ingresados.
# 💡 Pista: input() y convertir a entero con int().

# suma = 0

# while True:
#     num = int(input("Ingresa un numero: "))

#     if num == 0:
#         break

#     suma += num

# print("La suma es: ", suma)


# Haz que el programa pida una contraseña hasta que el usuario escriba "python123".
# Cuando la escriba correctamente, imprime "Acceso concedido".

# contraseña = input("Ingresa la contraseña")
# while contraseña != "python123":
#     print("Contraseña incorrecta")

#     contraseña = input("Intenta de nuevo: ")

# print("Contraseña correcta")


# Ejercicio 4: Número aleatorio
# Usa random.randint(1, 10) para generar un número secreto.
# El usuario debe adivinarlo.
# Si adivina, imprime "¡Correcto!" y termina el bucle.
# Si falla, imprime "Intenta de nuevo" y sigue pidiendo.
# 💡 Pista: necesitas import random.


#Bucle while

# contraseña = input("Ingresa la contraseña: ")

# while contraseña != "python123":
#     print("Contrasela incorrecta")

#     contraseña = input("Intentalo de nuevo: ")

# print("Contraseña Correcta")



# # Inicializa la variable
# y = 4

# # Realiza las siguientes operaciones usando operadores combinados:
# # 1. Multiplica y por 6
# # 2. Divide y entre 3

# print(y)

# y = 4
# y *= 6
# y //= 3
# print(y)



# Pide al usuario números hasta que ingrese 0. Muestra la suma de todos los números.
# Pistas: usa while True, break y un acumulador (suma).

# suma = 0


# while True:
#     numero = int(input("Ingresa un numero (0 para salir): "))
#     if numero == 0:
#         break

#     suma += numero   

# print("La suma de todos los numeros es: ", suma)


#pedirle un numero que tiene que ser positivo

# numero = -1

# while numero < 0:
#     try:
#         numero = int(input("Ingresa un numero positivo: "))

#         if numero < 0:
#             print("El numero tiene que ser positivo: ")

#     except ValueError:
#         print("El valor tiene que ser un numero: ")

# print(f"El numero que ingresaste fue: {numero}")

    
# Ejercicio 1: Cuenta atrás
# Imprime los números del 10 al 1 usando un bucle while.


# numero = 10

# while numero > 0:
#     print(numero)
#     numero -= 1

# print("Se acabo el bucle")



# Ejercicio 2: Suma de números pares (while)
# Calcula la suma de los números pares entre 1 y 20 (inclusive) usando un bucle while.



#Numera del 1 al 10 con while

# numero = 0

# while numero > 10:
#     numero += 1

# print("fin del bucle")

# lista = [1,2,3,4,5]
# variable = lista.copy()

# variable.append("rick")
# print(lista)
# print(variable)

    