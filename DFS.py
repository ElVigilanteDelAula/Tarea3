pesoObjeto = [3, 4, 5, 2, 1]
beneficioObjeto = [4, 5, 6, 3, 2]
capacidadMochila = 10

def evaluate(solution):
    total_weight = sum(pesoObjeto[i] for i in range(len(solution)) if solution[i])
    if total_weight > capacidadMochila:
        return -float("inf")
    total_value = sum(beneficioObjeto[i] for i in range(len(solution)) if solution[i])
    return total_value

def dfs(depth, current_weight, current_value, solution):
    global best_solution, best_value
    if depth == len(pesoObjeto):
        if current_value > best_value:
            best_solution = solution.copy()
            best_value = current_value
        return
    if current_weight + pesoObjeto[depth] <= capacidadMochila:
        solution[depth] = 1
        dfs(depth+1, current_weight+pesoObjeto[depth], current_value+beneficioObjeto[depth], solution)
    solution[depth] = 0
    dfs(depth+1, current_weight, current_value, solution)

best_solution = None
best_value = -float("inf")
dfs(0, 0, 0, [0]*len(pesoObjeto))
print("Solución encontrada:")
print(best_solution)
print("Valor total de los elementos seleccionados:", best_value)
