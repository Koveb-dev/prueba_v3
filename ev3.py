from funciones_gasexplosive import *


print('Bienvenido a la app Gas explosive!')
limpiar_esperar_screen()

opciones = (1,2,3,4,5)

while True:
    limpiar_esperar_screen()
    opc = menu_opciones((opciones))
    if opc == 1:
        registrar_pedido()
    elif opc == 2:
        listar_todos_pedidos()
    elif opc == 3:
        buscar_pedido_rut()
    elif opc == 4:
        imprimir_ruta_csv()
    else:
        salir()
        break
