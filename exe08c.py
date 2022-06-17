lg = float(input('digite a lagura da parede: '))
al = float(input('digite a altura da parede: '))
area = lg * al
print('as dimesões da parede de {} x {} tem uma area de {}m².'.format(lg, al, area))
tinta = area / 7.18  # teste ultilizando tinta Suvinil
print('para pinta essa parede voce precisará de {:.2f} l de Tinta Suvinil.'.format(tinta))
