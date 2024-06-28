import csv
import os


def menu():
    menu1 = True
    
    print('**********')
    print('   MENU')
    print('**********')
    print('1.- Grabar')
    print('2.- Buscar')
    print('3.- Imprimir certificados')
    print('4.- Salir')
    print('**********')
    while menu1:
        opcion = int(input('Ingrese su opcion: '))
        if opcion == 1:
                os.system('cls')
                opcion1()
        elif opcion == 2:
                os.system('cls')
                opcion2()    
        elif opcion == 3:
                os.system('cls')
                opcion3()
        elif opcion == 4:
                os.system('cls')
                opcion4()

def opcion1():
    
    nombre = str(input('Ingrese su nombre: '))
    apellido = str(input('Ingrese su Apellido: '))
    Edad=True
    while Edad:
        edad=int(input("Ingrese su edad: "))
        if edad >= 18:
            print("Edad valida")
            Edad=False
        else:
            print("Menor de edad, !!!por favor ingrese una edad mayor de 18 años¡¡¡")
    Estado_Civil=True
    while Estado_Civil:
        estado_civil=str(input("Ingrese Su estado civil: [S=soltero]-[C=Casado]-[V=Viudo]: ")).upper()
        n_estadocivil=len(estado_civil)
        if n_estadocivil ==1 and estado_civil == "C" or estado_civil == "S" or estado_civil== "V":
            print("Estado Civil Valido")
            Estado_Civil=False
        else:
            print("Estado Civil invalido, por falor ingresar otra vez")
    Genero=True
    while Genero:
        genero=str(input("Ingrese su genero: [Masculino = M]-[Femenino = F]-[Otro = O]: ")).upper()
        ngenero=len(genero)
        if ngenero == 1 and genero == "M" or genero == "F" or genero == "O":
            print("Genero ingresado")
            Genero=False
        else:
            print("Seleccione una de las 3 opciones")
    fecha_de_afiliacion=input("Ingrese su fecha de afiliacion, en el siguiente formato: [dd/mm/aaaa]: ")
    menuop1  = True
    while  menuop1 :
            rut = ''
            rut = input('Ingrese su RUT: ').upper()
            os.system('cls')
            niflen = len(rut)
            if niflen == 12:
                        print('RUT validado')
                        with open('Informacion_de_Afiliado.csv', 'a',newline='') as alias:
                            info = csv.writer(alias)
                            info.writerow([rut,nombre,apellido,edad,estado_civil,genero,fecha_de_afiliacion])
                        with open('Certificados.csv','a',newline='') as alias:
                            lector = csv.writer(alias)
                            cert = 0 + 1
                            lector.writerows([
                            [f'Certificado {cert}'],    
                            ['RUT','Nombre','Apellido','Edad','Estado_Civil','Genero','Fecha_deAfiliacion'],
                            [rut,nombre,apellido,edad,estado_civil,genero,fecha_de_afiliacion]
                            ]) 
                        menuop1  = False
            else:
                print('RUT no validado, intentar denuevo')
                os.system('cls')


def opcion2():
    op3w = True
    while op3w:
        rutquestion = str(input('Ingresar tu RUT: ')).upper()
        with open('Informacion_de_Afiliado.csv', 'r',newline='') as alias:
            info = csv.reader(alias)
            listarut = list(info) #es para que el index funcione
            rutlen1 = len(rutquestion)
            
            for i in listarut:
                if rutquestion in i and rutlen1 == 12 and '-' in rutquestion:
                            indice = listarut.index(i)
                            print(listarut[indice])
                            print(f'Su RUT {listarut[indice][0]} coincide con: \n Nombre: {listarut[indice][1]}\n Edad: {listarut[indice][2]}\nUnion Europea: {listarut[indice][3]}\nEstado conyugal: {listarut[indice][4]}')
                            op3w = False
                else:
                    print('Su RUT no esta registrado')


def opcion3():
    with open('Informacion_de_afiliado.csv', 'r',newline='') as alias:
        infoR = csv.reader(alias)
        for i in infoR:
            print(i)

def opcion4():
     print("SALIENDO")
     print("Gracias por utilizar Vida y Salud 2.2.1 ")
     print("Creadores: Jean Vidal, Nicolas Rubilar")
   #No nos funciona el salir

menu()