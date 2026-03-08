# Problema do Caixeiro-Viajante(TSP)

## Resumo do Problema:
O código, cujo nome é "autoTSP.py", é uma aproximação de uma "solução" do Problema do Caixeiro-Viajante feita em python.
O problema consiste em passar por todos os pontos, fechando um ciclo voltando do ponto de origem, sem voltar pelas coordenadas passada antes, 
tentando achar um caminho mais curto entre eles.

## Lógica utilizada
A lógica utilizada foi do conceito do vizinho mais próximo, ele parte de um ponto de referência e encontra um ponto mais próximo,
assim sucessivamente até passar por todas as cidades. Basicamente ele calcula a distância entre cada duas coordenadas, depois de calcular,
ele sempre vai para o ponto mais próximo, se repetindo até o final, durante o processo, ele vai somando cada "passo" e armazenando numa variável,
então, quando chegar no ponto de origem, fechando o ciclo, o código acaba.

## Como rodar:
O código não utiliza nenhuma biblioteca além do ".math", o qual já vêm nativo do python.
Portanto, para rodar, é necessário colocar o código "autoTSP.py" dentro de uma mesma pasta com outro arquivo onde tem os pontos, o qual seria o "rat99.tsp"
Feito isso, é necessário apenas debuggar num compilador, e o resultado será dado no terminal.

## Resultado no terminal:





