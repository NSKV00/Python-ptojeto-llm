#2- Implemente um validador de senha: mínimo 8 caracteres, deve conter número e letra.

while True:
    senha = input("Digite uma senha para validar (ou 'sair' para encerrar): ")
    if senha.lower() == 'sair':
        break

    if len(senha) < 8:
        print("Senha inválida. Deve ter no mínimo 8 caracteres.")
    elif not any(char.isdigit() for char in senha):
        print("Senha inválida. Deve conter pelo menos um número.")
    elif not any(char.isalpha() for char in senha):
        print("Senha inválida. Deve conter pelo menos uma letra.")
    # elif not any(char.isupper() for char in senha):
    #     print("Senha inválida. Deve conter pelo menos uma letra maiúscula.")
    else:
        print("Senha válida.")

print("Validador de senha encerrado.")