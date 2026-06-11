import pulp

# 1. Definir el problema (Maximización)
model = pulp.LpProblem("Servicios_virtuales", pulp.LpMaximize)

# 2. Definir Variables (Enteras)
x1 = pulp.LpVariable("Ilustracion", lowBound=0, upBound=6, cat='Integer')
x2 = pulp.LpVariable("Icono", lowBound=0, upBound=7, cat='Integer')

# 3. Función Objetivo
model += 40 * x1 + 20 * x2, "Rendimiento_Total"

# 4. Restricciones
model += 2 * x1 + 1 * x2 <= 12, "Tiempo_diseño"
model += 1 * x1 + 1 * x2 <= 9, "Tiempo_renderizado"

# 5. Resolver y mostrar
model.solve()

print(f"Estado: {pulp.LpStatus[model.status]}")
print(f"Ilustracion: {x1.varValue}")
print(f"Icono: {x2.varValue}")
print(f"Ganancia total: ${pulp.value(model.objective)}")

#source .venv/bin/activate