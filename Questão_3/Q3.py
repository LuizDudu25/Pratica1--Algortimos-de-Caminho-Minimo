import heapq


def carregar_grid(nome_arquivo):
  
    with open(nome_arquivo, "r") as f:
        linhas = f.read().splitlines()

    # primeira linha contém as dimensões
    n_linhas, n_colunas = map(int, linhas[0].split())
    grid = [list(l) for l in linhas[1:]]
    return grid, n_linhas, n_colunas




def vizinhos(i, j, n, m):
    
    movimentos = [(1,0), (-1,0), (0,1), (0,-1)]  # 4 direções
    for di, dj in movimentos:
        ni, nj = i + di, j + dj
        if 0 <= ni < n and 0 <= nj < m:
            yield ni, nj



def custo(c):

    if c in (".", "S", "G"):
        return 1
    elif c == "~":
        return 3
    elif c == "#":
        return None  # obstáculo
    return None



def dijkstra(grid, n, m, inicio, objetivo):

    # Inicialização: distâncias infinitas, exceto a origem
    dist = [[float("inf")] * m for _ in range(n)]
    dist[inicio[0]][inicio[1]] = 0

    # Vetor de predecessores (para reconstrução do caminho)
    pai = [[None] * m for _ in range(n)]

    # Conjunto A representado implicitamente pela fila de prioridade
    fila = [(0, inicio)]  # (distância acumulada, célula)

    while fila:
        d, (i, j) = heapq.heappop(fila)

        # Se chegamos ao objetivo, pode parar
        if (i, j) == objetivo:
            break

        # Se já encontramos caminho melhor, ignora
        if d > dist[i][j]:
            continue

        # Relaxamento das arestas (vizinhos)
        for ni, nj in vizinhos(i, j, n, m):
            custo_celula = custo(grid[ni][nj])
            if custo_celula is None:  # obstáculo
                continue

            novo_custo = dist[i][j] + custo_celula
            if novo_custo < dist[ni][nj]:
                dist[ni][nj] = novo_custo
                pai[ni][nj] = (i, j)
                heapq.heappush(fila, (novo_custo, (ni, nj)))

    # Reconstrução do caminho
    caminho = []
    atual = objetivo
    if dist[objetivo[0]][objetivo[1]] != float("inf"):
        while atual:
            caminho.append(atual)
            atual = pai[atual[0]][atual[1]]
        caminho.reverse()

    return dist[objetivo[0]][objetivo[1]], caminho


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
