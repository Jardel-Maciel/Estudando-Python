from math import sin, cos, tan, radians
ang = float(input('Digite o valor do ângulo: '))
seno = sin(radians(ang))
print(f'O angulo de {ang} tem um seno de {seno:.2f}')
cosseno = cos(radians(ang))
print(f'O ângulo {ang}, tem o cosseno de {cosseno:.2f} ')
tangente = tan(radians(ang))
print(f'O angulo de {ang}, tem a tangente de {tangente:.2f}')
