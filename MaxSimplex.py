import numpy

print()
print("     -----   Maximización Por Simplex    -----           ")
print()
NumVar = int(input("    Ingrese El Número De Variables  :   "))
NumRest = int(input("    Ingrese El Número De Restriciones   :   "))
print()
'''

            MatrizRstr me almacena las ecuaciones de restricción
            TablaSimplex = MatrizRstr + la ecuación objetivo

'''
MatrizRstr = numpy.zeros((NumRest , NumVar))
TablaSimplex = numpy.zeros((NumRest + 1 , NumVar + 1))

print(" Ingrese El Valor de: ")
print()
for c in range (0,NumRest):
    for f in range (0,NumVar):
        MatrizRstr[c,f] = input(" La Variable " + str(f+1) + " De La Restricción " + str(c+1) + " : ")
print()

print(MatrizRstr)
