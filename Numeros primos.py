a = int(input("Establezca el número mínimo del rango: "))
b = int(input("Establezca el número máximo del rango: "))

def listap(num):
    if num<2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

prim = [num for num in range(a, b +1)if listap(num)]
print(prim)