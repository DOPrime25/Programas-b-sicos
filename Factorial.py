num = int(input("Ingresa el número cuyo factorial se desea calcular: "))
fact = 1

for i in range(1, num+1):
    fact = fact*i

print("El factorial de ",num," es: ")
print(fact)