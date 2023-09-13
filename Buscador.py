list = [62, 51, 19, 14]

num = int(input("Ingrese el número a buscar: "))

for i in list:
    if i==num:
        print("El número se encuentra en la lista")
        break
    else:
        print("El número no se encuentra en la lista")
        break