#Dados a, b, c determinar las raices de la ec. de 2do grado.
a = float(input("Ingrese primer numero:"))
b = float(input("Ingrese segundo numero:"))
c = float(input("Ingrese tercer numero:"))
if a == 0:
    print("a Debe ser mayor a cero")
else:
    d = (b**2-4*a*c)
    if d == 0:
        print("Las raices son iguales:",-b/(2*a))
    else:
        x1 = (-b + (d)**.5)/(2*a)
        x2 = (-b - (d)**.5)/(2*a)
        print("Las raices son x1, x2:",x1, "," , x2)
