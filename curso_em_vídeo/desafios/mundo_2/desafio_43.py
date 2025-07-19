
peso = float(input('Qual pe o seu peso? '))
altura = float(input('Qual é a sua altura? '))
imc = peso / (altura * altura)
if imc < 18.5:
    print('Abaixo do Peso')
elif imc == 18.5 in 25:
    print('Peso ideal')
elif imc == 25 in 30:
    print('Sobreoeso')
elif imc ==  range(30, 40):
    print('Obesidade')
elif imc > 40:
    print('Obesidade Morbida')
print(f'Seu IMC é de {imc:.2f}')