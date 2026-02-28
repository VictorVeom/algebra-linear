import math


def converterGrausParaRad(numero):
    rad = (numero / 180) * math.pi
    return rad


def seno(numero):
    resultado = math.sqrt(1 - coseno(numero) ** 2)
    return resultado


def coseno(rad):
    numero = converterGrausParaRad(rad)
    cont = 0
    resultado = 1
    while cont < 50:
        cont += 1
        resultado += ((-1) ** cont * numero ** (2 * cont)) / math.factorial(2 * cont)
    return round(resultado, 6)


def entrar():
    mat = []
    quantidade = int(input('Entre com quantos (x,y) voce deseja. Exemplo (x,y), (x,y) entre com 2: '))
    for i in range(quantidade):
        linha = []
        for ii in range(2):
            linha.append(float(input('Entre com a variavel: ')))
        mat.append(linha)
    print("Voce escoheu esses x e y: ")
    print(mat)
    return mat


def escolher_eixo():
    eixo = input("Voce quer alterar X ou Y?").strip().upper()
    if eixo == "X":
        return 0
    elif eixo == "Y":
        return 1
    print('Voce nao escolheu X ou Y' + '\033[1m' + ' TENTE NOVAMENTE' + '\033[0m')
    return escolher_eixo()


def transformar_eixo(matriz, eixo, func):
    for ponto in matriz:
        ponto[eixo] = func(ponto)


def dilatacaoXeY():
    matriz = entrar()
    uni = float(input("Quantas unidades para X e Y? Exemplo: 1 ou -1"))
    for ponto in matriz:
        ponto[0] *= uni
        ponto[1] *= uni
    print(matriz)


def dilatacaoXouY():
    matriz = entrar()
    eixo = escolher_eixo()
    nome = "Y" if eixo == 1 else "X"
    uni = float(input(f"Quantas unidades para {nome}? Exemplo: 1 ou -1"))
    transformar_eixo(matriz, eixo, lambda p: p[eixo] * uni)
    print(matriz)


def reflexaoXouY():
    matriz = entrar()
    eixo = escolher_eixo()
    transformar_eixo(matriz, eixo, lambda p: p[eixo] * -1)
    print(matriz)


def rotacao():
    matriz = entrar()
    rot = float(input("Quanto de rotacao voce vai querer em graus? Exemplo 90 "))
    cos = coseno(rot)
    sen = seno(rot)
    for ponto in matriz:
        novo_x = cos * ponto[0] - sen * ponto[1]
        novo_y = sen * ponto[0] + cos * ponto[1]
        print("[%s, %s]" % (novo_x, novo_y))


def cisalhamento():
    matriz = entrar()
    eixo = escolher_eixo()
    nome = "Y" if eixo == 1 else "X"
    cisa = float(input(f"Quanto de cisalhamento para {nome}? Exemplo 2 "))
    transformar_eixo(matriz, eixo, lambda p: p[eixo] + cisa * p[1 - eixo])
    print(matriz)


def iniciar():
    print("Digite uma dessas opcoes abaixo para : \n")
    print("1 para Dilatação em relação ao eixo x e y ")
    print("2 para Dilatação e relação ao eixo x ou y ")
    print("3 para Reflexão em relação ao eixo x ou y ")
    print("4 para Rotação")
    print("5 para Cisalhamento em relação a x ou a y")

    resultOpcao = int(input("insira sua escolha : "))

    if resultOpcao == 1:
        print("Voce escolheu dilatacao de X e Y ")
        dilatacaoXeY()
    elif resultOpcao == 2:
        print("Voce escolheu dilatacao de X ou Y ")
        dilatacaoXouY()
    elif resultOpcao == 3:
        print("Voce escolheu reflexao de X ou Y ")
        reflexaoXouY()
    elif resultOpcao == 4:
        print("Voce escolheu rotacao ")
        rotacao()
    elif resultOpcao == 5:
        print("Voce escolheu cisalhamento de X ou Y ")
        cisalhamento()
    else:
        print('Voce nao escolheu nenhuma das opcoes,' + '\033[1m' + ' TENTE NOVAMENTE' + '\033[0m')
        return iniciar()


if __name__ == "__main__":
    iniciar()
