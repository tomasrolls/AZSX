#Suma de los primeros n numeros pares:
n = int(input("Ingrese n"))
i = 0
s = 0
while (i < n):
    i = i + 2
    p = 2*i
    s = s + p
print("La suma de los ",n," numeros pares es",s)
