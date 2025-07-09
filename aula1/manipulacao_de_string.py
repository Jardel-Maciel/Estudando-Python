
#s2 = 'A' + ' '*28 + 'B'
#print(s2)

#Maneira mas complicada

"""
nota = 8.9
s1 = 'Voce tirou no ta %.2f na disciplina de Algoritimos' % nota
print(s1) 
"""

"""
nota = 8.9
diciplina = 'Matematica'
s1 = 'voce tirou %.2f na diciplina %s .' %(nota, diciplina)
print(s1)
"""

#composição moderna
"""
nota = 8.9
diciplina = 'Matematica'
s1 = 'voce tirou {} na diciplina {} .' .format(nota, diciplina)
print(s1)
"""
#formato com f-string
nota = 8.9
diciplina = 'Matematica'
s1 = f'voce tirou nota {nota},  na diciplina  de {diciplina} .'
print(s1)





