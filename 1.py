#Ejercicios
# from os import system

# diccionario = {
#     "nombre": "ricardo",
#     "edad": 22,
#     "nacionalidad": "mexicano",
#     "auto": "mercedes"
# }


# for claves in diccionario.items():
#     print(claves)


# cadena_entero = int("12345")
# cadena_decimal = float("12345")
# decimal_float = float(int("12345"))


# print(type(cadena_entero))
# print(type(cadena_decimal))
# print(type(decimal_float))


# resultado = round(3.1416) // 2
# print(resultado)

#Ejemplo con slicing listas

# mensaje = ["C", "o", "d", "i", "g", "o", " ", "s", "e", "c", "r", "e", "t", "o"]
# variable = mensaje[7:]
# print(variable)

# mensaje = ["C", "o", "d", "i", "g", "o", " ", "s", "e", "c", "r", "e", "t", "o"]
# primera_parte = mensaje[0:6]
# segunda_parte = mensaje[7:]
# concatenacion = primera_parte + segunda_parte

# print(concatenacion.count)

# for valores in mensaje:
#     print(valores, end="\n")


# Intercambia la primera y la última posición utilizando solo asignación por índice.
# numeros = [10, 20, 30, 40, 50]

# valor1 = numeros[0]
# numeros[0] = numeros[4]
# numeros[4] = valor1
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


# lista_original = [1, 2, 3]
# nueva_lista = lista_original[::]
# result = nueva_lista + lista_original
# print(result)


# Ejercicio 5: Extrayendo el centro
# Dada una lista con un número impar de elementos, extrae el elemento que se encuentra en el centro de la lista utilizando slicing.
# Ejemplo: lista = [10, 20, 30, 40, 50] -> El centro es 30

# lista = [10, 20, 30, 40, 50] 
# centro = lista[2]
# print(centro)

# Ejercicio 6: Reversa parcial
# Dada una lista, invierte solo la primera mitad de la lista (utilizando slicing y concatenación).
# Ejemplo: lista = [1, 2, 3, 4, 5, 6] -> Resultado: [3, 2, 1, 4, 5, 6]

# lista = [1, 2, 3, 4, 5, 6]
# primera_parte = lista[3:]     # [4, 5, 6]
# segunda_parte = lista[:3]     # [1, 2, 3]

# segunda_parte = segunda_parte[::-1]

# print(segunda_parte + primera_parte)


# lista = [1,2,3,4,5]
# lista.extend(["🥰", "🇲🇽"])
# lista.remove("🇲🇽")
# lista.pop(1) #Elimina desde el indice 1 que es el valor de 2
# del lista[-3]
# lista.clear()
# print(lista)

# lista = [1,2,3,4,5]
# print("✌️" in lista)


# lista = [1,2,3,4,5]
# del lista[1:3] #no incluye el indice 3 
# print(lista)


#ordena la lista de forma ascendente
#Modificando directamente desde la lista
# lista = [12,234,23,6,47,538,3]
# lista.sort()
# print(lista)


#Otro ejemplo pero creando una lista nueva
#Dejando a la lista original intacta

# lista = [12,234,23,6,47,538,3]
# lista_ordenada = sorted(lista)
# print(lista_ordenada)



#Ordenando una lista ingnoradno MAYUSCULAS

# lista = "fruta", 'MERCADO', 'Familia', 'agosto'
# lista_ordenada = sorted(lista, key=str.lower)
# print(lista_ordenada)



#Poniendo todas las letras MAYUSCULAS a minusculas de una lista

# lista = ["NIKE", "MERCEDES", "TEQUILA"]
# lista_minusculas = [palabra.lower() for palabra in lista]
# print(lista_minusculas)



# lista = [1,2,3,4,5]
# lista2 = [100,235,437,7438]
# lista3 = [48,35,7,8]
# lista.insert(0, "ricki")
# lista.append(22)
# lista.reverse()
# lista.extend([6, 7])
# lista.append(lista2)

# print(len(lista))
# print(lista.count(2))
# print(2 in lista)


# Ejercicio 1: Añadir y modificar elementos
# Crea una lista con los números del 1 al 5.
# Añade el número 6 al final usando append().
# Inserta el número 10 en la posición 2 usando insert().
# Modifica el primer elemento de la lista para que sea 0.

# lista = [1,2,3,4,5]
# lista.append(6)
# lista.insert(2, 10)
# lista[0] = 0
# print(lista)


# Ejercicio 2: Combinar y limpiar listas
# Crea dos listas:
# lista_a = [1, 2, 3]
# lista_b = [4, 5, 6, 1, 2]
# Extiende lista_a con lista_b usando extend().
# Elimina la primera aparición del número 1 en lista_a usando remove().
# Elimina el elemento en el índice 3 de lista_a usando pop(). Imprime el elemento eliminado.
# Limpia completamente lista_b usando clear().

