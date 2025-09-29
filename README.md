# Pratica1--Algortimos-de-Caminho-Minimo

## Como Executar

1. Clone este repositório:

    ```bash
    git clone https://github.com/LuizDudu25/Pratica1--Algortimos-de-Caminho-Minimo.git
    cd Pratica1--Algortimos-de-Caminho-Minimo
    ```

2. Escolha uma das implementações:

    **Questão 1:**
    ```bash
    cd "Questão_1"
    python questao_1.py
    ```

    **Questão 2:**
    ```bash
    cd "Questão_2"
    python Questao2.py
    ```

    **Questão 3:**
    ```bash
    cd "Questão_3"
    python Q3.py
    ```


## Questão 1
#### Para este problema, escolhemos implementar o algoritmo de Floyd-Warshall, pois ele é ideal para calcular os caminhos mínimos entre todos os pares de vértices em um grafo com pesos positivos. Como o objetivo é encontrar o vértice central da rede de metrô — isto é, a estação cuja soma das distâncias para todas as outras é mínima — precisamos conhecer as menores distâncias entre qualquer par de nós, e Floyd-Warshall resolve exatamente essa necessidade.
#### Não utilizamos Dijkstra porque, embora seja eficiente para calcular caminhos mínimos a partir de uma única origem, seria necessário executá-lo repetidas vezes (uma vez para cada vértice), o que torna o processo menos prático neste caso. Da mesma forma, Bellman-Ford também não é adequado, pois é mais custoso e voltado para grafos com pesos negativos, algo que não ocorre em nosso cenário.
#### Assim, o Floyd-Warshall é a escolha mais apropriada, permitindo construir a matriz de distâncias mínimas entre todas as estações e, a partir dela, identificar a estação central e também a mais distante em relação a ela.
## Questão 2
####Neste problema escolhemos implementar o algoritmo Bellmann-Ford, já que os problemas da questão requerem, principalmente, caminhos mínimos relacionados à um únco vértice (que torna o uso de algoritmos como Floyd-Warshall desnecessários) e abarca arestas de peso tanto negativo quanto positivo (que impossibilita o uso de algoritmos como o Dijkstra). Apesar de não ser o mais otimizado e rápido, é o que melhor se encaixa na probçemática apresentada, além de retornar os vetores de distâncias mínimas e de *backtracking* necessários para a resolução da questão.
## Questão 3
#### Para este questão, escolhemos o algoritmo de Dijkstra, pois não há custos negativos (todos os pesos das arestas são positivos: 1 para corredores livres e 3 para pisos difíceis), e como o problema requer apenas um único caminho mais curto de S para G, este seria o algoritmo mais eficiente. Não escolhemos Bellman-Ford ou Floyd-Warshall porque eles são muito mais lentos que Dijkstra, com complexidades de O(VE) e O(V³) respectivamente, o que se torna particularmente problemático quando o grid representa um grafo muito grande. Além disso, eles são projetados para problemas diferentes: Bellman-Ford para grafos com pesos negativos, e Floyd-Warshall para calcular caminhos mais curtos entre todos os pares de vértices, nenhum dos quais é necessário para o nosso cenário do robô de armazém.

## Equipe:
- Luiz Eduardo Soares Bezerra
- Luiza Bezerra Bastos
- Marco Albuquerque Silva Rocha Gomes
