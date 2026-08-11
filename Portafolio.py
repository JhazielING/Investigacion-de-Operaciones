import math

D = 12000
S = 200
H = 4
C = 50
dias_laborables = 240
lead_time = 6

EOQ = math.sqrt((2 * D * S) / H)
pedidos_anuales = D / EOQ
demanda_diaria = D / dias_laborables
ROP = demanda_diaria * lead_time

costo_ordenar = (D / EOQ) * S
costo_mantener = (EOQ / 2) * H
costo_compra = D * C
costo_total = costo_ordenar + costo_mantener + costo_compra

print("===== EJERCICIO 3.4 - MODELO EOQ =====")
print(f"EOQ: {EOQ:.2f} tarjetas por pedido")
print(f"EOQ redondeado: {round(EOQ)} tarjetas")
print(f"Pedidos al año: {pedidos_anuales:.2f}")
print(f"Demanda diaria: {demanda_diaria:.2f} tarjetas")
print(f"Punto de reorden: {ROP:.2f} tarjetas")
print(f"Costo de ordenar: ${costo_ordenar:.2f} USD")
print(f"Costo de mantener: ${costo_mantener:.2f} USD")
print(f"Costo de compra: ${costo_compra:.2f} USD")
print(f"Costo total anual: ${costo_total:.2f} USD")