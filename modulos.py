def obtener_usuarios(nombrearchivo):
    archivo = open(nombrearchivo,"r")
    usuarios=[]
    for linea in archivo.readlines():
        usuario=linea.replace('\n','')
        usuario=usuario.split(",")
        usuario={"dni":usuario[0],"password":usuario[1],"nombre":usuario[2],"monto":usuario[3]}
        usuarios.append(usuario)
    return usuarios

