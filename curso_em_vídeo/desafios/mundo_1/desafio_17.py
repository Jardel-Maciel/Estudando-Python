from math import hypot
co = float(input('Qual é a medida do cateto oposto? '))
ca = float(input('Qua a medida do cattedo adjacente? '))
print(f'A soma do cateto oposto {co} mais o cateto adjacente {ca}, tem uma hipotenuza {hypot(co, ca):.2f}')