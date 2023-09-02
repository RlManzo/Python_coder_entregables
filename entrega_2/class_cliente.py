class Cliente:
    
    def __init__(self, nombre, apellido, direccion, mail):
        self.nombre = nombre
        self.apellido = apellido
        self.direccion = direccion
        self.mail = mail
        

    def comprar(self,producto,marca):
         
         print(f"Agregaste {producto} de la marca {marca} a tu carrito")
         print("Gracias por tu compra" )

    def login(self):
        usuario =  input("escribe tu nombre de usuario: ")
        contraseña = input("escribe tu password: ")
        print(f"Bienvenido usuario: {usuario}")

    def __str__(self):
        return f"bienvenido a nuestra tienda {self.nombre}"


