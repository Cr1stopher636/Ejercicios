# Ejercicio 1: Cuenta atrás
# Imprime los números del 10 al 1 usando un bucle while.

# contador = 10
# while contador >= 1:
#     print(contador)
#     contador -= 1


# Ejercicio 2: Suma de números pares (while)
# Calcula la suma de los números pares entre 1 y 20 (inclusive) usando un bucle while.
# print("\nEjercicio 2:")

# contador = 20
# while contador >= 1:
#     print(contador)
#     contador -= 1




# Ejercicio 3: Factorial de un número
# Pide al usuario que introduzca un número entero positivo.
# Calcula su factorial usando un bucle while.
# El factorial de un número entero positivo es el producto de todos los números del 1 al ese número. Por ejemplo, el factorial de 5
# 5! = 5 x 4 x 3 x 2 x 1 = 120.
# print("\nEjercicio 3:")

# numero = int(input("Ingresa un numero entero positivo: "))

# factorial = 1
# contador = numero

# while contador > 0:
#     factorial *= contador
#     contador -= 1

# print(f"El factorial de {numero} es {factorial}")



# Ejercicio 4: Validación de contraseña
# Pide al usuario que introduzca una contraseña.
# La contraseña debe tener al menos 8 caracteres.
# Usa un bucle while para seguir pidiendo la contraseña hasta que cumpla con los requisitos.
# Si la contraseña es válida, imprime "Contraseña válida".
# print("\nEjercicio 4:")

# contraseña = input("Introduce la contraseña: ")
# while contraseña != "12345678":
#     print("Acceso denegado")
#     contraseña = input("Ingresa de nuevo la contraseña: ")
 
# print("Contraseña valida")





# Ejercicio 5: Tabla de multiplicar
# Pide al usuario que introduzca un número.
# Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle while.
# print("\nEjercicio 5:")

num1 = int(input("Ingresa el primer numero: "))
contador = 1

while contador <= 10:
    print(num1, "x", contador, "=", num1 * contador)
    contador += 1
    

# Ejercicio 6: Números primos hasta N
# Pide al usuario que introduzca un número entero positivo N.
# Imprime todos los números primos menores o iguales que N usando un bucle while.
# print("\nEjercicio 6:")