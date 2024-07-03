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
        print('\tMenu Gas explosive\n\t1. Registrar pedido\n\t2. Listar todos los pedidos\n\t3. Buscar pedido por RUT\n\t4. Imprimir hoja ruta\n\t5. Salir\n')
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
        mensaje = str(input('Desea llevar un gas de 5 kilos, Ingrese ("S"si"N":no): '))
        if mensaje.upper() in ("S","N"):
            if mensaje.upper() == "S":
                while True:
                    try:
                        cant_cilindro_5 = int(input('Ingrese la cantidad de cilindros: '))
                        if cant_cilindro_5 >= 1:
                            print('cantidad ingresada correctamente!')
                            limpiar_esperar_screen()
                            break
                        else:
                            print('ERROR! debe ingresar una cantidad valida, la cantidad debe ser mayor o igual a 1!')
                        limpiar_esperar_screen()
                    except:
                        print('ERROR! debe ingresar un numero entero!')
            else:
                if mensaje.upper() == "N":
                    break
        else:
            print('ERROR! debe ingresa una opcion valida, opciones validas ("S"o "N")')
        limpiar_esperar_screen()
                
    
    while True:
        mensaje = str(input('Desea llevar un gas de 15 kilos, Ingrese ("S"si"N":no): '))
        if mensaje.upper() in ("S","N"):
            if mensaje.upper() == "S":
                while True:
                    try:
                        cant_cilindro_15 = int(input('Ingrese la cantidad de cilindros: '))
                        if cant_cilindro_15 >= 1:
                            print('cantidad ingresada correctamente!')
                            limpiar_esperar_screen()
                            break
                        else:
                            print('ERROR! debe ingresar una cantidad valida, la cantidad debe ser mayor o igual a 1!')
                        limpiar_esperar_screen()
                    except:
                        print('ERROR! debe ingresar un numero entero!')
            else:
                if mensaje.upper() == "N":
                    break
        else:
            print('ERROR! debe ingresa una opcion valida, opciones validas ("S"o "N")')
        limpiar_esperar_screen()
    
    precio_total_ped = (cant_cilindro_5 * precio_cilindro_5 ) + (cant_cilindro_15 * precio_cilindro_15)
                
    pedido = [rut,nombre,direccion,comunas[comuna_tipo-1],cant_cilindro_5,cant_cilindro_15,precio_total_ped]


    pedidos.append(pedido)
    print('PEDIDO REGISTRADO!')
    limpiar_esperar_screen()




def listar_todos_pedidos():
    print('Listar todos los pedidos!')
    limpiar_esperar_screen()

    if len(pedidos) >= 1:
        while True:
            print('\tLista de pedidos\n')
            for p in pedidos:
                print(f"\t RUT:{p[0]}\t Cliente:{p[1]}\t Direccion:{p[2]}\t Comuna:{p[3]}\t Cant.5kg:{p[4]}\t Cant.15kg:{p[5]}\t Total:{p[6]}\n")
            opc_salir = str(input('Deseas salir? Ingrese ("S":SALIR "N":redirigir pedidos): '))
            if opc_salir.upper() in ("S","N"):
                if opc_salir.upper() == "S":
                    print('Saliendo.')
                    limpiar_esperar_screen()
                    break
                else:
                    print('Redirigiendo.')
                    limpiar_esperar_screen()
            else:
                print('ERROR! debe ingresar una opcion valida, opciones valida ("S" o "N")!')
    else:
        print('NO HAY PEDIDOS REGISTRADOS!')
    limpiar_esperar_screen()




def buscar_pedido_rut():
    print('Buscar pedido por rut!')
    limpiar_esperar_screen()   
    if len(pedidos) >=1:
        while True:
            try:
                rut = int(input('Ingrese el rut para buscar el pedido (Sin puntos ni guion): '))
                if rut >= 1000000 and rut <= 99999999:
                    print('Buscando.')
                    limpiar_esperar_screen()
                    for x in pedidos:
                        if x[0] == rut:
                            print('Pedidos')
                            print(f"\t RUT:{x[0]}\t Cliente:{x[1]}\t Direccion:{x[2]}\t Comuna:{x[3]}\t Cant.5kg:{x[4]}\t Cant.15kg:{x[5]}\t Total:{x[6]}\n")
                            time.sleep(3)
                            limpiar_esperar_screen()
                            break
                        else:
                            print('El rut no tiene ningun pedido!')
                        limpiar_esperar_screen()
                else:
                    print('ERROR! debe ingrear un rut valido que es dentro del rango 1000000 a 99999999!')
                limpiar_esperar_screen()
            except:
                print('ERROR! debe ingresar numeros enteros!')
    else:
        print('NO HAY PEDIDOS REGISTRADOS!')
    limpiar_esperar_screen()


def imprimir_ruta_csv():
    print('Imprimir hoja de ruta!')
    limpiar_esperar_screen()

    if len(pedidos)>=1:
        while True:
            try:
                comuna = int(input('Ingrese la comuna que desea repartir (1:Santiago 2:Colina 3:Pirque): '))
                if comuna in (1,2,3):
                    print('comuna ingresada correctamente!')
                    limpiar_esperar_screen()
                    break
                else:
                    print('ERROR! debe ingresar una comuna valida, comunas validas(1,2,3)!')
                limpiar_esperar_screen()
            except:
                print('ERROR! debe ingresar un numero entero!')
        while True:
            nombre_archivo = str(input('Ingrese el nombre del archivo : '))
            if len(nombre_archivo.strip()) >= 3:
                print('nombre archivo guardado!')
                limpiar_esperar_screen()
                break
            else:
                print("ERROR! debes ingresar un nombre que contenga al menos 3 caracteres!")
                limpiar_esperar_screen()
                
        with open(f'{nombre_archivo}.csv',"w",newline="") as archivo:
            titulos = ["RUT","CLIENTE","DIRECCION","COMUNA","CANT.5KG","CANT.15KG","TOTAL"]
            escritor = csv.writer(archivo)
            escritor.writerow(titulos)
            for x in pedidos:
                if x[3] == comunas[comuna-1]:
                    

                    

            escritor.writerow(lista)
               

                




        
    else:
        print('NO HAY VENTAS REGISTRADAS!')
    limpiar_esperar_screen()





def salir():
    for x in range(1,4):
        print('Saliendo de gas explosive',("."*x))
        limpiar_esperar_screen()


def limpiar_esperar_screen():
    time.sleep(1)
    os.system('cls')
    