def cadastrar_pacientes():
    print('''
    ====================
    Cadastrar Pacientes:
    ====================
    ''')

    nome = obter_nome()
    cpf = obter_cpf()
    plano = obter_plano_saude()

    try:
        gravar_paciente(cpf, nome, plano)
        print("Cadastro de paciente realizado com sucesso.")
    except Exception as e:
        print("ERRO na gravação do Paciente:", str(e))


def obter_nome():
    while True:
        nome = input("Digite o nome do paciente: ").strip()

        if not nome:
            print("O nome não pode ser vazio. Por favor, tente novamente.")
            continue

        if any(char.isdigit() for char in nome):
            print("O nome não pode conter números. Por favor, tente novamente.")
            continue

        return nome.upper()


def obter_cpf():
    while True:
        cpf = input("Digite o CPF do paciente: ")

        if len(cpf) != 11 or not cpf.isdigit():
            print("Erro: O CPF deve ter obrigatoriamente 11 dígitos.")
        else:
            if verificar_cpf_existente(cpf):
                print("Erro: CPF já cadastrado.")
            else:
                return cpf


def obter_plano_saude():
    while True:
        plano = input("Digite o número do plano de saúde para continuar: ")

        if len(plano) == 8 and plano.isdigit():
            if verificar_plano_existente(plano):
                print("Erro: Número do plano já cadastrado.")
            else:
                return plano
        else:
            print("Erro: O número do plano deve ter 8 dígitos e não deve possuir letras. Confira os dados!")


def gravar_paciente(cpf, nome, plano):
    dados = f'{cpf};{nome};{plano}\n'
    with open("pacientes.csv", "a") as pacientes_cadastrados:
        pacientes_cadastrados.write(dados)


def verificar_cpf_existente(cpf):
    with open("pacientes.csv", "r") as pacientes_cadastrados:
        for paciente in pacientes_cadastrados:
            cpf_cadastrado = paciente.split(";")[0]
            if cpf == cpf_cadastrado:
                return True
    return False


def verificar_plano_existente(plano):
    with open("pacientes.csv", "r") as pacientes_cadastrados:
        for paciente in pacientes_cadastrados:
            plano_cadastrado = paciente.split(";")[2]
            if plano == plano_cadastrado.strip():
                return True
    return False


def cancelar_cadastro_paciente():
    print('''
    ====================
    Cancelar Cadastro:
    ====================
    ''')
    cpf = input("Digite o CPF do paciente que você deseja cancelar: ")
    if len(cpf) != 11 or not cpf.isdigit():
        print("Erro: O CPF deve ter obrigatoriamente 11 dígitos.")
    else:
        if verificar_cpf_existente(cpf):
            pacientes = []
            with open("pacientes.csv", "r") as pacientes_cadastrados:
                for paciente in pacientes_cadastrados:
                    if cpf not in paciente:
                        pacientes.append(paciente)

            with open("pacientes.csv", "w") as pacientes_cadastrados:
                pacientes_cadastrados.writelines(pacientes)
            print("Cadastro deletado com sucesso.")
        else:
            print("Não há cadastro existente para esse CPF!")


def alterar_cadastro_paciente():
    print('''
    =========================
    Alterar Cadastro Paciente
    =========================
    ''')
    cpf = input("Digite o CPF do paciente que deseja alterar o cadastro: ")
    pacientes = []
    encontrado = False

    with open("pacientes.csv", "r") as pacientes_cadastrados:
        for paciente in pacientes_cadastrados:
            dados = paciente.split(";")
            if cpf == dados[0]:
                print(f"CPF: {dados[0]}")
                print(f"Nome: {dados[1]}")
                print(f"Plano de Saúde: {dados[2]}")
                opcao = input("Deseja manter os dados do cadastro? (S/N): ")
                if opcao.upper() == "N":
                    nome = obter_nome()
                    plano = obter_plano_saude()
                    if nome.strip():
                        dados[1] = nome
                    if plano.strip():
                        dados[2] = plano
                    paciente = ";".join(dados)
                pacientes.append(paciente)
                encontrado = True

    if not encontrado:
        print("CPF não encontrado no banco de dados.")
        return

    with open("pacientes.csv", "w") as pacientes_cadastrados:
        pacientes_cadastrados.writelines(pacientes)

    print("Processo Finalizado")
