import pandas as pd
from ImplementacoesGrafosPython import GraphAdjMatrix as GMatrix

def printMatrix(matrix, k):
    n=len(matrix[0])-1 #considerando matriz quadrada, considerando grafo com tamanho (0, N+1)
    for i in range(k, n+k):
        print(matrix[i][k: n+k])

def sumRow(row):
    result=0
    for i in range(0, len(row)):
        result+=row[i]
    return result

def floydAlgorithm(graph, IR, nodesN):
    # Criar matrizes D e R com tamanho adequado
    D = [[float('inf')] * (nodesN + IR + 1) for _ in range(nodesN + IR + 1)]
    R = [[0] * (nodesN + IR + 1) for _ in range(nodesN + IR + 1)]
    
    # Inicialização das matrizes
    for i in range(IR, IR + nodesN):
        for j in range(IR, IR + nodesN):
            if i == j:
                D[i][j] = 0
                R[i][j] = i  # ou pode ser 0, dependendo da convenção
            elif graph.M[i][j] != 0:
                D[i][j] = graph.M[i][j]
                R[i][j] = j
    
    # Algoritmo de Floyd-Warshall
    for k in range(IR, IR + nodesN):
        for i in range(IR, IR + nodesN):
            for j in range(IR, IR + nodesN):
                if D[i][k] + D[k][j] < D[i][j]:
                    D[i][j] = D[i][k] + D[k][j]
                    R[i][j] = R[i][k]
    
    return D, R

if __name__== "__main__":

    Input=[]
    with open("graph1.txt", 'r') as input:
        for line in input:
            final_Line=line.strip("\n").split("\t")
            Input.append(final_Line)
    input_graph=pd.DataFrame(Input)

    nodesN=int(input_graph.iloc[0,0])
    edgesM=int(input_graph.iloc[0,1])
    initialNode=input_graph.iloc[1:edgesM+1, 0].astype(int).to_list()
    finalNode=input_graph.iloc[1:edgesM+1, 1].astype(int).to_list()
    costNode=input_graph.iloc[1:edgesM+1, 2].astype(int).to_list()
    k=min(min(initialNode), min(finalNode)) #primeiro nó (considerando que os vértices seguem uma ordem crescente) #referência de vértice e intervalo

    graph=GMatrix(nodesN)
    for i in range (0, edgesM):
        graph.addEdge(initialNode[i], finalNode[i], costNode[i])
    
    D, R = floydAlgorithm(graph, k)

    nodeSum=[]
    for i in range(k, nodesN+k):
        nodeSum.append(sumRow(D[i]))

    centralNode=nodeSum.index(min(nodeSum))+k #nó central
    centralNode_distanceList=D[centralNode][k: nodesN+k] #vetor de distâncias em relação ao central
    mostDistantNode=centralNode_distanceList.index(max(centralNode_distanceList))+k #vértice mais longe do central
    
    #respostas:
    print(f"Pela matriz dada:\n   Nó escolhido como central: {centralNode}\n   Distâncias em relação ao nó central: {centralNode_distanceList}\n   Vértice mais distante do central: {mostDistantNode}\n   Matriz com nós cadidatos e distâncias mínimas (Matriz de distâncias): ")
    printMatrix(D, k)
