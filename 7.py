# print(4 > 3, 5 < 2, sep= "\n") #\n es el salto de linea
#Programa de Verficacion de edades



# edad = int(input("Ingresa tu edad: "))

# if edad >= 18:
#     print("Bienvenido")

# else:
#     print("Denegado")

#Convirtiendo Valores
# cadena = "12345"

# bol = bool(cadena)
# print(type(bol))

#Bucle for con distintos iterables

# persona = {
#     "nombre": "ricardo",
#     "edad": 22,
#     "nacionalidad": "mexicano"
# }

# for clave in persona:
#     print(clave)

# lista = [1,2,3,4,5]

# for i in lista:
#     print(i)




# Ejercicio 1: El mensaje secreto
# Dada la siguiente lista:
# mensaje = ["C", "o", "d", "i", "g", "o", " ", "s", "e", "c", "r", "e", "t", "o"]
# Utilizando slicing y concatenación, crea una nueva lista que contenga solo el mensaje "secreto".

# mensaje = ["C", "o", "d", "i", "g", "o", " ", "s", "e", "c", "r", "e", "t", "o"]
# variable = mensaje[7::]
# primera_parte = mensaje[7:11]
# segunda_parte = mensaje[11:]

# nueva_lista = primera_parte + segunda_parte
# print(nueva_lista)
# print(variable)




# Ejercicio 2: Intercambio de posiciones
# Dada la siguiente lista:
# numeros = [10, 20, 30, 40, 50]
# Intercambia la primera y la última posición utilizando solo asignación por índice.

# numeros = [10, 20, 30, 40, 50]

# variable = numeros[0]

# numeros[0] = numeros[-1]
# numeros[-1] = variable

# print(numeros)




# Ejercicio 3: El sándwich de listas
# Dadas las siguientes listas:
# pan = ["pan arriba"]
# ingredientes = ["jamón", "queso", "tomate"]
# pan_abajo = ["pan abajo"]
# Crea una lista llamada sandwich que contenga el pan de arriba, los ingredientes y el pan de abajo, en ese orden.

# pan = ["pan arriba"]
# ingredientes = ["jamón", "queso", "tomate"]
# pan_abajo = ["pan abajo"]

# sandwich = pan + ingredientes + pan_abajo
# print(sandwich)




# Ejercicio 4: Duplicando la lista
# Dada una lista:
# lista = [1, 2, 3]
# Crea una nueva lista que contenga los elementos de la lista original duplicados.
# Ejemplo: [1, 2, 3] -> [1, 2, 3, 1, 2, 3]

# lista = [1, 2, 3]
# nueva_lista = lista * 2
# print(nueva_lista)




# Ejercicio 5: Extrayendo el centro
# Dada una lista con un número impar de elementos, extrae el elemento que se encuentra en el centro de la lista utilizando slicing.
# Ejemplo: lista = [10, 20, 30, 40, 50] -> El centro es 30

# lista = [10, 20, 30, 40, 50]
# variable = lista[2]
# print(variable)





# Ejercicio 6: Reversa parcial
# Dada una lista, invierte solo la primera mitad de la lista (utilizando slicing y concatenación).
# Ejemplo: lista = [1, 2, 3, 4, 5, 6] -> Resultado: [3, 2, 1, 4, 5, 6]

# lista = [1, 2, 3, 4, 5, 6]

# mitad = len(lista) // 2
# primera_mitad = lista[:mitad][::-1]
# segunda_mitad = lista[mitad:]

# variable = primera_mitad + segunda_mitad
# print(variable)


#Imprime todos los números del 1 al 10 usando un for.

numeros = 10

for numero in range(1, numeros + 1): #Empieza en el 1 y termina en el 10 
    print(numero)










