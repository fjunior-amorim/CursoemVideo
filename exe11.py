hora = float(input('quantas horas: '))
if hora < 6:
    print('Agora são {}hs, tenha uma boa madrugada!'.format(hora))
elif hora < 12:
    print('Agora são {}hs, BOM DIA!'.format(hora))
elif hora < 18:
    print('Agora são {}hs, BOA TARDE!'.format(hora))
else:
    print('Agora são {}hs, BOA NOITE!'.format(hora))
