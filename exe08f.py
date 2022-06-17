dias = int(input('quantos dias?: '))
km = float(input('quantos Km?: '))
pago = (dias * 60) + (km * 0.15)
print('o valor a ser pago é de R${:.2f}'.format(pago))
