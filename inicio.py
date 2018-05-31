'''
print('Hola Mundo')
valor = int(input('ingrese un numero '))
print('la suma es', valor + 10)
'''

'''
int()
float()
str()
bool()
complex()
'''

# tipos de datos
# entero
numero1 = 45
numero2 = 50
reales = 45.0
complejo = 45 + 2j
cadena = "hola"
boolean = True
nada = None

# operadores aritmeticos + - * / // % **
"""
print(2 ** 5)
print(5 / 2)
print(5 // 2)
print(5 % 2)
"""
# estructuras de control
# condicionales

# < > >= <= == !=
# and or ^
opcion = None

if(opcion == 1):
    print('mayor que 45')
elif(opcion == 2):
    print("es menor")
elif(opcion == 3):
    print("es menor")
else:
    print('son igual')

# colecciones lista diccionario conjunto ...

lista_numeros = [99, True, 22.5, "hola", 45, 78]

# print(lista_numeros[2])

# Ciclos
numero = 10
# mientras
while(numero < 10):
    print('numero', numero)
    numero += 1
# para
for numero in lista_numeros:
    print(numero)
