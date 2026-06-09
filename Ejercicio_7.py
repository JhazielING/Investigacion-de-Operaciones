import pulp

# 1. Definir el problema (Maximización)
model = pulp.LpProblem("Optimizacion_Assets_Videojuego", pulp.LpMaximize)

# 2. Definir Variables
x1 = pulp.LpVariable("Personajes_3D", lowBound=0, cat='Integer')
x2 = pulp.LpVariable("Escenarios_3D", lowBound=0, cat='Integer')

# 3. Función Objetivo
model += 80 * x1 + 60 * x2, "Valor_Total_Proyecto"

# 4. Restricciones

# Tiempo de Renderizado (GPU)
model += 2 * x1 + 1 * x2 <= 12, "Tiempo_Render"

# Memoria de Video (VRAM)
model += 1 * x1 + 2 * x2 <= 14, "Uso_VRAM"

# 5. Resolver y mostrar resultados
model.solve()

print(f"Estado: {pulp.LpStatus[model.status]}")
print(f"Cantidad de Personajes 3D: {x1.varValue}")
print(f"Cantidad de Escenarios 3D: {x2.varValue}")
print(f"Valor Máximo del Proyecto: ${pulp.value(model.objective)} USD")