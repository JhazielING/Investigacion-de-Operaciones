import heapq

def dijkstra(grafo, inicio, destino):
    distancias = {nodo: float('inf') for nodo in grafo}
    distancias[inicio] = 0

    procedentes = {nodo: None for nodo in grafo}

    cola_prioridad = [(0, inicio)]

    print("EVOLUCIÓN DEL ALGORITMO DE DIJKSTRA\n")

    while cola_prioridad:
        distancia_actual, nodo_actual = heapq.heappop(cola_prioridad)

        if distancia_actual > distancias[nodo_actual]:
            continue

        # Etiqueta permanente
        print(f"Se hace permanente el nodo: {nodo_actual} ({distancia_actual} km)")

        if nodo_actual == destino:
            break

        for vecino, peso in grafo[nodo_actual].items():
            distancia_nueva = distancia_actual + peso

            if distancia_nueva < distancias[vecino]:
                distancias[vecino] = distancia_nueva
                procedentes[vecino] = nodo_actual
                heapq.heappush(cola_prioridad, (distancia_nueva, vecino))

                # Etiqueta temporal
                print(f"  {vecino} = {distancia_nueva} km (desde {nodo_actual})")

        print("Etiquetas actuales:")
        for nodo in grafo:
            if distancias[nodo] == float('inf'):
                print(f"  {nodo}: ∞")
            else:
                print(f"  {nodo}: {distancias[nodo]} km")
        print("-" * 40)

    # Reconstrucción de la ruta
    ruta = []
    nodo_rastreo = destino

    while nodo_rastreo is not None:
        ruta.insert(0, nodo_rastreo)
        nodo_rastreo = procedentes[nodo_rastreo]

    return distancias[destino], ruta


# Grafo del ejercicio
grafo_red = {
    'A': {'B': 3, 'C': 6},
    'B': {'C': 2, 'D': 8},
    'C': {'D': 4, 'E': 7},
    'D': {'E': 1, 'F': 5},
    'E': {'F': 3, 'G': 8},
    'F': {'G': 2},
    'G': {}
}

origen = 'A'
fin = 'G'

distancia_minima, ruta_optima = dijkstra(grafo_red, origen, fin)

print("\nRESULTADO DEL ALGORITMO DE DIJKSTRA")
print("------------------------------------")
print(f"Ruta óptima: {' -> '.join(ruta_optima)}")
print(f"Distancia mínima total: {distancia_minima} km")