import heapq


# Carrega o grid do arquivo

def carregar_grid(nome_arquivo):
    with open(nome_arquivo, "r") as f:
        linhas = f.read().splitlines()

    n_linhas, n_colunas = map(int, linhas[0].split())
    grid = [list(l) for l in linhas[1:]]
    return grid, n_linhas, n_colunas



# Função que retorna vizinhos válidos (N, S, L, O)

def vizinhos(i, j, n, m):
    movimentos = [(1,0), (-1,0), (0,1), (0,-1)]
    for di, dj in movimentos:
        ni, nj = i + di, j + dj
        if 0 <= ni < n and 0 <= nj < m:
            yield ni, nj



# Define custo de cada célula

def custo(c):
    if c in (".", "S", "G"):
        return 1
    elif c == "~":
        return 3
    elif c == "#":
        return None  # obstáculo
    return None



# Algoritmo de Dijkstra

def dijkstra(grid, n, m, inicio, objetivo):
   
    # PSEUDOCÓDIGO: d_11 ← 0; d_1i ← ∞ ∀ i ∈ V - {1}
  
    dist = [[float("inf")] * m for _ in range(n)]
    dist[inicio[0]][inicio[1]] = 0

   
    # PSEUDOCÓDIGO: anterior(i) ← 0 ∀ i
 
    pai = [[None] * m for _ in range(n)]

 
    # PSEUDOCÓDIGO: A ← V ; F ← ∅
    # Aqui usamos uma fila de prioridade (heapq) como conjunto A implícito
 
    fila = [(0, inicio)]  # (distância acumulada, célula)

  
    # PSEUDOCÓDIGO: enquanto A ≠ ∅ faça
   
    while fila:
       
        # PSEUDOCÓDIGO: r ← v ∈ V | d_1r = min[d_1j]
        # Aqui: extrai o nó com menor distância
       
        d, (i, j) = heapq.heappop(fila)

        # Se já chegamos ao objetivo, podemos parar
        if (i, j) == objetivo:
            break

        # Ignora se já existe distância melhor (equivale a não reprocessar F)
        if d > dist[i][j]:
            continue

       
        # PSEUDOCÓDIGO: S ← A ∩ N*(r)
        # Para cada vizinho i de r ainda aberto
       
        for ni, nj in vizinhos(i, j, n, m):
            custo_celula = custo(grid[ni][nj])
            if custo_celula is None:  # obstáculo
                continue

            
            # PSEUDOCÓDIGO: p ← min[d_1i, (d_1r + v_ri)]
            # Aqui: calculamos o custo alternativo pelo nó atual
            
            novo_custo = dist[i][j] + custo_celula

            
            # PSEUDOCÓDIGO: se p < d_1i então
            # Atualiza distância e "anterior(i)"
            
            if novo_custo < dist[ni][nj]:
                dist[ni][nj] = novo_custo
                pai[ni][nj] = (i, j)   # anterior(i) ← r
                heapq.heappush(fila, (novo_custo, (ni, nj)))

   
    # Reconstrução do caminho (usando anterior(i))
    caminho = []
    atual = objetivo
    if dist[objetivo[0]][objetivo[1]] != float("inf"):
        while atual:
            caminho.append(atual)
            atual = pai[atual[0]][atual[1]]
        caminho.reverse()

    return dist[objetivo[0]][objetivo[1]], caminho



# Programa principal
if __name__ == "__main__":
    grid, n, m = carregar_grid("grid_example.txt")

    # localizar S e G
    inicio = objetivo = None
    for i in range(n):
        for j in range(m):
            if grid[i][j] == "S":
                inicio = (i, j)
            elif grid[i][j] == "G":
                objetivo = (i, j)

    distancia, caminho = dijkstra(grid, n, m, inicio, objetivo)

    print("Custo mínimo:", distancia)
    print("Caminho encontrado:", caminho)

    # marcar o caminho no grid para visualizar
    for (i, j) in caminho:
        if grid[i][j] not in ("S", "G"):
            grid[i][j] = "*"

    print("\nGrid com caminho:")
    for linha in grid:
        print("".join(linha))
