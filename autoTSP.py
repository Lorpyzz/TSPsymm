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

#teste para distancia
linhas = ler_arqTSP("rat99.tsp")
pontos = extrair_coordenadas(linhas)

distancia = calcular_distancia(int(pontos[0][1]),int(pontos[0][2]),int(pontos[1][1]),int(pontos[1][2]))
print(distancia)
#resultado = 14.212670, verificado e certa resposta
