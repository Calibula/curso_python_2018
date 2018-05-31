import random

lista = ["piedra", 'papel', 'tijera']

cont_jug = 0
cont_maq = 0
'''
while (cont_jug < 3) and (cont_maq < 3):
    maq = random.choice(lista)
    jug = lista[int(input("ingrese opcion 0-Piedra , 1-Papel, 2-Tijera"))]
    print("jugador", jug, "PC", maq)
    # COMPARAR
    if(jug == "piedra") and (maq == "tijera"):
        cont_jug += 1
    if(jug == "papel") and (maq == "piedra"):
        cont_jug += 1
    if(jug == "tijera") and (maq == "papel"):
        cont_jug += 1
    if(maq == "piedra") and (jug == "tijera"):
        cont_maq += 1
    if(maq == "papel") and (jug == "piedra"):
        cont_maq += 1
    if(maq == "tijera") and (jug == "papel"):
        cont_maq += 1

if cont_jug == 3:
    print("gano jugador")
else:
    print("gano maquina")
'''

'''
numero = int(input('ingrese un numero'))
while (numero != 0):
    lista.append(numero)
    numero = int(input('ingrese un numero'))
'''
# print(lista.count(2))

# print(lista)
# print(lista.pop(0))
# print(lista.remove(0))
# lista.sort(reverse=True)
# lista.reverse()
# print(lista)
# print(len(lista))

'''
for i in range(1, 6):
    print(random.choice(lista))


for elemento in lista:
    print(elemento)
'''

# DICCIONARIO

dic = {'a': "palabras con a", 'b': "palabras con b", 12: 123}

# print(dic.get('c'))
# print('a' in dic)

dic['c'] = [1, 2, 3]
dic['d'] = {}
dic['c'].append(99)


claves = dic.keys()
claves.sort()

'''
for elemento in claves:
    print(dic[elemento])
'''

# print(dic.keys())
# print(dic.values())

tupla = (1, 2, 3)
print(tupla[0])


conjunto = set(lista)
conjunto.add("valor")

for elemento in conjunto:
    print(elemento)


#FUNCIONES
