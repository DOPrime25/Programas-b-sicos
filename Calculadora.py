def menu(opc):
    print("¿Qué operación desea realizar?")
    print("1.- Suma")
    print("2.- Resta")
    print("3.- Multiplicación")
    print("4.- División")
    print("5.- Salir")
    opc=int(input())
    return True

def suma(num1, num2):
    num1 = input("Ingrese el primer número")
    num2 = input("Ingrese el segundo número")
    plus = num1+num2
    print("El resultado es: ",plus)
    return True

def resta(num1, num2):
    num1 = input("Ingrese el primer número")
    num2 = input("Ingrese el segundo número")
    minus = num1-num2
    print("El resultado es: ",minus)
    return True

def multipl(num1, num2):
    num1 = input("Ingrese el primer número")
    num2 = input("Ingrese el segundo número")
    times = num1*num2
    print("El resultado es: ",times)
    return True

def divi(num1, num2):
    num1 = input("Ingrese el primer número")
    num2 = input("Ingrese el segundo número")
    divided = num1/num2
    print("El resultado es: ",divided)
    return True

menu(opc=0)

