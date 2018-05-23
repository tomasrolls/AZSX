#Suma de los primeros n numeros impares:
n = int(input("Ingrese n"))
i = 0
s = 0
while (i < n):
    i = i + 1
    imp = 2*i - 1
    s = s + imp
print("La suma de los ",n," numeros pares es",s)
