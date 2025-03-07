'''
Operadores Logicos

'''

op1 = False
op2 = True
op3 = op1 and op2 

op4 = not op1
print(op4)

'''
Jerarquia definitiva de operadores 
NOTA: si hay operaciones en el mismo nivel 
de jerarquia, se resuelven de izquierda a derecha
            1.  ()
            2.  **
            3.  *, /, %
            4.  +, -
            5.  <, >, <=, >=, != 
            6.  NOT
            7.  AND
            8.  OR
            9.  =
'''


op1 = False
op2 = True
op3 = False
op4 = True

resultado = not op1 and (op2 or op3 and not op1) and not op4

print (resultado)