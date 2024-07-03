import time
import os
import csv


precio_cilindro_5 = 12500
precio_cilindro_15 = 25500

cilindros = ("5 Kilos","15 Kilos")
comunas = ("Santiago","Colina","Pirque")

pedidos = []

def menu_opciones(p_opcs):
    while True:
        print('\tMenu Gasexplosive\n\t1. Registrar pedido\n\t2. Listar todos los pedidos\n\t3. Buscar pedido por RUT\n\t4. Imprimir hoja ruta\n\t5. Salir\n')
        try:
            opc = int(input('Ingrese una opcion: '))
            if opc in p_opcs:
                return opc
            else:
                print('ERROR! debes ingresar una opcion valida, opciones validas(1,2,3,4,5)!')
            limpiar_esperar_screen()
        except:
            print('ERROR! debe ingresar un numero entero!')


def registrar_pedido():
    print('Registrar pedido!')
    limpiar_esperar_screen()

    while True:
        try:
            rut = int(input('Ingrese su rut (sin puntos ni guion): '))
            if len(str(rut.strip())) >= 7 and len(str(rut.strip())) <= 8:
                print('Rut ingresado correctamente!')
                limpiar_esperar_screen()
                break
            else:
                print('ERROR! el rut ingresado debe contener al menos 7 digitos y no sobrepasar los 8 digitos!')
            limpiar_esperar_screen()
        except:
            print('ERROR! debe ingresar numeros enteros!')

    while True:
        nombre = str(input('Ingrese el nombre: '))
        if len(nombre.strip()) >= 3 and nombre.isalpha():
            print('Nombre ingresado correctamente!')
            limpiar_esperar_screen()
            break
        else:
            print('ERROR! debe ingresar un nombre que contenga al menos 3 letras!')
        limpiar_esperar_screen()

    while True:
        direccion = str(input('Ingrese la direccion: '))
        if len(direccion.strip()) >= 6:
            print('Direccion ingresada correctamente!')
            limpiar_esperar_screen()
            break
        else:
            print('ERROR! la direccion debe contener al menos 6 caracteres!')
        limpiar_esperar_screen()

    while True:
        try:
            comuna_tipo = int(input('Ingrese una comuna (1: Santiago 2: Colina 3: Pirque): '))
            if comuna_tipo in (1,2,3):
                print('Comuna ingresada correctamente!')
                limpiar_esperar_screen()
                break
            else:
                print("ERROR! debe ingresar una comuna valida, opciones de comunas validas(1,2,3)!")
            limpiar_esperar_screen()
        except:
            print('ERROR! debe ingresar un numero entero!')       


    while True:
        try:
            tipo_cilindro = int(input('Ingrese el tipo de cilindro que desea llevar (1:5 kilos 2:15 kilos): '))
            if tipo_cilindro in (1,2):
                print('tipo de cilindro ingresado correctamente!')
                limpiar_esperar_screen()
                break
            else:
                print('ERROR! debe ingresar un tipo de cilindro valido, tipo cilindro valido (1,2)!')
            limpiar_esperar_screen()
        except:
            print('ERROR! debe ingresar un numero entero!')

    cont_cilindro5 = 0
    if tipo_cilindro == 1:
        cont


    pedido = [rut,nombre,direccion,comunas[comuna_tipo-1]]


def


def listar_todos_pedidos():
    print('Listar todoos los pedidos!')
    limpiar_esperar_screen()

def buscar_pedido_rut():
    print('Listar todos los pedidos!')
    limpiar_esperar_screen()

def imprimir_ruta_csv():
    print('Imprimir hoja de ruta!')
    limpiar_esperar_screen()



def salir():
    for x in range(1,4):
        print('Saliendo de gas explosive',("."*x))
        limpiar_esperar_screen()


def limpiar_esperar_screen():
    time.sleep(1)
    os.system('cls')
    