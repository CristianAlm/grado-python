# hipoteca.py

saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0
mes = 0
pagoExtra = 1000

while saldo > 0:
    if mes < 12:
        saldo = saldo * (1+tasa/12) - pago_mensual - pagoExtra
        total_pagado = total_pagado + pago_mensual + pagoExtra
    else:
        saldo = saldo * (1+tasa/12) - pago_mensual
        total_pagado = total_pagado + pago_mensual
    mes = mes +1

mensaje = (
    f'Total pagado es '
    f'{round(total_pagado, 2)}'
    f' en '
    f'{mes}'
    f' meses'
)
print(mensaje)