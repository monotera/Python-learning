import os
import time

def menu ():
 os.system('clear') #funcion que limpia pantalla
 print ("Agenda con lista negra")
 print ("\tseleccione una opción")
 print ("\t1 - Ingresar datos de contacto")
 print ("\t2 - Contactos que me caen bien")
 print ("\t3 - Contactos que me caen mal")
 print ("\t4 - Eliminar un contacto")
 print ("\t5 - Buscar un contacto")
 print ("\t6 - Salir")

directorio = []
telefonos = {}
nombres = {}
direcciones = {}
estados = {}
caen_bien = {}
caen_mal = {}
opcion = 0


while opcion != 6:
        menu()
        opcion=int(input('Digite el numero de la opcion que desea ver: '))

        if opcion == 1:
            ya = True
            while ya == True:
                nombre = input('Nombre: ')
                if nombre in telefonos:
                    print('Ya existe un contacto con ese nombre.')
                else:
                    ya = False
            telefono = input('Telefono: ')
            direccion = input('Direccion: ')
            estado = input ('Estado (1 para bien, 2 para mal): ')
            telefonos[nombre] = telefono
            nombres[telefono] = nombre
            direcciones[nombre] = direccion

            if estado == '1':
                estados[nombre] = 'bien'
                caen_bien[nombre] = nombre

            elif estado == '2':
                estados[nombre] = 'mal'
                caen_mal[nombre] = nombre


        elif opcion == 2:
            for a in caen_bien:
                print (caen_bien[a])    
            input('Presione enter para continuar') 

        elif opcion ==3:
            for a in caen_mal:
                print (caen_mal[a])    
            input('Presione enter para continuar')

        elif opcion == 4:
            nombre = input('Nombre: ')
            if nombre in telefonos:
                otro = telefonos.pop(nombre)
                nombres.pop(otro)
                direcciones.pop(nombre)
                valor = estados.pop(nombre)
                if valor == 'bien':
                    caen_bien.pop(nombre)
                elif valor == 'mal':
                    caen_mal.pop(nombre)
            input('Presione enter para continuar')  
        elif opcion == 5:
            nombre = input('Nombre: ')
            if nombre in telefonos:
                print("Telefono: ", telefonos[nombre])
                print("Direccion: ", direcciones[nombre])
                print("Estado: Me cae", estados[nombre])
            input('Presione enter para continuar') 