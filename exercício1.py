#1- Escreva um programa que lê 5 idades e imprima a média, a maior e a menor idade.
Idades = [12, 19, 8, 25, 18]
soma_idades = sum(Idades)

media = soma_idades / len(Idades)

print(f"Média das idades: {media}")
print(f"Maior idade: {max(Idades)}")
print(f"Menor idade: {min(Idades)}")