lenguajes = ("Python", "Java", "C", "C++")
print(lenguajes[-3])

tuple1 = (1, 2, 3, 4, 5)
tuple2 = (6, 7, 8, 9, 10)
tup = tuple1 + tuple2
print(tup)

tup = tuple1 * 3
print((tup))

tup = 7 in tuple1
print(tup)

tup = tuple1.index(5)
print(tup)

tuple3 = (65, 67, 5, 67, 34, 76, 67, 231, 98, 67)
tup = tuple3.count(67)
print(tup)

tup = tuple3[4]
print(tup)

# CONVERSION DE TUPLA A LISTA
tuple1 = (1, 2, 3, 4, 5)
print(tuple1)
lista1 = list(tuple1)
print(lista1)

# CONVERSION DE LISTA A TUPLA
lista2 = [6, 7, 8, 9, 10]
print(lista2)
tupla2 = tuple(lista2)
print(tupla2)

# EMPAQUETADO
x = 10
y = 30
punto = x, y
print(punto)

# DESEMPAQUETADO
fecha = (25, "diciembre", 2022)
print(fecha)
dd, mm, aa = fecha
print("Día", dd)
print("Mes", mm)
print("Año", aa)

diccionario = {"nombre" : "Carlos", "edad" : 22, "cursos" : ["Python", "Django", "JavaScript"]}
print(diccionario)

print(diccionario["nombre"])
print(diccionario["edad"])
print(diccionario["cursos"])

print(diccionario["cursos"][0])
print(diccionario["cursos"][1])
print(diccionario["cursos"][2])

for key in diccionario:
    print(key, ":", diccionario[key])

diccionario1 = {"Juan" : "15 años", "Pedro" : "23 años", "Rosa" : "19 años"}
print(diccionario1.get("Rosa"))
print(diccionario1.pop("Pedro"))
print(diccionario1)

diccionario1.update({"Maria" : "50 años"})
diccionario1.update({"Rosa" : "60 años"})
print(diccionario1)

print("Juan" in diccionario1)
print("50 años" in diccionario1)

print("60 años" in diccionario1.values())

del diccionario1["Rosa"]
print(diccionario1)