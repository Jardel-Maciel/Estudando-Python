nota1 = float(input('Digite a nota do aluno: '))
nota2 = float(input('Digite a segunda nota do aluno: '))
media = (nota1 + nota2) / 2
print(f'A média do aluno é {media}')
if media < 5.0:   
    print('REPROVADO')
elif media >= 5.0 and media < 7:    
    print('RECUPERAÇÃO')
else:    
    print('APROVADO')
