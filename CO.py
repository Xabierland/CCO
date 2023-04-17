#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Calculador de operaciones de bases de datos

#Imports
import math
import sys

#Constantes
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
    for x in lista_tabla:
        i=i+1
        print(f"[{i}] {x.nombre}")

def fuerza_bruta():
    return null

def busqueda_indices():
    log=int(math.log(t2.size)/math.log(2))
    return t1.cost + t1.size*t*log

def exit():
    sys.exit()

#Programa principal
def main():
    while True:
        print("===================================")
        print("Menu principal")
        print("\t[1] Crear una tabla:")
        print("\t[2] Ver lista de tablas")
        print("\t[3] Calcular fuerza bruta")
        print("\t[0] Salir")
        opt=int(input("Opcion: "))
        print("===================================")
        switch = {
            1:crear_tabla,
            2:ver_tablas,
            3:fuerza_bruta,
            0:exit
        }
        switch.get(opt, exit)()
    
# Comprobar si se esta ejecutando como script principal
if __name__ == '__main__':
    main()
