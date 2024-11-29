
def coletar_dados():
    print("Formulário de Contato")
    print("----------------------")
    
    # Coletando os dados do usuário
    nome = input("Digite seu nome: ")
    email = input("Digite seu e-mail: ")
    telefone = input("Digite seu número de contato: ")

    # Exibindo a confirmação
    print("\nObrigado pelo seu contato!")
    print("Resumo da sua mensagem:")
    print(f"Nome: {nome}")
    print(f"E-mail: {email}")
    print(f"Número de Contato: {telefone}")

# Chama a função para coletar e exibir os dados
coletar_dados()
