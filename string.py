# -*- coding: utf-8 -*-

#### este es el ejemplo que aparece en el ejercicio del nodo
import random
caracteres = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz­_'
lista = []
for n in range(0,100):    
    string_aleatorio = ''    
    largo = random.randint(1, 20)    
    for i in range(0, largo):        
        string_aleatorio += random.choice(caracteres)    
    lista.append(string_aleatorio)
print(lista)

######## desde aca comienza el codigo que realizo el profe en clases


caracteres = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz­_'

def calcula_largo_promedio(lista):
    suma_largos = 0
    for elemento in lista:
        largo = len(elemento)
        suma_largos = suma_largos + largo
    largo_promedio = suma_largos/len(lista)
    return largo_promedio


largo_listas = 5
lista = []
for n in range(0,largo_listas):
    string_aleatorio = ''
    largo = random.randint(1, 20)
    for i in range(0, largo):
        string_aleatorio += random.choice(caracteres)
    lista.append(string_aleatorio)
print("Lista Inicial: \n" , lista)
largo_promedio = calcula_largo_promedio(lista)
print("Largo promedio elemento de lista: ", largo_promedio)


lista2 = []
for n in range(0,largo_listas):
    string_aleatorio = ''
    largo = len(lista[n])
    for i in range(0, largo):
        string_aleatorio += random.choice(caracteres)
    lista2.append(string_aleatorio)
print("Esta es la lista 2: \n", lista2)

largo_promedio2 = calcula_largo_promedio(lista2)
print("Largo promedio elemento de lista2: ", largo_promedio2)
print("\n")

