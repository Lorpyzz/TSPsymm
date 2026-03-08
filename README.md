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



