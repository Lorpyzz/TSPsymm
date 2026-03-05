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


def organizar_trajeto(lista_pontos):
    visitados = [False] * len(lista_pontos)
    caminho_final = []
    pos_atual = 0

    for i in range(len(lista_pontos)):
        #ou seja, vamos começar no ponto 0, e cada cidade vizinha visitada, vai mudar de False para True
        casa_atual = lista_pontos[pos_atual]
        caminho_final.append(casa_atual)
        visitados[pos_atual] = True

        #print(visitados) #ver a lista sendo preenchida
        #print()
        prox_pos = verificar_vizinho(casa_atual, lista_pontos, visitados)
        pos_atual = prox_pos
    
    return caminho_final


linhas = ler_arqTSP("rat99.tsp")
pontos = extrair_coordenadas(linhas)
caminho_final = organizar_trajeto(pontos)
print(caminho_final)

#tendo a lista organizada, so falta pegar a distancia dos pontos entre cada um deles e somar
#a ideia inicial até agora foi de simplesmente fazer com que a lista inical, resjustasse para os vizinho mais proximo, na ordem



