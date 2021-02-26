import os

#clase llanta con sus propiedades
class Llanta:
    def __init__(self):
        self.__presion=0
        self.__rodada=0

#clase suspension que hereda lo de llanta, en este caso el construcotr y las propiedades
class Suspension(Llanta):
    def crear(self):#propiedades de las suspensiones
        self.__suspension=""
        self.__suspension_de_adelante=""

#clase tramision y sus propiedades
class Transmision:
    def __init__(self):
        self.__velocidaes=0
        self.__cambios=0
        self.__tipoPalanca=""

#clase frenos con sus propiedades
class Frenos:
    def __init__(self):
        self.__delantero=""
        self.__trasero=""

#clase bicicleta donde hace creacion de todo
class Bicicleta:
    #metodo constructor no hace nada
    def __init__(self):
        print("")
        #creacion de los objetos para usarlos
        self.rueda=Suspension()
        self.cambios=Transmision()
        self.frenos=Frenos()
    #metodos para armar la bicicleta
    

    #para determinar la parte de las llantas
    def setRuedas(self):
        #llamo al objeto ruedas y le pregunto y asigno los valores necesarios
        self.rueda.__presion=int(input("Dame la presion de la llanta "))
        self.rueda.__rodada=int(input("¿Cual es la rodada de la llanta? "))
        self.rueda.__suspension=input("¿Tiene suspension trasera? ")
        self.rueda.__suspension_de_adelante=input("¿Tiene suspencion delantera? ")

    #para obtener el valor de las ruedas, sirve para poder presentarlos en pantalla
    def getRuedas(self):
        print("\n\n\n---------------------------------")#un salto de linea para poder diferenciarlo de los demas
        propiedades=self.rueda.__dict__#creacion de un diccionario para tener los valores de cada uno
        llaves=propiedades.keys() #obtencion de los ID de los valores
        contador=0
        for propiedad in llaves:#para propiedad en llaves (for each ó "Para cada uno en"), propiedad es igual a lo que hay en llaves, dependiendo de la vuelta que este dando
            #como los dos primers llaves son llaves de la clase que estan vacias y no contienen nada, hago un contador para que las salte
            if contador>=3:#cuando llega a tres significa que ya las paso
                etiqueta = propiedad[12:len(propiedad)]#esta etiqueta es para presentarla infor, esta es igual a propiedad la llave dependiendo de la vuelta, tomara el nombre de la propiedadad desde el caracter 12 hasta la longitud de la palabra
                etiqueta=etiqueta.capitalize()
                print (etiqueta+":\n"+" "+str(propiedades[propiedad]))
            contador=contador+1#contador aumentna en uno para saltar las propiedades vacias

    #para determinar los cambios
    def setCambios(self):
        #ido los cambios y los asigno a sus valores
        self.cambios.__velocidades=int(input("¿Cuantas velocidades tiene? "))
        self.cambios.__cambios=int(input("¿Cuantos cambios tiene? "))
        self.cambios.__tipoPalanca=input("¿Que tipo de palanca tiene? ")

    #para mostrar los cambios
    def getCambios(self):
        print("\n\n\n---------------------------------")
        propiedades=self.cambios.__dict__
        llaves=propiedades.keys()
        contador=0
        #hago lo mismo que en el getRuedas
        for propiedad in llaves:
            if contador>2:
                etiqueta=propiedad[12:len(propiedad)]
                etiqueta=etiqueta.capitalize()
                print(etiqueta+":\n"+" "+str(propiedades[propiedad]))
            contador=contador+1

    #para determinar los frenos
    def setFrenos(self):
        #pido los datos y los asigno
        self.frenos.__delantero=input("¿Tiene frenos delanteros? ")
        self.frenos.__trasero=input("¿Tiene frenos treseros? ")

    #para mostrar los frenos
    def getFrenos(self):
        #hago lo mismo que en getRuedas
        print("\n\n\n---------------------------------")
        propiedades=self.frenos.__dict__
        llaves=propiedades.keys()
        contador=0
        for propiedad in llaves:
            if contador>1:
                etiqueta=propiedad[12:len(propiedad)]
                etiqueta=etiqueta.capitalize()
                print(etiqueta+":\n"+" "+str(propiedades[propiedad]))
            contador=contador+1


continuar='s'
array_menu=["Crear bicicleta", "Editar bicicleta","Mostrar datos", "Salir"]
array_partes=["Suspencion", "Trasmision", "Frenos"]
#MENU PRINCIPAL
while continuar=='s':
    print("Selecciona una de las opciones del menu: ")
    #presento el menu
    for i in range(len(array_menu)):
        print(str(i+1)+". "+array_menu[i])
    #seleccion de la opcion menu
    seleccion=int(input("Tu seleccion: "))
    #un switch case dependiendo de la eleccion
    if seleccion==1:#la eleccion uno es para crear la bicicleta
        bicicleta=Bicicleta()#se crea
        print("Bicicleta creado, ahora regresa al menu para editarla a tu gusto")
        menu=input("Presiona enter para continuar")#mensaje para salir
        os.system ("cls")#limpiar pantalla

        #opcion dos es para editarla la bici
    elif seleccion==2:
        os.system ("cls")#limpio pantalla
        print("¿Que parte deseas editar?")
        #para mostrar el menu de las partes
        for i in range(len(array_partes)):
            print(str(i+1)+". "+array_partes[i])
            #eleccion del usuario
        edicion=int(input("Tu seleccion: "))
        #switch case para la seleccion
        if edicion==1:#si es uno mando a llamar al objeto bicicleta y el metodo para ingresar los tados a ruedas
            bicicleta.setRuedas()
        elif edicion==2:#si es dos mando a llamar al objeto bicicleta y el metodo para ingresar los tados a cambios
            bicicleta.setCambios()
        elif edicion==3:#si es tres mando a llamar al objeto bicicleta y el metodo para ingresar los tados a frenos
            bicicleta.setFrenos()
        else:
            print("Opcion incorrecta vuelve al menu pricipal")
   #si la eleccion en el menu principal es tres
    elif seleccion==3:
        print("Se mostraran los datos")#presento todos los datos con los get de cada propiedad
        bicicleta.getRuedas()
        bicicleta.getCambios()
        bicicleta.getFrenos()
    elif seleccion==4:#para salir
        print("Perfecto nos vemos")
        menu=input("Presiona enter para continuar")
        os.system ("cls")
        continuar='z'#rompo el while
    else:#para q no le juege al vrgas y meta cosas q no son
        print("Selecciona una de las opciones disponibles")
        menu=input("Presiona enter para continuar")
        os.system ("cls")

