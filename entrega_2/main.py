from class_cliente import *
from funciones import crear_pedido, crear_usuario 

#se crea una instancia de la clase Cliente
cliente_1 = Cliente("Ricardo","manzo","siemprevida 2323","rl_manzo@hotmail.com")

#se imprime el metodo str
print(cliente_1)

#se ejecuta el metodo "Login" de la clase. 
cliente_1.login()
cliente_1.comprar("heladera","Gafa")


#ADICIONAL:
#Se crearon 2 funciones para utilizar los metodos de las clases.

#Funcion para instanciar la clase.
crear_usuario()

#Funcion para llamar al metodo comprar de la clase cliente
crear_pedido(cliente_1)
