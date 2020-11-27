import os
name=input("Hola Bienvenido Antes de comenzar Quisiera saber como te llamas..... ")
name = name.upper()

def calculadora():
    print("               +-----------------------------------------+")
    print("               |                                         |")
    print("               |             BASIC CALCULATOR            |")
    print("               |                 BIENVENID@              |")
    print("               |                                         |")
    print("               +-----------------------------------------+")
    print("               +-----+  +-----+  +-----+  +-----+  +-----+")
    print("               |     |  |     |  |     |  |     |  |     |")
    print("               +-----+  +-----+  +-----+  +-----+  +-----+")
    print("               +-----+  +-----+  +-----+  +-----+  +-----+")
    print("               |     |  |     |  |     |  |     |  |     |")
    print("               |     |  |     |  |     |  |     |  |     |")
    print("               +-----+  +-----+  +-----+  +-----+  +-----+")
    print("               +-----+  +-----+  +-----+  +-----+  +-----+")
    print("               |     |  |     |  |     |  |     |  |     |")
    print("               |     |  |     |  |     |  |     |  |     |")
    print("               +-----+  +-----+  +-----+  +-----+  +-----+")
    print("               +-----+  +-----+  +-----+  +-----+  +-----+")
    print("               |     |  |     |  |     |  |     |  |     |")
    print("               |     |  |     |  |     |  |     |  |     |")
    print("               +-----+  +-----+  +-----+  +-----+  +-----+")



    reboot = "SI"

    while reboot == "SI":
        print("")
        num1=int(input("Por favor ingresa el Primer numero.. "))
        print("")
        num2=int(input("Por favor ingresa el Segundo numero.. "))
        print("")
        operador=input(name + "\n\nIndicame porfavor que operacion deseas realizar---->> +  -  /  * <<---- == " )
        if operador == "+":
            resultado = num1 + num2
            print("\n\n*********************************************************")
            print("El resultado de la SUMA de los 2 numeros es", resultado)
            print("*********************************************************")
            print("")
        elif operador == "-":
            resultado = num1 - num2
            print("\n\n*********************************************************")
            print("El resultado de la RESTA de los 2 numeros es", resultado)
            print("*********************************************************")
            print("")
        elif operador == "/":
            resultado = num1 / num2
            
            print("\n\n*********************************************************")
            print("El resultado de la DIVISION de los 2 numeros es", resultado)
            print("*********************************************************")
            print("")
        elif operador == "*":
            resultado = num1 * num2
            print("\n\n*********************************************************")
            print("El resultado de la MULTIPLICACION de los 2 numeros es", resultado)
            print("*********************************************************")
            print("")
        print("")
        reboot = input(name + " Deseas realizar otra operacion para confirmar  'SI' de lo contrario 'NO' \n\n ----->>>  ")
        reboot = reboot.upper()
        print(reboot)
        os.system ("cls") 


calculadora()


