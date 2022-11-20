## importacion de modulos
from modulos import obtener_usuarios
import time
#cargo lista de usuarios
listadodeusuarios= obtener_usuarios("bd_user.md")
print(listadodeusuarios)

##inicializacion cajero.
print(f'''\t
============================
Bienvenido al cajero Virtual
============================
cargando usuarios.''')
encontrado=[]
for elem in listadodeusuarios:      
    if elem['dni']=="11111111":
        elem['monto']= str(int(elem['monto']) + 1000)
        encontrado=elem


print(encontrado)
print(listadodeusuarios)


# for i in range(5):
#     print("." * i)
#     time.sleep(1)


# usuario_encontrado=[]
# filtro=str(31054623)
# for u in listadodeusuarios:
#     usuario = u.replace("\n","") 
#     usuario = usuario.split(",") 
#     if filtro.lower() in usuario[0].lower():
#         usuario_encontrado=usuario


