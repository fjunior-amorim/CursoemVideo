di = float(input('quantas reis voce quer coverter:R$ '))
dolar = di / 5.11
euro = di / 5.37
iene = di / 0.038
print('com {} voce tera US {:.2f} dolares\n e com {} voce tera EUR {:.2f} euros\n'
      'e com {} voce tera IN {:.2f} iene(japones)'.format(di, dolar, di, euro, di, iene))
