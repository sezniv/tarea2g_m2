import random

caracteres = '0123456789'

   

lista = []
for n in range(0,5):    
    string_aleatorio = ''    
    largo = random.randint(10, 50)    
    for i in range(0, largo):        
        string_aleatorio += random.choice(caracteres)    
        flotante = "{0:.3f}".format(float(string_aleatorio) / 3) 
    lista.append(flotante)
print(lista)

# aca estoy sumando cada numero que contiene cada un elemento dentro de la lista

cont1 = 0
for elemento in lista: 
    cont2 = float(elemento)
    cont3 = cont1 + cont2
    cont1 = cont3
resultado = cont1 / 5
resultadox = "{0:.3f}".format(resultado)
print("el promedio de los valores dentro de la lista es de: " + str(resultadox))

for elemento in lista:
    resultado1 = float(elemento) - resultadox
for elemento in lista:
    ele1 = float(elemento)