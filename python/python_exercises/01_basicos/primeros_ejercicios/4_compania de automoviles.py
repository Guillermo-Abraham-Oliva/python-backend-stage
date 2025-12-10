'''COMPAÑÍA DE AUTOMÓVILES:
Una compañía de automóviles vende tres tipos de coche: 
RBM Serie 1, RMB Serie plus, RBM todoterreno. 
Cada uno de estos coches tiene un precio de venta
y el vendedor recibe una comisión diferente por cada tipo de coche que ha vendido.

Suponga que los precios y las comisiones son:

    RBM Serie 1:
    precio: 20.000 EU, comisión: 3%

    RMB Serie plus:
    precio: 35.000 EU, comisión: 5%

    RBM todoterreno:
    precio: 60.000 EU, comisión: 7%

Crea un programa donde el usuario introduzca el numero de coches vendidos de cada tipo ese
mes y que le devuelva la cantidad en euros a comisionar ese mes.'''

RBM_Serie_1 = int(input('Cuantos RBM Serie 1 has vendido? ')) 
RMB_Serie_plus = int(input('Cuantos RMB Serie plus has vendido? ')) 
RBM_todoterreno = int(input('Cuantos RBM todoterreno has vendido? ')) 

comision = ((RBM_Serie_1 * (20000*0.03)) + (RMB_Serie_plus * (35000*0.05)) + (RBM_todoterreno * (60000*0.07)))

print('Tu Comisión total de este mes es: ', comision, "euros")



