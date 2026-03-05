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

linhas = ler_arqTSP("rat99.tsp")
pontos = extrair_coordenadas(linhas)
print(pontos)