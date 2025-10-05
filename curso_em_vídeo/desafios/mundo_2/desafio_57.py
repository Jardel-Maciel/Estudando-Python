sexo = ''
while sexo.upper() != 'M' and sexo.upper() != 'F' :
    sexo = str(input('Qual é o seu genero [M/F] : ')).upper()
    if sexo == 'M':
        print('Você escolhel a opção Masculino.')
    if sexo == 'F':
        print('Você escolheu a opção Feminino')
    

