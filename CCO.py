#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Calculador de Costes de Operaciones de Select en MySQL

#Imports
import math
import os
import sys

#Constantes
global lista_tabla
lista_tabla=[]

#Objetos
class tabla:
    def __init__(self, nombre, size, cost):
        self.nombre=nombre
        self.size=size
        self.cost=cost

#Funciones
def crear_tabla():
    nombre=input("Nombre: ")
    tamaño=int(input("Tamaño: "))
    coste=int(input("Coste: "))
    lista_tabla.append(tabla(nombre, tamaño, coste))

def ver_tablas():
    i=0
    print(f"[{i}] \t\tNombre\t\tTamaño\t\tCoste")
    for x in lista_tabla:
        i=i+1
        print(f"[{i}] \t\t{x.nombre}\t\t{x.size}\t\t{x.cost}")
    print()

def fuerza_bruta():
    #Muestra la lista de tablas
    print("Lista de Tablas")
    ver_tablas()
    #Elige la primera tabla
    o1=int(input("Elige la primera tabla a calcular: "))
    t1=lista_tabla[o1-1]
    #Elige la segunda tabla
    o2=int(input("Elige la segunda tabla a calcular: "))
    t2=lista_tabla[o2-1]
    #Calcular coste
    coste=t1.size*t2.size+t1.cost+t2.cost
    print(f"El coste por fuerza bruta es de {coste}")
    return coste

def busqueda_indices():
    #Muestra la lista de tablas
    print("Lista de Tablas")
    ver_tablas()
    #Elige la primera tabla
    o1=int(input("Elige la tabla sin indices a calcular: "))
    t1=lista_tabla[o1-1]
    #Elige la segunda tabla
    o2=int(input("Elige la tabla con indices a calcular: "))
    t2=lista_tabla[o2-1]
    #Elige el multiplicador
    t=int(input("Elige el factor de multiplicacion: "))
    #Calcular coste
    coste=(t1.size*t*math.ceil(math.log2(t2.size)))+t1.cost+t2.cost
    print(f"El coste por busqueda por indices es de {coste}")
    return coste


def busqueda_mezcla():
    #Muestra la lista de tablas
    print("Lista de Tablas")
    ver_tablas()
    #Elige la primera tabla
    o1=int(input("Elige la tabla a ordenar a calcular: "))
    t1=lista_tabla[o1-1]
    #Elige la segunda tabla
    o2=int(input("Elige la tabla no ordenada a calcular: "))
    t2=lista_tabla[o2-1]
    #Elige el multiplicador
    t=int(input("Elige el factor de multiplicacion: "))
    #Calcular coste
    coste=(t1.size*t*math.ceil(math.log2(t1.size)))+t1.size+t2.size+t1.cost+t2.cost
    print(f"El coste por busqueda por mezcla es de {coste}")
    return coste    

def borrar_tablas():
    global lista_tabla
    lista_tabla=[]

def exit():
    sys.exit()

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def imprimir_titulo():
    archivo=open("title","r",encoding='utf-8')
    title=archivo.read()
    print(title)
    archivo.close()

#Programa principal
def main():
    while True:
        print(">>> Menu principal")
        print("[1] Crear una tabla:")
        print("[2] Ver lista de tablas:")
        print("[3] Calcular por fuerza bruta:")
        print("[4] Calcular por indice más busqueda por indices:")
        print("[5] Calcular por ordenacion más busqueda por mezcla:")
        print("[9] Borrar tablas:")
        print("[0] Salir:")
        opt=int(input("\nOpcion: "))
        print()
        switch = {
            1:crear_tabla,
            2:ver_tablas,
            3:fuerza_bruta,
            4:busqueda_indices,
            5:busqueda_mezcla,
            9:borrar_tablas,
            0:exit
        }
        switch.get(opt, exit)()
        os.system('pause')
        limpiar_pantalla()
    
# Comprobar si se esta ejecutando como script principal
if __name__ == '__main__':
    limpiar_pantalla()
    imprimir_titulo()
    main()
