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
        print(mes, round(total_pagado, 2), round(saldo, 2))
    else:
        saldo = saldo * (1+tasa/12) - pago_mensual
        total_pagado = total_pagado + pago_mensual
        if saldo < 0:
            print(mes, round(total_pagado, 2), 0)
        else:
            print(mes, round(total_pagado, 2), round(saldo, 2))

    mes = mes +1
    

print('Total pagado', round(total_pagado, 2), 'meses: ', mes)