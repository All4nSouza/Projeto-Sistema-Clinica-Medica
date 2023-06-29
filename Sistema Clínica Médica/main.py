from functions_clientes import cadastrar_pacientes, cancelar_cadastro_paciente, alterar_cadastro_paciente
from functions_consultas import agendar_consultas, cancelar_consulta, consultar_agendamentos, buscar_consultas


def menu():
    while True:
        print('''
    ==========================================
    Menu:

    Bem vindo ao controle de consultas médicas:

    [1] - Clientes
    [2] - Consultas
    [3] - SAIR

    ==========================================
        ''')

        opcoes = input("Digite a opção desejada: ")

        if opcoes == "1":
            menu_clientes()
        elif opcoes == "2":
            menu_consultas()
        elif opcoes == "3":
            sair()
        else:
            print("Opção inválida. Digite um número válido.")


def menu_clientes():
    while True:
        print('''
    =================================================
          CLIENTES:

    [1] - Cadastrar Novos Pacientes
    [2] - Cancelar Cadastro
    [3] - Alterar Cadastro do Paciente   
    [4] - Voltar

    =================================================
        ''')

        opcao = input("Digite a opção desejada: ")

        if opcao == "1":
            cadastrar_pacientes()
        elif opcao == "2":
            cancelar_cadastro_paciente()
        elif opcao == "3":
            alterar_cadastro_paciente()
        elif opcao == "4":
            break
        else:
            print("Opção inválida. Digite um número válido.")


def menu_consultas():
    while True:
        print('''
    =================================================
          CONSULTAS:

    [1] - Agendar Consultas
    [2] - Cancelar Consultas
    [3] - Consultar Agendamentos e Imprimir Recibos
    [4] - Buscar Consultas 
    [5] - Voltar

    =================================================
        ''')

        opcao = input("Digite a opção desejada: ")

        if opcao == "1":
            agendar_consultas()
        elif opcao == "2":
            cancelar_consulta()
        elif opcao == "3":
            consultar_agendamentos()
        elif opcao == "4":
            buscar_consultas()
        elif opcao == "5":
            break
        else:
            print("Opção inválida. Digite um número válido.")


def sair():
    print("Saindo do programa...")
    exit()


if __name__ == "__main__":
    menu()
