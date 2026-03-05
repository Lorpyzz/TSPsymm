import math

def ler_arqTSP(arq):
    arquivo = open(arq, 'r')
    linhas = arquivo.readlines()
    arquivo.close()
    return linhas

def extrair_coordenadas(linhas):
    lista_pontos = []

    for i in range(6, len(linhas)-1):
        #as coordenadas começam da linha 7
        #tirando tambem a ultima linha "EOF"
        linha_atual = linhas[i].strip()
        partes = linha_atual.split()
        lista_pontos.append(partes)

    return lista_pontos

def calcular_distancia(x1,y1,x2,y2):
    delta_x = x2 - x1
    delta_y = y2 - y1

    distancia = math.sqrt(delta_x**2 + delta_y**2)
    #fazendo pitágoras para achar uma distancia (hipotenusa) entre dois pontos

    return distancia

def verificar_vizinho(ponto_referencia, lista_pontos, visitados):
    menor_distancia = 999999
    pos_visitado = -1

    #coordenada do ponto que teremos como referencial para medir a distancia
    x_ref = ponto_referencia[1]
    y_ref = ponto_referencia[2]

    for i in range(len(lista_pontos)):

        if visitados[i] == False:
            #isto é, se não foi visitado (False), ele vai armazenar o menor valor, fazendo testes com os nao visitados restantes
            x_comparado = lista_pontos[i][1]
            y_comparado = lista_pontos[i][2]

            distancia = calcular_distancia(int(x_ref),int(y_ref), int(x_comparado), int(y_comparado))

            if distancia > 0 and distancia < menor_distancia:
                #maior que zero, pois ele vai fazer testes com todos os pontos, inclusive ele mesmo, isso evita dele armazenar a distancia nula
                menor_distancia = distancia
                pos_visitado = i
    
    return pos_visitado

# #teste para distancia
# linhas = ler_arqTSP("rat99.tsp")
# pontos = extrair_coordenadas(linhas)

# distancia = calcular_distancia(int(pontos[0][1]),int(pontos[0][2]),int(pontos[1][1]),int(pontos[1][2]))
# print(distancia)
# #resultado = 14.212670, verificado e certa resposta
