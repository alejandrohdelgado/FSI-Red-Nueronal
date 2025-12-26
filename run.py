'''# Search methods

import search

ab = search.GPSProblem('A', 'B'
                       , search.romania)

print(search.breadth_first_graph_search(ab))
print(search.depth_first_graph_search(ab))
print(search.branch_and_bound_graph_search(ab))
print(search.branch_and_bound_with_heuristic_graph_search(ab))

# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
'''


import search
import time
# Importamos tus otros modulos para llamar a sus funciones
import run_trace
import run_overestimate

# =============================================================================
# PARTE OBLIGATORIA: GENERACIÓN DE DATOS PARA LA TABLA
# =============================================================================

# Escenarios de la tabla
scenarios = [
    {"id": 1, "orig_name": "Arad",    "dest_name": "Bucharest", "orig": 'A', "dest": 'B'},
    {"id": 2, "orig_name": "Oradea",  "dest_name": "Eforie",    "orig": 'O', "dest": 'E'},
    {"id": 3, "orig_name": "Giurgiu", "dest_name": "Zerind",    "orig": 'G', "dest": 'Z'},
    {"id": 4, "orig_name": "Neamt",   "dest_name": "Dobreta",   "orig": 'N', "dest": 'D'},
    {"id": 5, "orig_name": "Mehadia", "dest_name": "Fagaras",   "orig": 'M', "dest": 'F'},
]

algorithms = [
    ("Amplitud", search.breadth_first_graph_search),
    ("Profundidad", search.depth_first_graph_search),
    ("Ramificación y Acotación", search.branch_and_bound_graph_search),
    ("Ramif. con Subestimación (A*)", search.branch_and_bound_with_heuristic_graph_search)
]

print(f"{'='*80}")
print(f"PARTE OBLIGATORIA: DATOS PARA LA TABLA")
print(f"{'='*80}")

for sc in scenarios:
    print(f"\n\n{'#'*80}")
    print(f"ID {sc['id']}: {sc['orig_name']} -> {sc['dest_name']}")
    print(f"{'#'*80}")
    
    problem = search.GPSProblem(sc['orig'], sc['dest'], search.romania)
    
    for algo_name, algo_func in algorithms:
        print(f"\n--- COLUMNA: {algo_name} ---")
        # graph_search en search.py imprime: Generados, Visitados, Coste, Ruta
        result = algo_func(problem)
        if not result:
            print("(!) No se encontró solución.")

# =============================================================================
# PARTE 1 OPCIONAL: LLAMADA A RUN_TRACE
# =============================================================================
print(f"\n\n{'='*80}")
print("PARTE 1 OPCIONAL: TRAZA MANUAL (Llamando a run_trace.py)")
print(f"{'='*80}")

# Creamos el problema Arad->Bucharest y llamamos a la función importada
p_manual = search.GPSProblem('A', 'B', search.romania)
run_trace.trace_branch_and_bound(p_manual)

# =============================================================================
# PARTE 2 OPCIONAL: LLAMADA A RUN_OVERESTIMATE
# =============================================================================
print(f"\n\n{'='*80}")
print("PARTE 2 OPCIONAL: HEURÍSTICA SOBREESTIMADA (Llamando a run_overestimate.py)")
print(f"{'='*80}")

# Llamamos a la función de demostración importada
run_overestimate.demo_overestimation()

print(f"\n\n{'='*80}")
print("FIN DE LA EJECUCIÓN GLOBAL")
print(f"{'='*80}")