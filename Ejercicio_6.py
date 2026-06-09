import pulp

# 1. Definir el problema (Minimización)
model = pulp.LpProblem("Optimizacion_Almacenamiento_Cloud", pulp.LpMinimize)

# 2. Definir Variables (TB de almacenamiento)
x1 = pulp.LpVariable("Almacenamiento_Estandar", lowBound=0, cat='Integer')
x2 = pulp.LpVariable("Almacenamiento_Premium", lowBound=0, cat='Integer')

# 3. Función Objetivo
model += 20 * x1 + 60 * x2, "Costo_Total_Mensual"

# 4. Restricciones

# Capacidad de Lectura Rápida (IOPS)
model += 1 * x1 + 3 * x2 >= 15, "Velocidad_IOPS"

# Días de Retención
model += 2 * x1 + 2 * x2 >= 14, "Retencion_Datos"

# 5. Resolver y mostrar resultados
model.solve()

print(f"Estado: {pulp.LpStatus[model.status]}")
print(f"TB de Almacenamiento Estándar: {x1.varValue}")
print(f"TB de Almacenamiento Premium: {x2.varValue}")
print(f"Costo Minimo Mensual: ${pulp.value(model.objective)} USD")