import numpy

print()
print("     -----   Maximización Por Simplex    -----           ")
print()
print("Ingrese El Valor de: ")
print()
NumVar = int(input("    El Número De Variables    :   "))
NumRest = int(input("    El Número De Restriciones  :   "))
print()
'''

            MatrizRstr me almacena las ecuaciones de restricción
            TablaSimplex = MatrizRstr + la ecuación objetivo

'''

NumCol = NumRest + NumVar +2
NumFil = NumRest +1
cont = 0

MatrizRstr = numpy.zeros((NumRest , NumVar), dtype=float)
TablaSimplex = numpy.zeros((NumRest + 1 , NumVar + NumRest + 2), dtype=float)
Resultado = list(range(NumRest))
Holgura = numpy.zeros((NumRest, NumRest), dtype=float)
Ecuacn = list(range(NumCol))           #   Ecuacion a Mazimizar
ArreAux = list(range(NumFil))
EcuNuv = list(range(NumCol))            #   Ecuación Resultado despues de proceso
Solucionado = bool

for c in range(0,NumRest):
    for f in range (0,NumVar):
        MatrizRstr[c,f] = input(" La Variable " + str(f+1) + " De La Restricción " + str(c+1) + " : ")

print()


for h in range(0,NumRest):
    Resultado[h] = input("  El resultado de la restricción "+ str(h+1) +" : ")
'''
Holgura
'''
for f in range(0, NumRest):
    for c in range(0, NumRest):
        if (f == c):
            Holgura[f,c] = 1
'''

    Lleno la Tabla Simplex

'''
print()
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
                TablaSimplex[f,c] = -1*(float(input("   El valor De La Variable " + str(c) + " De La Ecuacion Objetivo : ")))
        if(c>NumVar and c<NumCol-1 and f<NumFil-1):
                    TablaSimplex[f,c] = Holgura[f,c-NumVar-1 ]
'''

    Proceso Simplex

'''
while(Solucionado != True):
    cont = cont + 1
    print()
    print(" la Tabla simplex "+str(cont)+" es :   ")
    print()
    print(TablaSimplex)
    print()
    '''
        1. Encontrar los pivotes
    '''
    Ep = 0          # Elemento Pivote
    ifp = 0         # Indice de la fila pivote
    icp = 0         # Indice de la columna pivote
    for c in range(0, NumCol):
        Ecuacn[c] = (TablaSimplex[NumFil-1,c])
        icp = Ecuacn.index(min(Ecuacn))
    for f in range (0,NumFil-1):
        if(TablaSimplex[f,icp] != 0):
            ArreAux [f] = TablaSimplex[f,NumCol-1] / TablaSimplex[f,icp]
            ifp = ArreAux.index(min(ArreAux))
    Ep = TablaSimplex[ifp,icp]
    '''
        2. Operar y Actualizar La Tabla Simplex
    '''
    for f in range (0, NumFil):
        for c in range(0,NumCol):
            if(f==ifp):
                if (Ep != 0):
                    TablaSimplex[ifp,c] = TablaSimplex[ifp,c] / Ep
            else:
                TablaSimplex[f,c] = TablaSimplex[f,c] - (TablaSimplex[f,icp] * TablaSimplex[ifp,c])

    print()
    print(TablaSimplex)
    print()
    print(" Los Valores de la Tabla simplex "+str(cont)+" son :   ")
    print()
    for f in range (0, NumFil):
        for c in range(0,NumCol):
            if(f == NumFil):
                EcuNuv[c] = -1*TablaSimplex[f,c]
                print()
            print(TablaSimplex[f,c], end=" , ")
            print()
    yes = 0
    for c in range(0,NumCol):
        if(max(EcuNuv) <= 0):
            yes = yes +1

    if(yes >= NumCol-1):
        Solucionado = True
        break

