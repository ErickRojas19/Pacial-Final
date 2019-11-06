from datetime import datetime

placas = {}
cont = 0

while True:

    print("Por favor escoja una opción de las siguientes")

    print ("\n1 Agregar Vehiculo"
           "\n2 Retirar Vehiculo"
           "\n3 Reporte total"
           "\n4 Salir")
    opcion = int(input("Escriba la opcion: "))

    numero_ve = 0
    hora = 0
    if (opcion == 1):
        hora = datetime.now()
        placa = input("Escriba la placa del vehiculo: ")
        print ("Su hora de entrada es: ", hora)
        placas[hora] = placa
        print(placas.keys())

    if (opcion == 2):
        precio_f = placas - hora
        valor_t = precio_f * 80
        print("Valor a pagar: ",valor_t)

    if (opcion == 3):
        cont = valor_t + 1
        total_ = cont + valor_t

    if (opcion == 4):
        break
