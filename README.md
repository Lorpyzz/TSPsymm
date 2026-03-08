# Problema do Caixeiro-Viajante(TSP)

## Resumo do Problema:
O código, cujo nome é "autoTSP.py", é uma aproximação de uma "solução" do Problema do Caixeiro-Viajante feita em python.
O problema consiste em passar por todos os pontos, fechando um ciclo voltando do ponto de origem, sem voltar pelas coordenadas passada antes, 
tentando achar um caminho mais curto entre eles.

## Primeiros pensamentos:
Quando foi passado o problema, fiquei analizando como ela poderia ser solucionada, em primeira instância, já sabia que era algo extensivo,
primeira coisa que eu pensei, foi de selecionar 3 caminhos mais curtos em cada ponto, e no final, analizar entre elas para ver qual seria menor,
porém, pensei de forma matemática, e analisei que isso iria crescer de forma exponencial na base 3, resultando num número gigantesco, 
logo notei que isso seria um problema gigantesco para o computador analisar cada caso e ainda verificar entre eles.
Então, pesquisei sobre o problema, mas só foi fazer uma assimilação com um mapa aleatório com pontos definidos, que notei algo,
podemos basicamente pegar o caminho mais curto entre os pontos vizinhos, assim como uma viagem de carro que queremos ir em várias cidades diferentes,
e apliquei essa mesma lógica em python, seguindo com essa ideia ao longo dela.

## Sobre o código:
Partes do código foi feita por Inteligência Artificial, especificamente o Gemini PRO,
seu uso foi feito para verificar quais pontos já foram visitados, isto é, lista de ("visitados"), e sua aplicação no código para organização das casas,
isto é, a função ("organizar_trajeto"), e sua aplicação no final da função ("verificar_vizinho"),
especificamente: linha 50; linha 54-70.
Cada linha de código gerada pela ferramenta foi devidamente verificada, analizada e refinada por mim.

## Lógica utilizada:
A lógica utilizada foi do conceito do vizinho mais próximo, ele parte de um ponto de referência e encontra um ponto mais próximo,
assim sucessivamente até passar por todas as cidades. Basicamente ele calcula a distância entre cada duas coordenadas, depois de calcular,
ele sempre vai para o ponto mais próximo, se repetindo até o final, durante o processo, ele vai somando cada "passo" e armazenando numa variável,
então, quando chegar no ponto de origem, fechando o ciclo, o código acaba.

## Como rodar:
O código não utiliza nenhuma biblioteca além do ".math", o qual já vêm nativo do python.
Portanto, para rodar, é necessário colocar o código "autoTSP.py" dentro de uma mesma pasta com outro arquivo onde tem os pontos, o qual seria o "rat99.tsp"
Feito isso, é necessário apenas debuggar num compilador, e o resultado será dado no terminal.

## Resultado no terminal:
Ele vai printar uma lista com os pontos, organizado em ordem seguindo a lógica citada anteriormente,
além disso, ele vai printar uma distância final percorrida durante todo o trajeto.
Print dado no terminal: "A distancia total é: 1566.40"

## Algumas limitações:
Esse código ele não printa o melhor resultado possível, na verdade, essa lógica minimiza muito do trabalho que o computador faz para chegar num resultado mais satisfatório possível.
Esse problema é completamente extenso, apesar de parecer simples, uma máquina não consegue chegar num resultado "perfeito" de forma rápida,
na verdade, chega a ser impossível com os métodos e a tecnologia de hoje.
Esse código, seguindo naquela lógica, pode ser quer aconteça saltos gigantescos de um ponto para o outro, já que nessa ideia, ele pode fazer pontos mais isolados, aumentando ainda mais a distância somada no final.
Existem outras formas de código na qual aplicam algorítmos de otimização, como o 2-opt, na qual, através do resultado, ele pega linhas que se cruzam entre diferente pontos, e invertem eles de posição, então, faz alguns testes para verificar se o caminho fica mais curto.
Essa otimização é como "destrançar" uma emerado de fios, apenas usando técnica de matemática e lógica, mas ainda assim, fica distante do resultado perfeito.







