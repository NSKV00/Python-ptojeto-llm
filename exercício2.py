#2- Implemente um validador de senha: mínimo 8 caracteres, deve conter número e letra.
senha = input("Digite sua senha: ")

if len(senha) <= 8:
    print("Senha inválida. Deve ter no mínimo 8 caracteres.")
