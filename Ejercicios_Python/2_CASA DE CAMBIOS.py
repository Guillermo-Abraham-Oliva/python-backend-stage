Euros_Usuario = int(0)
Dolares_equivalentes = float(0.00000)
Comision = float(10)
Cambio_Euro_a_Dolar_hoy = float(1.2000)
Dolares_finales = float(0.00000)
Comision_total = float(0.00000)
confirmacion = str()

print('\n\n\t\t♔ ♕   Casa de Cambio  ♔ ♕')
Euros_Usuario = int(input('\n\tTus euros? '))

Dolares_equivalentes = (Euros_Usuario * Cambio_Euro_a_Dolar_hoy)
print(f'\nCambio "directo" (sin comisión) .... {Dolares_equivalentes:.2f} dólares.-')

Comision_total = (Dolares_equivalentes * Comision) / 100
print(f'\nComisión (10%) .....................  {Comision_total:.2f} dólares.-')

Dolares_finales = Dolares_equivalentes - Comision_total
print(f'\n-----Recibirás neto ................ {Dolares_finales:.2f} dólares.-')

confirmacion = input('\n\n        Realizas la operación? [y/n] ').strip().lower()

if confirmacion == 'y':
    print('\n---Recoge tus dólares. Gracias por elegirnos ♫•¨•.¸¸ღ')
    print('\n\n')
elif confirmacion == 'n':
    print('\n---Adiós ♫•¨•.¸¸ღ ')
    print('\n\n')
else:
    print('\n### Opción no válida ###')
    print('\n---Adiós.-')
    print('\n\n')
