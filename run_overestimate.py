import search

# Definimos la clase aquí para que esté disponible
class WeightedGPSProblem(search.GPSProblem):
    def h(self, node):
        # Heurística multiplicada por 4 para forzar sobreestimación
        return super().h(node) * 4

def demo_overestimation():
    print(f"{'='*60}")
    print("DEMOSTRACIÓN: HEURÍSTICA QUE SOBREESTIMA (FACTOR x4)")
    print(f"{'='*60}")

    # 1. Resolvemos con A* NORMAL
    print("\n1. Ejecución con A* Normal (h original):")
    problem_good = search.GPSProblem('A', 'B', search.romania)
    # Nota: graph_search ya imprime los detalles (Generados, Visitados, etc.)
    res_good = search.branch_and_bound_with_heuristic_graph_search(problem_good)

    # 2. Resolvemos con A* SOBREESTIMADO
    print("\n2. Ejecución con Heurística Multiplicada por 4:")
    problem_bad = WeightedGPSProblem('A', 'B', search.romania)
    res_bad = search.branch_and_bound_with_heuristic_graph_search(problem_bad)

    print("\n--- CONCLUSIÓN DE LA COMPARATIVA ---")
    if res_good and res_bad:
        if res_bad.path_cost > res_good.path_cost:
            print("¡ÉXITO! Al multiplicar h(n) por 4, el algoritmo perdió la optimidad.")
            print(f"Coste Óptimo (A* Normal): {res_good.path_cost}")
            print(f"Coste Encontrado (A* Sobreestimado): {res_bad.path_cost}")
        else:
            print("Ambos encontraron el mismo coste en este caso.")
    else:
        print("No se encontraron soluciones para comparar.")

# Esto permite probar este fichero individualmente
if __name__ == "__main__":
    demo_overestimation()