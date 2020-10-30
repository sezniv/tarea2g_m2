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
print("Esta es la lista original random " + str(lista))

# aca estoy sumando cada numero que contiene cada un elemento dentro de la lista

cont1 = 0
for elemento in lista: 
    cont2 = float(elemento)
    cont3 = cont1 + cont2
    cont1 = cont3
resultado = cont1 / 5
promedio = "{0:.3f}".format(resultado)
print("el promedio de los valores dentro de la lista random es de: " + str(promedio))


maximo = max(lista)
for elemento in lista:
    resultado1 = float(elemento) - float(promedio)
    n_lista = resultado1 / float(maximo)
    var_x = 0
    contenedor = n_lista
    var_x += contenedor
print("esta el la suma total de cada elemento de la lista modificada: ")
print(var_x)