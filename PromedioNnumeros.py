#Dados n numeros determinar su promedio
n = int(input("Total de numeros a promediar:"))
i = 0
s = 0
count = 0
while i < n:
    i = i + 1
    texto = "Ingrese dato numero"+str(i)+":"
    x = float(input(texto))
    s = s + x
p = s/n
print("El promedio de los numeros ingresados es:",p)
