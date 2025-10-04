num = int(input('Digite um numero inteiro: '))
primo = True
if num < 2 :
    primo = False
else:
    for i in range(2, num):
        if  num % i == 0:
            primo = False

if primo:
    print(f'{num} é um numero primo')
else:
    print(f'{num} não é um numero primo')