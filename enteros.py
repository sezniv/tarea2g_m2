import random

caracteres = '0123456789'

# calcula el promedio de la lista 
def promedio_lista(lista2):
    sum=0
    m = len(lista2)
    for i in range(0,m):
        sum = sum + lista2[i]
    return sum/len(lista2)

   
# script enteros.py lista contiene enteros de largo 
# aleatorio entre 1 y 20 

lista = []
for n in range(0,5):    
    string_aleatorio = ''    
    largo = random.randint(1, 20)    
    for i in range(0, largo):        
        string_aleatorio += random.choice(caracteres)    
    lista.append(string_aleatorio)


# transforma lista string en lista enteros y calcula el promedio
lista2 = [int(x) for x in lista]
print('La lista generada es: ')
print(lista2)
print('y su promedio viene dado por')
print(promedio_lista(lista2))



# Se genera la acutualizacion
p = promedio_lista(lista2)
lista3 = []
lista3 = [lista2[0] - p, lista2[1] - p, lista2[2] - p, 
          lista2[3] - p, lista2[4] - p]
print('La actualizacion de la lista es: ')
print(lista3)


input()


