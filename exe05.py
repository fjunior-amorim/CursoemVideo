#=====================\\ exercicio 05 //=======================#
txt = input('digite algo: ')
print('o tipo primitivo de "{}" é igual {}'.format(txt, type(txt)))
print('só tem espaços?',txt.isspace())
print('é um numero?', txt.isnumeric())
print('é alfabetico?', txt.isalpha())
print('é alfanumerico?', txt.isalnum())
print('esta em minuscula?', txt.islower())
print('esta masculas?', txt.isupper())
print('esta capitalizada?', txt.istitle())


