#Dados los lados de un triangulo, determinar su area, perimetro, tipo y grafico
a = int(input("Ingrese primer lado: "))
b = int(input("Ingrese segundo lado: "))
c = int(input("Ingrese tercer lado: "))
if (a+b)>c and (a+c)>b and (b+c)>a:
    p = a + b + c
    s = p/2
    area = (s*(s-a)*(s-b)*(s-c))**.5
    if a != b and b != c and a != c :
        print("Triangulo Escaleno de perimetro =",p," y area =",area)
        #Llamar graficador
    else :
        if (a == b) and (b == c) :
            print("Triangulo Equilatero de perimetro =",p," y area =",area)
        else :
            print("Triangulo Isósceles de perimetro =",p," y area =",area)
else :
    print("No es triangulo")

def triangulo (a,b,c):
    program statement1
    program statement3
    program statement3
    ...
            
        
