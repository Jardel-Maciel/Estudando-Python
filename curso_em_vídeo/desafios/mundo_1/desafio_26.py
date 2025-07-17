frase = str(input('Digite uma frase: ')).strip().upper()
print(f'Quantas veses aparece a letra A nessa frase? {frase.count('A')}')
print(f'Em quais psições ela aparece? {frase.find('A')+1}')
print(f'Em qual posição ela aprarece a ultima vez? {frase.rfind('A')+1}')
