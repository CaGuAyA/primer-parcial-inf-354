import itertools

# Definir el grafo como una lista de adyacencia
grafo = {
    'A': {'B': 2, 'C': 3, 'D': 4},
    'B': {'A': 2, 'C': 5, 'D': 6},
    'C': {'A': 3, 'B': 5, 'D': 7},
    'D': {'A': 4, 'B': 6, 'C': 7}
}

# Obtener todos los nodos del grafo
nodos = list(grafo.keys())

# Obtener todas las permutaciones de los nodos
permutaciones = itertools.permutations(nodos)

# Filtrar las permutaciones para asegurarse de que cada nodo aparezca una vez en cada camino
caminos = []
for perm in permutaciones:
    if all(perm[i] in grafo[perm[i-1]] for i in range(1, len(perm))):
        caminos.append(perm)

# Imprimir todos los caminos
for camino in caminos:
    print('->'.join(camino))
