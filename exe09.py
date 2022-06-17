# =================\ exercicio 09 /==================== #
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2

if media < 5:
    print('aluno reprovado!')
    print('a media foi: {}'.format(media))
else:
    if media < 7:
        print('aluno esta de recuperação!')
        print('a media foi: {}'.format(media))
    else:
        print("O aluno está aprovado")
        print("Parabéns !")
        print('a media foi: {}'.format(media))
