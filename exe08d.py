print('=$'*20)
preco = float(input('digite o preço do produto:R$ '))
novo = preco - (preco * 5 / 100)
econom = preco - novo
print('-'*45)
print('o produto com preço de R${},\n a vista saí á R${:.2f}\n '
      'voce economizará R${:.2f}'.format(preco, novo, econom))
print('-'*45)
parc = int(input('voce pode parcelar: '))
alm = preco + (preco * 10 / 100)
valorP = alm / parc
print('-'*45)
print('voce pagará {} parcelas no valor de R${:.2f}'.format(parc, valorP))
print('parcelando em {}x o valor será de R${}.'.format(parc, alm))
print('-'*45)
print(' '*20)
print('-'*10, 'vamos finalizar a compra?', '-'*10)
