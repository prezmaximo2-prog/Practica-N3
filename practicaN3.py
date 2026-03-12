estados = 0
total_alfabeto = 0
transiciones = 0
estado_inicial = 0
estado_final = 0
total_verificar = 0

alfabeto = []
estado_aceptacion = []

transicion1 = []
transicion2 = []
transicion3 = []
transicion4 = []
transicion5 = []
transicion6 = []

verificar1 = ""
verificar2 = ""
verificar3 = ""
verificar4 = ""

try:
    with open('Practica3/documento.txt', 'r') as archivo:
        lineas = archivo.readlines()
        
        datos = lineas[0].split()
        estados = int(datos[0])
        total_alfabeto = int(datos[1])
        transiciones = int(datos[2])
        estado_inicial = int(datos[3])
        estado_final = int(datos[4])
        total_verificar = int(datos[5])
        
        alfabeto = lineas[1].split()
        estado_aceptacion = list(map(int, lineas[2].split()))
        
        transicion1 = lineas[3].split()
        transicion2 = lineas[4].split()
        transicion3 = lineas[5].split()
        transicion4 = lineas[6].split()
        transicion5 = lineas[7].split()
        transicion6 = lineas[8].split()

        verificar1 = lineas[9].strip()
        verificar2 = lineas[10].strip()
        verificar3 = lineas[11].strip()
        verificar4 = lineas[12].strip()

    lista_transiciones = [transicion1, transicion2, transicion3, transicion4, transicion5, transicion6]
    cadenas_evaluar = [verificar1, verificar2, verificar3, verificar4]

    for cadena in cadenas_evaluar:
        estado_actual = estado_inicial
        valida = True
        
        for simbolo in cadena:
            encontrado = False
            for t in lista_transiciones:
                if int(t[0]) == estado_actual and t[1] == simbolo:
                    estado_actual = int(t[2])
                    encontrado = True
                    break
            
            if not encontrado:
                valida = False
                break
        
        if valida and estado_actual in estado_aceptacion:
            print("ACEPTADA")
        else:
            print("RECHAZADA")

except FileNotFoundError:
    print('No se encontró el archivo')
except IndexError:
    print('El archivo no tiene el formato o la cantidad de líneas esperadas')
