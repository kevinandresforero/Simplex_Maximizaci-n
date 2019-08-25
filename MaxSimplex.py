import numpy

print()
print("     -----   Maximización Por Simplex    -----           ")
print()
NumVar = int(input("    Ingrese El Número De Variables    :   "))
NumRest = int(input("    Ingrese El Número De Restriciones  :   "))
print()
'''

            MatrizRstr me almacena las ecuaciones de restricción
            TablaSimplex = MatrizRstr + la ecuación objetivo

'''

NumCol = NumRest + NumVar +2
NumFil = NumRest +1

MatrizRstr = numpy.zeros((NumRest , NumVar))
TablaSimplex = numpy.zeros((NumRest + 1 , NumVar + NumRest + 2))
Resultado = list(range(NumRest))
Holgura = numpy.zeros((NumRest, NumRest))

print(" Ingrese El Valor de: ")
print()
for c in range(0,NumRest):
    for f in range (0,NumVar):
        MatrizRstr[c,f] = input(" La Variable " + str(f+1) + " De La Restricción " + str(c+1) + " : ")

print()


for h in range(0,NumRest):
    Resultado[h] = input("Ingrese el resultado de la restricción "+ str(h+1) +" : ")

print()
print(" la matriz de restriccíon es :   ")
print()
print(MatrizRstr)
print()

'''Holgura'''
for f in range(0, NumRest):
    for c in range(0, NumRest):
        if (f == c):
            Holgura[f,c] = 1

'''Lleno la Tabla Simplex'''
for f in range(0, NumFil):
    for c in range(0, NumCol):
        if(c>0 and c<NumVar+1 and f < NumFil-1):
            TablaSimplex[f,c] = MatrizRstr[f,c-1]
        if(c == NumCol-1  and f < NumFil-1 ):
            TablaSimplex[f,c] = Resultado[f]
        if(c==0):
            if(f < NumRest):
                TablaSimplex[f,c] = 0
            else:
                TablaSimplex[f,c] = 1
        else:
            if (f == NumFil-1 and c < NumVar+1):
                TablaSimplex[f,c] = -1*(float(input("Ingrese El valor De La Variable " + str(c) + " De La Ecuacion Objetivo : ")))
        if(c>NumVar and c<NumCol-1 and f<NumFil-1):
                    TablaSimplex[f,c] = Holgura[f,c-NumVar-1 ]

print()
print(" la Tabla simplex es :   ")
print()
print(TablaSimplex)
print()


