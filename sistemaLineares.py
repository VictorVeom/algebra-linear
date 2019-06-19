import numpy as np
 
linha = [ ] 
mat = [ ] 
result = [ ] 

matriz = int (input ('Entre com o numero da matriz. Exemplo 3x3 entre com 3: ')) 

for i in range (matriz): 
    for ii in range (matriz): 
        linha.append (float(input('Entre com a variavel: '))) 
    mat.append(linha) 

    linha = [ ] 
    print(linha)
    print(mat)

for ii in range (matriz): 
    result.append (float(input('Resultado da equação: '))) 

calc = np.linalg.solve(mat, result) 

print(mat)

print(result)

print(calc)
