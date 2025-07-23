
peso = float(input('Qual pe o seu peso? (Kg) '))
altura = float(input('Qual é a sua altura? (M) '))
imc = peso / (altura ** 2)
print(f'Seu IMC é de {imc:.2f}')
if imc < 18.5:
    print('Você está Abaixo do Peso')
elif 18.5 <= imc < 25:
    print('Você está com Peso ideal')
elif  25 <= imc < 30:
    print('Você está com Sobreoeso')
elif 30 <= imc < 40 :
    print('Você está com Obesidade')
elif imc >= 40:
    print('Você está com Obesidade Morbida, CUIDADO!!!')
