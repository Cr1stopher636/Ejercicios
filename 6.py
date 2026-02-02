# print("Rick"," es el mejor", "programador", sep = "--")
# print("Rick tiene su mercedes", "benz", sep="-")

# Ejercicio 1: Determinar el mayor de dos números
# Pide al usuario que introduzca dos números y muestra un mensaje
# indicando cuál es mayor o si son iguales

# num1 = int(input("ingresa el primer numero: "))
# num2 = int(input("ingresa el segundo numero: "))

# if num1 > num2:
#     print(f"El numero {num1} es mayor")

# elif num2 > num1:
#     print(f"El numero {num2} es mayor")

# else:
#     print("Son iguales")





# Ejercicio 2: Calculadora simple
# Pide al usuario dos números y una operación (+, -, *, /)
# Realiza la operación y muestra el resultado (maneja la división entre zero)

# num1 = int(input("Ingrea el primer numero: "))
# num2 = int(input("Ingrea el segundo numero: "))
# operacion = input("Operacion: (+,-,*,/)")



# if operacion == "+":
#     resultado = num1 + num2
#     print("Resultado: ", resultado)

# elif operacion == "-":
#     resultado = num1 - num2
#     print("Resultado: ", resultado)

# elif operacion == "*":
#     resultado = num1 * num2
#     print("Resultado: ", resultado)


# elif operacion == "/":
#     resultado = num1 / num2
#     print("Resultado: ", resultado)




# Ejercicio 3: Año bisiesto
# Pide al usuario que introduzca un año y determina si es bisiesto.
# Un año es bisiesto si es divisible por 4, excepto si es divisible por 100 pero no por 400.

# año = int(input("introduce un año: "))


# if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
#     print("Año Bisiesto")

# else:
#     print("No es Bisiesto")





# Ejercicio 4: Categorizar edades
# Pide al usuario que introduzca una edad y la clasifique en:
# - Bebé (0-2 años)
# - Niño (3-12 años)
# - Adolescente (13-17 años)
# - Adulto (18-64 años)
# - Adulto mayor (65 años o más)

# edad = int(input("Introduce una edad: "))

# if edad >= 65:
#     print("Adulto mayor")

# elif edad >= 18:
#     print("Adulto")

# elif edad >= 13:
#     print("Adolescente")

# elif edad >= 3:
#     print("Niño")

# elif edad >= 0:
#     print("Bebe")


