
# Inicializa uma lista para armazenar as notas
notas = []

# Loop para receber as notas dos alunos
for i in range(1, 6):
    nota = float(input(f'Nota do aluno {i}: '))
    notas.append(nota)

# Calcula a maior e menor nota
maior_nota = max(notas)
menor_nota = min(notas)

# Calcula a média das notas
media_nota = sum(notas) / len(notas)
# Exibe os resultados
print(f'Maior nota: {maior_nota}')
print(f'Menor nota: {menor_nota}')
print(f'Média das notas: {media_nota:.1f}')