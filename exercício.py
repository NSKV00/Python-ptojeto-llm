#Para rodar o código, python exercíco.py

nota = 8.5
if nota >= 7:
    status = "Aprovado"
elif nota >= 5:
    status = "Recuperação"
else:
    status = "Reprovado"

print(f"Nota: {nota} - Status: {status}")

#Loop for
print("\nNúmeros de 1 a 5:")
for n in range(1, 6):
    print(n)

#Loop while
print("\nDigite algo (ou 'sair' para encerrar):")
while True:
    texto = input("Digite algo (ou 'sair'): ")
    if texto.lower() == 'sair':
        break
    print(f"Você digitou: {texto}")

print("Programa encerrado.")