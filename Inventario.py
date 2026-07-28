import math
import matplotlib.pyplot as plt
import numpy as np

def resolver_eoq(D, S, H, C, dias_laborables, lead_time):
    # Cálculo del EOQ
    Q_optimo = math.sqrt((2 * D * S) / H)

    # Número de pedidos al año
    N_pedidos = D / Q_optimo

    # Tiempo entre pedidos
    tiempo_entre_pedidos = dias_laborables / N_pedidos

    # Demanda diaria
    demanda_diaria = D / dias_laborables

    # Punto de reorden
    rop = demanda_diaria * lead_time

    # Costos
    costo_compra = D * C
    costo_ordenar = (D / Q_optimo) * S
    costo_mantener = (Q_optimo / 2) * H
    costo_total = costo_compra + costo_ordenar + costo_mantener

    # Resultados
    print("=" * 45)
    print("      RESULTADOS DEL MODELO EOQ")
    print("=" * 45)
    print(f"Demanda anual (D): {D} unidades")
    print(f"Costo por pedido (S): ${S:.2f} USD")
    print(f"Costo de mantener (H): ${H:.2f} USD/unidad")
    print(f"Costo unitario (C): ${C:.2f} USD")
    print("-" * 45)
    print(f"Cantidad Económica de Pedido (EOQ): {Q_optimo:.2f} unidades")
    print(f"Número de pedidos al año: {N_pedidos:.2f}")
    print(f"Tiempo entre pedidos: {tiempo_entre_pedidos:.2f} días")
    print(f"Demanda diaria: {demanda_diaria:.2f} unidades")
    print(f"Punto de Reorden (ROP): {rop:.2f} unidades")
    print("-" * 45)
    print(f"Costo anual de compra: ${costo_compra:,.2f} USD")
    print(f"Costo anual de ordenar: ${costo_ordenar:,.2f} USD")
    print(f"Costo anual de mantener: ${costo_mantener:,.2f} USD")
    print(f"Costo Total Anual: ${costo_total:,.2f} USD")
    print("=" * 45)

    return Q_optimo, rop, tiempo_entre_pedidos



D = 10000          # Demanda anual
S = 150            # Costo por pedido
H = 3              # Costo de mantenimiento por unidad
C = 25             # Costo unitario
dias_lab = 250     # Días laborables
L = 5              # Lead Time

# Resolver modelo EOQ
Q_opt, rop_val, t_ciclo = resolver_eoq(D, S, H, C, dias_lab, L)



num_ciclos = 3

tiempo = np.linspace(0, num_ciclos * t_ciclo, 500)
inventario = []

for t in tiempo:
    tiempo_en_ciclo = t % t_ciclo
    inv = Q_opt - ((D / dias_lab) * tiempo_en_ciclo)
    inventario.append(inv)

plt.figure(figsize=(10,5))
plt.plot(tiempo, inventario, color="navy", linewidth=2, label="Inventario")
plt.axhline(y=rop_val, color="red", linestyle="--", linewidth=2, label="Punto de Reorden")
plt.axhline(y=0, color="black", linewidth=1)

plt.title("Simulación del Modelo EOQ")
plt.xlabel("Días Laborables")
plt.ylabel("Inventario (Unidades)")
plt.grid(True, linestyle=":", alpha=0.6)
plt.legend()
plt.tight_layout()
plt.show()