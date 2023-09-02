from class_cliente import *

#Funcion para crear pedido usando metodo de la clase "Cliente"

def crear_pedido(cliente):
    print(cliente)
    producto = str(input("Que producto estas comprando?: ")) 
    marca = str(input("escribe el tipo de marca seleccionada: ")) 
    cliente.comprar(producto, marca)

#Funcion para registrar usuario a partir de la clase "Cliente"

def crear_usuario():
    nombre = input("ingrese su nombre: ")
    apellido = input("ingrese su apellido: ")
    direccion = input("ingrese su direccion: ")
    email = input("ingrese su email: ")
    print("su usuario ha sido creado")
    cliente = Cliente(nombre,apellido,direccion,email)
    print(cliente)    