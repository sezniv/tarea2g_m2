import random

caracteres = '0123456789'

   

lista = []
for n in range(0,5):    
    string_aleatorio = ''    
    largo = random.randint(1, 20)    
    for i in range(0, largo):        
        string_aleatorio += random.choice(caracteres)    
    lista.append(string_aleatorio)
print(lista)

# aca estoy sumando cada numero que contiene cada un elemento dentro de la lista

cont1 = 0
for elemento in lista: 
    cont2 = int(elemento)
    cont3 = cont1 + cont2
    cont1 = cont3
resultado = cont1 // 5
print("el promedio de los valores dentro de la lista es de: " + str(resultado))