# lista_a = [1,2,3]
# lista_b = [4,5,6,1,2]

# lista_a.extend(lista_b)
# lista_a.remove(1)
# lista_a.pop(3)
# lista_b.clear
# print(lista_a)



# Ejercicio 3: Slicing y eliminación con del
# Crea una lista con los números del 1 al 10.
# Utiliza slicing y del para eliminar los elementos desde el índice 2 hasta el 5 (sin incluir el 5).
# Imprime la lista resultante.

# lista = [1,2,3,4,5,6,7,8,9,10]
# del lista[2:5]
# print(lista)




# Ejercicio 4: Ordenar y contar
# Crea una lista con los siguientes números: [5, 2, 8, 1, 9, 4, 2].
# Ordena la lista de forma ascendente usando sort().
# Cuenta cuántas veces aparece el número 2 en la lista usando count().
# Comprueba si el número 7 está en la lista usando in.

# lista = [5, 2, 8, 1, 9, 4, 2]
# lista.sort()
# print(lista.count(2))
# print(7 in lista)









# Ejercicio 5: Copia vs. Referencia
# Crea una lista llamada original con los números [1, 2, 3].
# Crea una copia de la lista original llamada copia_1 usando slicing.
# Crea otra copia llamada copia_2 usando copy().
# Crea una referencia a la lista original llamada referencia.
# Modifica el primer elemento de la lista referencia a 10.
# Imprime las cuatro listas (original, copia_1, copia_2, referencia) y observa los cambios.

# original = [1,2,3]
# copia_1 = original[::]
# copia_2 = original.copy()
# referencia = original
# referencia[0] = 10

# print(original)
# print(copia_1)
# print(copia_2)
# print(referencia)



# Ejercicio 6: Ordenar strings sin diferenciar mayúsculas y minúsculas.
# Crea una lista con las siguientes cadenas: ["Manzana", "pera", "BANANA", "naranja"].
# Ordena la lista sin diferenciar entre mayúsculas y minúsculas.


# lista = ["Manzana", "pera", "BANANA", "naranja"]

# lista_ordenada = sorted(lista, key=str.lower)
# print(lista_ordenada)


#Bucle While
# edad = 0

# while edad <= 5:
#     print(edad)
#     edad += 1


# nombre = "ricardo"
# edad = 22

# print(f"hola {nombre} tienes {edad} años")
# for letra in nombre:
#     print(letra)


# lista = [1,2,3,4,5]
# for palabra in lista:
#     print(lista)


# def saludar(edad, edad_acompañante):
#     if edad >= 18:
#         print("Bienvenido")

#     elif edad < 18 and edad_acompañante >= 18:
#         print("Puedes ingresar con un adulto")

#     else:
#         print("no puede ingresar")

# saludar(20, 0)
# saludar(18, 14)
# saludar(22, 54)
# saludar(13, 3)


# Crea una función llamada saludar que reciba un nombre y muestre:

# def saludar(nombre):
#     print(f"Hola {nombre}")

# saludar("ricardo")


# Crea una función sumar(a, b) que regrese la suma de dos números.

# def sumar(a, b):
#     return a + b

# print(sumar(10, 20))


# Crea una función es_par(numero) que regrese True si es par y False si es impar.

# def es_par(numero):
#     if numero % 2 == 0:
#         return True
#     else:
#         return False

# print(es_par(2)) 

   
#Crea una función area_rectangulo(base, altura) que regrese el área.

# def area_rectangulo(base, altura):
#     return base * altura


# print(area_rectangulo(10, 5))


# Crea una función mayor(a, b) que regrese el número mayor.
# Si son iguales, que regrese "Son iguales".

# def mayor(a, b):
#     if a > b:
#         print("A es mayor")

#     elif b > a:
#         print("B es mayor")

#     else:
#         print("Son iguales")

# mayor(10, 10)


# Crea una función contar_letras(palabra) que regrese cuántas letras tiene la palabra.

# def contar_letras(palabra):
#     return len(palabra)

# print(contar_letras("hola"))


# Crea una función tabla(numero) que imprima la tabla del 1 al 10 de ese número.

# def tabla(numero):
#     for i in range(1, 11):
#         print(f"{numero} x {i} = {numero * i}")

# tabla(2)

# Crea una función promedio(lista) que reciba una lista de números y regrese el promedio.
# def promedio(lista):
#     return sum(lista) / len(lista)

# # ejemplo
# print(promedio([10, 8, 9, 7]))

# Crea una función contar_vocales(texto) que regrese cuántas vocales hay en el texto.

# def contar_vocales(texto):
#     vocales = "aeiouAEIOU"
#     contador = 0

#     for letra in texto:
#         if letra in vocales:
#             contador += 1

#     return contador

# print(contar_vocales("Hola Mundo")) 


cadena = 1
cadena = str("hola")
print(type(cadena))

