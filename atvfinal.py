def menu_principal():
    print("\nMenu Principal:")
    print("1 - Alunos")
    print("2 - Professores")
    print("3 - Disciplinas")
    print("4 - Sair")

def menu_operacoes():
    print("\nMenu de Operações:")
    print("1 - Incluir")
    print("2 - Listar")
    print("3 - Atualizar")
    print("4 - Excluir")
    print("5 - Voltar ao Menu Principal")

# Função principal do sistema
def sistema_gestao_academico():
    while True:
        menu_principal()
        opcao_principal = input("Selecione uma opção do Menu Principal: ")
        
        if opcao_principal == "4":
            print("Encerrando o sistema...")
            break
        elif opcao_principal in ["1", "2", "3"]:
            print(f"Você selecionou a opção {opcao_principal} do Menu Principal.")
            
            # Menu de Operações
            while True:
                menu_operacoes()
                opcao_operacoes = input("Selecione uma opção do Menu de Operações: ")
                
                if opcao_operacoes == "5":
                    print("Voltando ao Menu Principal...")
                    break
                elif opcao_operacoes in ["1", "2", "3", "4"]:
                    print(f"Você selecionou a opção {opcao_operacoes} do Menu de Operações.")
                else:
                    print("Opção inválida! Tente novamente.")
        else:
            print("Opção inválida! Tente novamente.")

# Executa o sistema
sistema_gestao_academico()
