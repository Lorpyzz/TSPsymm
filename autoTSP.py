def ler_arqTSP(arq):
    arquivo = open(arq, 'r')
    linhas = arquivo.readlines()
    arquivo.close()
    return linhas

arquivo = ler_arqTSP("rat99.tsp")
print(arquivo)

#botamos esse arquivo dentro do programa, transformando nele em uma enorme lista com toda informação