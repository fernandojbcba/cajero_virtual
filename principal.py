##importacion de librerias
from modulos import obtener_usuarios, validar_dni,numerales_renglon, validarIngresoNumeroEntero, verificacion_password,tempo
import time, os
import getpass

#cargo lista de usuarios
def cajero():
    listadodeusuarios= obtener_usuarios("bd_user.md")
    # print(listadodeusuarios)

##inicializacion cajero.
    print(f'''\t
============================
Bienvenido al cajero Virtual
============================
cargando usuarios.''')
##busca usuario por dni.
    encontrado=False
    usuario_encontrado=[]
    while encontrado == False:
        ingreso_dni = input("ingrese su dni: ")
        if validar_dni(str(ingreso_dni)) == True:
            for elem in listadodeusuarios: 
                if elem['dni'] == ingreso_dni :
                    usuario_encontrado=elem
                    encontrado=True
                    break
            else:
                print("Debes ingresar un numero dni valido")
##validar password
    password_ok=False
    intentos=1
    tempo(8)
    while (password_ok == False) and (intentos != 4):
        print(f'''#### Validacion de Password ####:
    tiene 3 intentos, este es su intento numero {intentos}''')
        print("ingrese password: ")
        p1=getpass.getpass()
        p2=usuario_encontrado['password']
        if verificacion_password(p1,p2) == True:
            password_ok=True
            tempo(3)
        else:
            print(f"ingrese password correcto")
            intentos=intentos +1
            time.sleep(2)
            os.system("clear")
            tempo(5)
        
    if intentos >= 4:
        print("su cuenta a sido Bloquedada")
        tempo(10)
        cajero()

    while True:
        print(f'''
            ============================
            Bienvenido al cajero Virtual
            ============================
''')
        print(
            f'''
            \t Menu
            [1] Extraccion
            [2] Deposito
            [3] ver Datos de usuario
            [0] Salir
            ''')
        opcion = validarIngresoNumeroEntero("Ingrese opcion: ")

        if opcion == 0:
            break
        elif opcion == 1:
            numerales_renglon()
            print("Extraccion")

        elif opcion == 2:
            numerales_renglon()
            print("deposito")
            
        elif opcion == 3:
            numerales_renglon()
            print("ver datos")
            
        else:
            numerales_renglon()
            print("Elija una opcion correcta")

    print("Fin del sistema")

cajero()
# print(usuario_encontrado)
# print(listadodeusuarios)






