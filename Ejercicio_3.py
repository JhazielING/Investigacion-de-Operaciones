
import pulp

# 1. Definir el problema (Minimización)
model = pulp.LpProblem("Cloud_Optimization", pulp.LpMaximize)

# 2. Definir Variables (Enteras, ya que no puedes rentar media instancia)
x1 = pulp.LpVariable("Inspección Básica", lowBound=0, upBound=2, cat='Integer')
x2 = pulp.LpVariable("Inspección Profunda", lowBound=0, upBound=5, cat='Integer')

# 3. Función Objetivo
model += 2 * x1 + 5 * x2, "Seguridad_Total"

# 4. Restricciones
model += x1 * 1 + x2 * 3 <= 18, "Firewall"
model += x1 +  x2 <= 8, "Ram"

# 5. Resolver y mostrar 
model.solve()

print(f"Estado: {pulp.LpStatus[model.status]}")
print(f"Inspeccion Basica: {x1.varValue}")
print(f"Inspeccion Profunda: {x2.varValue}")
print(f"Ganancia Total: ${pulp.value(model.objective)}")

