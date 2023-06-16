# Arthur Pedroso De Francesco -> rm551087
# Lucas Matheus da Silve ->


def adicionar_alimento(cardapio):
    nome = input("Digite o nome do alimento: ")
    quantidade = float(input("Digite a quantidade do alimento: "))
    medida = input("Digite a medida (gramas, quilos, litros ou unidades): ")
    cardapio[nome] = (quantidade, medida)
    print(f"O alimento '{nome}' foi adicionado ao cardápio com sucesso.")


def exibir_cardapio(cardapio):
    if not cardapio:
        print("O cardápio está vazio.")
    else:
        print("Cardápio:")
        for nome, (quantidade, medida) in cardapio.items():
            print(f"{nome}: {quantidade} {medida}")


def remover_alimento(cardapio):
    if not cardapio:
        print("O cardápio está vazio. Não há alimentos para remover.")
        return

    exibir_cardapio(cardapio)
    nome = input("Digite o nome do alimento que deseja remover: ")
    if nome not in cardapio:
        print("Alimento não encontrado no cardápio.")
        return

    del cardapio[nome]
    print(f"O alimento '{nome}' foi removido do cardápio com sucesso.")


def menu():
    cardapio = {}
    while True:
        print("\n----Bem vindo!----")
        print("1. Adicionar alimento")
        print("2. Exibir cardápio")
        print("3. Remover alimento")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_alimento(cardapio)
        elif opcao == "2":
            exibir_cardapio(cardapio)
        elif opcao == "3":
            remover_alimento(cardapio)
        elif opcao == "4":
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida. Por favor, escolha novamente.")


menu()