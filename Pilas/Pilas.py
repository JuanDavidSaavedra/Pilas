from time import time


class Pila:
    def __init__(self):
        self.pila=[]
    def extraer(self):
        if len(self.pila)<1:
            print("Pila no tiene elementos")
            return None
        return self.pila.pop()
    def ingresar(self,item):
        self.pila.append(item)


mipila=Pila()
limite = 0
opcion=1

id_carro=[]
valor_park=[]

horacierre=0
opcion = 1

while limite < 8:
    print(limite)
    if limite!=7:
        sarta="Llegó el vehículo: " + str(limite+1) + " digite 1 para entrar, digite 2 para sacar: "
        ve = int(input(sarta))

        while ve!=1 and ve!=2:
            print("Opción incorrecta")
            sarta="Llegó el vehículo: " + str(limite+1) + " digite 1 para entrar, digite 2 para sacar: "
            ve=int(input(sarta))

        if ve==1:
            mipila.ingresar(time())
            limite = limite + 1

        elif ve==2:

            if limite>0:
                t1 =(time() - mipila.extraer())
                limite=limite-1
                print(t1*50)

            else:
                print("No hay carros")
    else:
        print("Parqueadero lleno")
        sarta="Digite 2 para sacar:"
        ve=int(input(sarta))
        while ve!=2:
            print("Opción incorrecta")
            ve=int(input(sarta))
        if ve==2:
            t1=(time()-mipila.extraer())
            limite=limite-1
            print(t1*50)


    #opcion = int(input("Digite 1 si desea continuar: "))
   # if x==0:
    #    horacierre=time()
     #   x=0
       #id_carro.append("Ingrese la maatricula de carro:")
       #valor_park.append(cont+=50)
#for i in range(7):
   # ve = int(input("sale un vehiculo digite 1: "))
    #if ve == 1: