import pulp

# 1. Definir el problema (Maximización)
model = pulp.LpProblem("Servicios_virtuales", pulp.LpMaximize)

# 2. Definir Variables (Enteras)
x1 = pulp.LpVariable("Servidor_basico", lowBound=0, upBound=6, cat='Integer')
x2 = pulp.LpVariable("Servidor_avanzado", lowBound=0, upBound=7, cat='Integer')

# 3. Función Objetivo
model += 30 * x1 + 50 * x2, "Rendimiento_Total"

# 4. Restricciones
model += 1 * x1 + 2 * x2 <= 16, "Capacidad_memoria_ram"
model += 3 * x1 + 2 * x2 <= 24, "Nucleos_procesador"

# 5. Resolver y mostrar
model.solve()

print(f"Estado: {pulp.LpStatus[model.status]}")
print(f"Servidor basico: {x1.varValue}")
print(f"Servidor avanzado: {x2.varValue}")
print(f"Ganancia total: ${pulp.value(model.objective)}")

#source .venv/bin/activate