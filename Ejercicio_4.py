import pulp

# 1. Definir el problema (Maximización)
model = pulp.LpProblem("Cloud_Optimization", pulp.LpMaximize)

# 2. Definir Variables (Enteras)
x1 = pulp.LpVariable("Server_Blade_Estandar", lowBound=0, upBound=24, cat='Integer')
x2 = pulp.LpVariable("Server_Rack_Pro", lowBound=2, upBound=8, cat='Integer')

# 3. Función Objetivo
model += 10000 * x1 + 25000 * x2, "EPS_Total"

# 4. Restricciones
model += 1500 * x1 + 4000 * x2 <= 30000, "Presupuesto"
model += 1 * x1 + 3 * x2 <= 24, "Rack"
model += 2 * x1 + 5 * x2 <= 45, "Energia"

# 5. Resolver y mostrar
model.solve()

print(f"Estado: {pulp.LpStatus[model.status]}")
print(f"Servers Blade Estandar: {x1.varValue}")
print(f"Servers Rack Pro: {x2.varValue}")
print(f"Capacidad Maxima EPS: {pulp.value(model.objective)}")

#source .venv/bin/activate