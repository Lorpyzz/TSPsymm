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

def calcular_distancia_total(caminho_final):
    distancia_total = 0
    for i in range(len(caminho_final)-1):
        #como estamos lidando em diferença entre dois pontos, subtrai um, já que o último vai ser o ponto final, caso contrario, faria uma distancia com algo que está out of range
        x1 = float(caminho_final[i][1])
        y1 = float(caminho_final[i][2])
        x2 = float(caminho_final[i+1][1])
        y2 = float(caminho_final[i+1][2])
        
        distancia = calcular_distancia(x1,y1,x2,y2)
        distancia_total += distancia
    
    #depois de ver os testes vendo as listas do visitado, como a primeira casa estava sendo marcada como True(já que é o ponto de partida), a ultima casa não fechava o ciclo de volta para o primeiro
    #isto é, necessitamos ainda somar a distancia entre o ultimo ponto da lista organizada e o primeiro ponto da lista
    ultimo_x = float(caminho_final[-1][1])
    ultimo_y = float(caminho_final[-1][2])
    prim_x = float(caminho_final[0][2])
    prim_y = float(caminho_final[0][2])
    distancia_total += calcular_distancia(ultimo_x,ultimo_y,prim_x,prim_y)
    
    return distancia_total


linhas = ler_arqTSP("rat99.tsp")
pontos = extrair_coordenadas(linhas)
caminho_final = organizar_trajeto(pontos)
distancia_total = calcular_distancia_total(caminho_final)
print(caminho_final)
print()
print(f'A distancia total é: {distancia_total:.2f}')





