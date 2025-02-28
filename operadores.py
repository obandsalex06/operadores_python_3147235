# operadores en phyton

'''
los operadores en phyton siguen elsiguiente orden jerarquico
1.                 (  )
2.                  **
3.               / , * , %
4.                 + , -
5.                   =
NOTA1: Si hay operaciones de la misma jerarquia, 
se resuelven de izquierda a derecha

NOTA2: Si hay parentesis dentro del parentesis 
se resuelve primero el parentesis interno.
'''

a = 3
b = 2
c = 1
x = 5
y = ((2 * a + c) / 7) * (a + (4 * a) / c)

print (y)
