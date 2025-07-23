nota1 = float(input('Digite a nota do aluno: '))
nota2 = float(input('Digite a segunda nota do aluno: '))
media = (nota1 + nota2) / 2
if media < 5.0:
    print(f'A média do aluno é {media}')
    print('REPROVADO')
elif media >= 5.0 and media < 7:
    print(f'A média do aluno é {media}')
    print('RECUPERAÇÃO')
else:
    print(f'A média do aluno é {media}')
    print('APROVADO')
