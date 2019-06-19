import math
def converterGrausParaRad(numero):
    rad = (numero/180)*math.pi
    return rad
    

def seno(numero):
    resultado = 0
    resultado = math.sqrt(1 - (coseno(numero))**2)
    return resultado


def coseno(rad):
    numero = converterGrausParaRad(rad)
    cont = 0
    resultado = 1 
    while(cont < 50):
        cont += 1
        resultado += (((-1)**cont)*(numero**(2 * cont)))/(math.factorial(2 * cont))

    return round(resultado, 6) 

def entrar():
    linha = [ ] 
    mat = [ ] 
    matriz = int (input ('Entre com quantos (x,y) voce deseja. Exemplo (x,y), (x,y) entre com 2: ')) 
    for i in range (matriz): 
        for ii in range (2): 
            linha.append (float(input('Entre com a variavel: '))) 
        mat.append(linha)
        linha = [ ]
    print("Voce escoheu esses x e y: ") 
    print(mat)
    return mat

def dilatacaoXeY():
    matriz = []
    matriz = entrar()
    uni = float(input("Quantas unidades para X e Y? Exemplo: 1 ou -1"))
    for i in range(len(matriz)):
        result = matriz[i][1] + uni
        matriz[i].pop()
        matriz[i].append(result)

    for i in range(len(matriz)):
        resultX = matriz[i][0] + uni
        y = matriz[i].pop() #y
        matriz[i].pop() #x
        matriz[i].append(resultX)
        matriz[i].append(y)
    
    print(matriz)

def dilatacaoXouY():
    matriz = []
    matriz = entrar()
    xouy = input("Voce quer alterar X ou Y?")
    if xouy == "Y" or xouy == "y" :
        uni = float(input("Quantas unidades para Y? Exemplo: 1 ou -1"))   
        for i in range(len(matriz)):
            result = matriz[i][1] + uni
            matriz[i].pop()
            matriz[i].append(result)
    
    elif xouy == "X" or xouy == "x" :
        uni = float(input("Quantas unidades para X? Exemplo: 1 ou -1"))
        for i in range(len(matriz)):
            resultX = matriz[i][0] + uni
            y = matriz[i].pop() #y
            matriz[i].pop() #x
            matriz[i].append(resultX)
            matriz[i].append(y)
    else:
        print('Voce nao escolheu X ou Y'+'\033[1m' + ' TENTE NOVAMENTE DO COMECO' + '\033[0m')
        return dilatacaoXouY()
    print(matriz)

def reflexaoXouY():
    matriz = []
    matriz = entrar()
    xouy = input("Voce quer alterar X ou Y?")
    
    if xouy == "Y" or xouy == "y" :
         for i in range(len(matriz)):
            result = matriz[i][1] * -1
            matriz[i].pop()
            matriz[i].append(result)
    
    elif xouy == "X" or xouy == "x" :
        for i in range(len(matriz)):
            result = matriz[i][0] * -1
            y = matriz[i].pop() #y
            matriz[i].pop() #x
            matriz[i].append(result)
            matriz[i].append(y)
    else:
        print('Voce nao escolheu X ou Y'+'\033[1m' + ' TENTE NOVAMENTE DO COMECO' + '\033[0m')
        return reflexaoXouY()

    print(matriz)

def rotacao():
    matriz = []
    matriz = entrar()
    rot = float(input("Quanto de rotacao voce vai querer em graus? Exemplo 90 "))
    cos = coseno(rot)
    sen = seno(rot)
    formula = [[cos, -(sen)], [sen, cos]]
    for i in range(len(matriz)):
        calc1 = (formula[0][0] * matriz[i][0]) + (formula[0][1] * matriz[i][1])
        calc2 = (formula[1][0] * matriz[i][0]) + (formula[1][1] * matriz[i][1]) 
        print("[%s, %s]"%(calc1, calc2)) 

def cisalhamento():
    matriz = []
    matriz = entrar()
    xouy = input("Voce quer alterar X ou Y?")

    if xouy == "Y" or xouy == "y" :
        cisa = float(input("Quanto de cisalhamento para Y? Exemplo 2 "))
        for i in range(len(matriz)):
            result = matriz[i][1] + (cisa * matriz[i][0])
            matriz[i].pop() 
            matriz[i].append(result)
    
    elif xouy == "X" or xouy == "x" :
        cisa = float(input("Quanto de cisalhamento para X? Exemplo 2 "))
        for i in range(len(matriz)):
            result = matriz[i][0] + (cisa * matriz[i][1])
            y = matriz[i].pop() #y
            matriz[i].pop() #x
            matriz[i].append(result)
            matriz[i].append(y)
    else:    
        print('Voce nao escolheu X ou Y'+'\033[1m' + ' TENTE NOVAMENTE DO COMECO' + '\033[0m')
        return cisalhamento()
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
        print('Voce nao escolheu nenhuma das opcoes,'+'\033[1m' + ' TENTE NOVAMENTE' + '\033[0m')
        return iniciar()
        
iniciar()