import os, re, time
def obtener_usuarios(nombrearchivo):
    archivo = open(nombrearchivo,"r")
    usuarios=[]
    for linea in archivo.readlines():
        usuario=linea.replace('\n','')
        usuario=usuario.split(",")
        usuario={"dni":usuario[0],"password":usuario[1],"nombre":usuario[2],"monto":usuario[3]}
        usuarios.append(usuario)
    return usuarios

def validar_dni(dni):
    if len(dni) == 8:
        if re.search('[0-9]', dni):
            return True
    else:
        return False
def numerales_renglon(caracter="#",cantidad=50):
    os.system("clear")
    print(caracter*cantidad)
    print(caracter*cantidad)       

def validarIngresoNumeroEntero(mensaje, msjError="Ingrese un numero entero"):
    while True:
        try:
            entero = int(input(mensaje))
            break
        except ValueError:
            print(msjError)
    return entero

def validar_password(p1,p2):
    if len(p1) == 4:
        if re.search('[0-9]', p1):
            if p1 == str(p2):
                print("password correcto")
                return True
        else:
            return False



## verificacion de password de usuario
def verificacion_password(p1,p2):
    if p1 == str(p2):
        print("password correcto")
        return True
    else:
        print("password incorrecto")

def tempo(r):
    for i in range(r):
        print("*" * i)
        time.sleep(5/10)
        os.system("clear")