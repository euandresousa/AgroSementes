
sementes = []

print("================================")
print("======SISTEMA AGROSEMENTES======")
print("================================")
print("Desenvolvedor: André Luz")

while True:
    print("\n1 - Cadastrar semente")
    print("2 - Consultar estoque")
    print("3 - Sobre o sistema")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Digite o nome da semente: ")

        try:
            quantidade = float(
                input("Digite a quantidade em kg: ")
            )

            if quantidade <= 0:
                print("A quantidade deve ser maior que zero.")
            else:
                semente = {
                    "nome": nome,
                    "quantidade": quantidade
                }

                sementes.append(semente)
                print("Semente cadastrada com sucesso!")

        except ValueError:
            print("Erro: digite uma quantidade numérica.")

    elif opcao == "2":
        if len(sementes) == 0:
            print("Nenhuma semente cadastrada.")
        else:
            print("\n===== ESTOQUE =====")

            for item in sementes:
                print("Nome:", item["nome"])
                print("Quantidade:", item["quantidade"], "kg")
                print("--------------------")

    elif opcao == "3":
        print("Sistema AgroSementes")
        print("Desenvolvido para controle de sementes.")

    elif opcao == "4":
        print("Encerrando o sistema...")
        break

    else:
        print("Opção inválida!")


