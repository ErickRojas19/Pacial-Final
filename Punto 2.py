notas = []
def calcular_notas():
    

    for i in range (0,5):

        nota1 = float(input("Digite la nota del 30%: "))
        nota2 = float(input("Digite la nota del 30%: "))
        nota3 = float(input("Digite la nota del 40%: "))

        a = nota1*0.3
        b = nota2*0.3
        c = nota3*0.4

        notaf= a+b+c

        if notaf < 2:
            print("No aprobaste y aparte no puede hablitar, perdio la platica papa {} Es tu nota " .format(notaf))
        elif notaf < 3:
            print("No aprobaste, puede habilitar de todas maneras {} Es tu nota ".format(notaf))
        elif notaf < 4:
            print("Aprobaste pero puedes mejorar {} Es tu nota ".format(notaf))
        elif notaf >= 4.5:
            print("Aprobaste! eres el mejor y ella te ama {} Estu nota  ".format(notaf))
        
        notas.append(notaf)
        print(notas)

calcular_notas()