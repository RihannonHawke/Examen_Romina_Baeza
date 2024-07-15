import random
import csv
import math

trabajadores = [
    {"Nombre": "Juan Pérez"},
    {"Nombre": "María García"},
    {"Nombre": "Carlos López"},
    {"Nombre": "Ana Martinéz"},
    {"Nombre": "Pedro Rodríguez"},
    {"Nombre": "Laura Hernández"},
    {"Nombre": "Miguel Sánchez"},
    {"Nombre": "Isabel Gómez"},
    {"Nombre": "Francisco Díaz"},
    {"Nombre": "Elena Fernandez"}
]
sueldos =[]

def calcular_sueldo():
    global sueldos
    sueldos = [random.randint(300000, 2500000) for _ in trabajadores]
    print("Sueldos asignados aleatoriamente")
    
def clasificar_sueldos():
       
    for trabajador, sueldo in zip(trabajadores, sueldos):
     
        if sueldo < 800000:
            print(f"Nombre del empleado: {trabajador ['Nombre']} Sueldo: ${sueldo},sueldo bajo")
           
        elif sueldo <= 2000000 and sueldo >= 800000:
            print(f"Nombre del empleado: {trabajador['Nombre']} Sueldo: ${sueldo}, sueldo medio")
        
        elif sueldo > 2000000:
            print(f"Nombre del empleado: {trabajador['Nombre']} Sueldo: ${sueldo}, sueldo alto")
    print("total de sueldos $",sum(sueldos))
    
def estadisticas():
    sueldo_max = max(sueldos)
    sueldo_min = min(sueldos)
    sueldo_promedio = sum(sueldos) / len(sueldos)
    sueldo_geom = math.exp(sum(math.log(sueldo) for sueldo in sueldos) / len(sueldos))

    print(f"Sueldo más alto: ${sueldo_max}")
    print(f"Sueldo más bajo: ${sueldo_min}")
    print(f"Promedio de sueldos: ${sueldo_promedio:.2f}")
    print(f"Media geométrica de sueldos: ${sueldo_geom:.2f}")
    
def reporte_sueldos():
    with open('reporte_sueldos.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Nombre empleado", "Cargo", "Sueldo Base", "Descuento Salud", "Descuento AFP", "Sueldo Líquido"])
        for trabajador, sueldo in zip(trabajadores, sueldos):
            salud = sueldo*0.07
            afp = sueldo*0.12
            liquido = sueldo - salud - afp
            writer.writerow([trabajador["Nombre"], sueldo, salud, afp, liquido])
            print(f"Nombre empleado: {trabajador['Nombre']} Sueldo Base: ${sueldo} Descuento Salud: ${salud:.2f} Descuento AFP: ${afp:.2f} Sueldo Líquido: ${liquido:.2f}")
        print("Reporte de sueldos generado")
        
def salir():
    print("Finalizando programa...")
    print("Desarrollado por Romina Baeza")
    print("RUT: 16.938.082-1")
    exit()

while True:
    print("1. Asignar sueldos aleatorios")
    print("2. Clasificar sueldos")
    print("3. Ver estadisticas")
    print("4. Reporte de sueldos")
    print("5. Salir del programa")
    
    opcion = input("Opción: ")
    
    if opcion == "1":
        calcular_sueldo()
    elif opcion == "2":
        clasificar_sueldos()
    elif opcion == "3":
        estadisticas()
    elif opcion == "4":
        reporte_sueldos()
    elif opcion == "5":
        salir()
    else:
        print("Opción no válida")
    