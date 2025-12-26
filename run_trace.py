import search

def trace_branch_and_bound(problem):
    """
    Simula la ejecución paso a paso imprimiendo la frontera.
    """
    print(f"\n--- TRAZA PASO A PASO: {problem.initial} -> {problem.goal} ---")
    
    # Cola de prioridad ordenada por coste (g)
    fringe = search.PriorityQueue(lambda n: n.path_cost)
    fringe.append(search.Node(problem.initial))
    
    iteration = 0
    closed = set()
    
    while fringe:
        iteration += 1
        
        # 1. Mostrar estado de la frontera ANTES de sacar el nodo
        contenido_cola = [(n.state, n.path_cost) for n in fringe.A]
        print(f"\nITERACIÓN {iteration}:")
        print(f"  Frontera (Nodos pendientes ordenados por coste): {contenido_cola}")
        
        # 2. Sacar el mejor nodo
        node = fringe.pop()
        print(f"  -> Seleccionado para expandir: {node.state} (Coste acumulado g={node.path_cost})")
        
        if problem.goal_test(node.state):
            print(f"\n¡OBJETIVO ALCANZADO! Ruta final: {node.path()}")
            return node
            
        if node.state not in closed:
            closed.add(node.state)
            
            # 3. Expandir hijos
            children = node.expand(problem)
            hijos_info = [(c.state, c.path_cost) for c in children]
            print(f"     Hijos generados: {hijos_info}")
            fringe.extend(children)
        else:
            print("     (Nodo ya visitado, se descarta)")
            
        if iteration >= 10: 
            print("\n... (Detenemos la traza detallada tras 10 iteraciones) ...")
            break

# Esto permite probar este fichero individualmente sin romper el run.py principal
if __name__ == "__main__":
    problem = search.GPSProblem('A', 'B', search.romania)
    trace_branch_and_bound(problem)