import os



def limpiar_pantalla():
    os.system('cls')

def longitud_lista(mi_lista):
    longitud = 0
    for i in mi_lista:
        longitud += 1
    return longitud

def agregar_notas(mi_lista):
    cantidad_notas = int(input("Ingrese cantidad de notas a Ingresar: "))
    i=0
    while i < cantidad_notas:
        num = float(input(f"Ingrese la nota {i+1}: "))
        if(i < 0):
            print("Ingrese una nota valida...")
            continue
        else:
            mi_lista.append(num)
            i+=1
    
    print("Notas Agregadas con exito.")

def mostrar_notas(mi_lista):
    if not mi_lista:
        print("[!] No hay notas registradas...\nSe pueden registrar notas en la opcion 1")
    else:
        for i,j in enumerate(mi_lista, start=1):
            print(f"Nota {i}: {j}")

def calcular_promedio(mi_lista):
    if not mi_lista:
        print("[!] No hay notas registradas...\nSe pueden registrar notas en la opcion 1")
    else:
        longitud = longitud_lista(mi_lista)
        sum = 0
        for i in range (0, longitud):
            sum += mi_lista[i]
        print("El promedio de las notas es: %.1f" % (sum / longitud))
    
def contar_aprobados_reprobados(mi_lista):
    if not mi_lista:
        print("[!] No hay notas registradas...\nSe pueden registrar notas en la opcion 1")
    else:
        aprobados = 0
        reprobados = 0
        
        longitud = longitud_lista(mi_lista)
        for i in range(0, longitud):
            if (mi_lista[i] >= 4.0):
                aprobados += 1
            else:
                reprobados += 1
        print("La cantidad de alumnos que aprobaron fueron: %d\nLa cantidad de alumnos que reprobaron fueron: %d" % (aprobados,reprobados))

def notas_altas_bajas(mi_lista):
    if not mi_lista:
        print("[!] No hay notas registradas...\nSe pueden registrar notas en la opcion 1")
    else:
        mayor = 0
        menor = 0
        longitud = longitud_lista(mi_lista)
        for i in range(0, longitud):
            if (i == 0):
                mayor = mi_lista[i]
            
            elif(mi_lista[i] > mayor):
                mayor = mi_lista[i]
            else:
                menor = mi_lista[i]

        print("La nota mas alta fue: %.1f\nLa nota mas baja fue: %.1f" % (mayor, menor))

def eliminar_ultima_nota(mi_lista):
    if not mi_lista:
        print("[!] No hay notas registradas...\nSe pueden registrar notas en la opcion 1")
    else:
        ultima_nota = mi_lista.pop()
        print(f"La nota {ultima_nota} fue eliminada ahora queda: {mi_lista}")
notas = []

while True:
    try: 
        limpiar_pantalla()
        print("---------- Menu:  ----------")
        print("1. Agregar notas: ")
        print("2. Mostrar todas las notas: ")
        print("3. Calcular promedio: ")
        print("4. Contar aprobados y reprobados: ")
        print("5. Notas mas altas y mas bajas: ")
        print("6. Eliminar la ultima nota ingresada")
        print("7. Salir ")

        opcion = int(input("Ingrese una opcion: "))
        
        if(opcion > 0 and opcion < 8):
            match opcion:
                case 1:
                    try:
                        limpiar_pantalla()
                        agregar_notas(notas)
                        input("Aprete enter para continuar: ")
                    except ValueError:
                        print("Error: Ingrese un número válido.")
                        input("Aprete enter para continuar: ")
                case 2:
                    limpiar_pantalla()
                    mostrar_notas(notas)
                    input("Aprete enter para continuar: ")
                    
                case 3:
                    limpiar_pantalla()
                    calcular_promedio(notas)
                    input("Aprete enter para continuar: ")
                    
                case 4:
                    limpiar_pantalla()
                    contar_aprobados_reprobados(notas)
                    input("Aprete enter para continuar: ")
                    
                case 5:
                    limpiar_pantalla()
                    notas_altas_bajas(notas)
                    input("Aprete enter para continuar: ")
                    
                case 6:
                    limpiar_pantalla()
                    eliminar_ultima_nota(notas)
                    input("Aprete enter para continuar: ")
                    
                case 7:
                    break
        else:
            print("[!] Ingrese una opcion valida...")
    except ValueError:
        print("[!] Ingrese un valor numerico valido")
                