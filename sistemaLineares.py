import numpy as np


def resolver_sistema():
    mat = []
    result = []

    matriz = int(input('Entre com o numero da matriz. Exemplo 3x3 entre com 3: '))

    for i in range(matriz):
        linha = []
        for ii in range(matriz):
            linha.append(float(input('Entre com a variavel: ')))
        mat.append(linha)

    for ii in range(matriz):
        result.append(float(input('Resultado da equação: ')))

    calc = np.linalg.solve(mat, result)

    print(mat)
    print(result)
    print(calc)


if __name__ == "__main__":
    resolver_sistema()
