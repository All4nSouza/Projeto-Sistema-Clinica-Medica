from datetime import datetime


def agendar_consultas():
    print('''
    ==================
    Agendar Consultas:
    ==================
    ''')
    cpf = input("Digite o CPF do paciente que deseja fazer a consulta: ")
    paciente = encontrar_paciente(cpf)

    if paciente:
        motivo = input("Digite o motivo da consulta: ").upper()

        while not motivo.strip():
            print("O motivo da consulta não pode ser vazio. Por favor, digite novamente.")
            motivo = input("Digite o motivo da consulta: ").upper()

        data = input("Digite a data da consulta [dia/mes/ano]: ")
        horario = input("Digite o horário da consulta [hora:min]: ")

        if verificar_formato_data(data) and verificar_formato_horario(horario):
            data_atual = datetime.now().strftime("%d/%m/%Y")
            data_obj = datetime.strptime(data, "%d/%m/%Y")
            data_atual_obj = datetime.strptime(data_atual, "%d/%m/%Y")

            if data_obj >= data_atual_obj:
                if verificar_horario(horario):
                    if verificar_disponibilidade(data, horario):
                        try:
                            cadastrar_consulta(cpf, paciente["nome"], paciente["plano"], data, horario, motivo)
                            print("Consulta agendada com sucesso.")
                        except Exception as e:
                            print("Erro na gravação da consulta:", str(e))
                    else:
                        print("Horário indisponível. Escolha outro horário.")
                        horarios_disponiveis = listar_horarios_disponiveis(data)
                        if horarios_disponiveis:
                            print("Horários disponíveis:")
                            for horario_disponivel in horarios_disponiveis:
                                print(horario_disponivel)
                        else:
                            print("Não há horários disponíveis nesse dia.")
                else:
                    print("Horário inválido. Os horários permitidos são: 08:00 às 12:00 e das 14:00 até 18:00!")
            else:
                print("Data inválida. A data da consulta deve ser igual ou posterior à data atual.")
        else:
            print("Formato inválido. O formato da data deve ser dd/mm/aaaa (exemplo: 30/06/2023) "
                  "e o formato do horário deve ser hh:mm (exemplo: 08:30).")
    else:
        print("CPF não cadastrado. Confira os dados ou cadastre o paciente!")


def consultar_agendamentos():
    print('''
    ====================
    Verificar Consultas:
    ====================
    ''')
    cpf = (input("Digite o CPF que voce deseja consultar: "))
    if len(cpf) != 11 or not cpf.isdigit():
        print("Erro: O CPF deve ter obrigatoriamente 11 dígitos.")

    elif verificar_cpf_existente_consulta(cpf):
        consultas_cadastradas = open("consultas.csv", "r")

        agendamentos_encontrados = []
        for linha in consultas_cadastradas:
            dados = linha.split(";")
            if cpf == dados[0]:
                agendamentos_encontrados.append({
                    "cpf": dados[0],
                    "nome": dados[1],
                    "plano": dados[2],
                    "data": dados[3],
                    "horario": dados[4],
                    "motivo": dados[5].rstrip("\n")
                })

        consultas_cadastradas.close()

        if len(agendamentos_encontrados) > 0:
            print("Agendamentos encontrados para o CPF:", cpf)
            recibo = input('Deseja imprimir o recibo [S/N]').upper()
            for agendamento in agendamentos_encontrados:
                if recibo == 'S':
                    print(f'''
        =====================================
                RECIBO DE CONSULTA
        =====================================
        O(a) paciente {agendamento["nome"]}, cujo CPF é
        {agendamento["cpf"]}, possui uma consulta 
        agendada para a data {agendamento["data"]} no 
                 horario {agendamento["horario"]}

                Motivo da Consulta

                    {agendamento["motivo"]}
        ====================================
                ''')

    else:
        print("Nenhum agendamento encontrado para o CPF:", cpf)


def cancelar_consulta():
    print('''
              ====================
              Cancelar Consulta:
              ====================
              ''')
    cpfdeletado = input("Digite o CPF que você deseja cancelar: ")
    if len(cpfdeletado) != 11 or not cpfdeletado.isdigit():
        print("Erro: O CPF deve ter obrigatoriamente 11 dígitos.")
    else:
        if verificar_cpf_existente_consulta(cpfdeletado):
            with open("consultas.csv", "r") as consulta_file:
                consultas = consulta_file.readlines()

            consultas_encontradas = []
            for consulta in consultas:
                if cpfdeletado in consulta:
                    consultas_encontradas.append(consulta)

            if len(consultas_encontradas) == 0:
                print("Não há consultas existentes para esse CPF!")
            elif len(consultas_encontradas) == 1:
                consulta = consultas_encontradas[0]
                consultas.remove(consulta)
                with open("consultas.csv", "w") as consulta_file:
                    consulta_file.writelines(consultas)
                print("Consulta deletada com sucesso")
            else:
                print("Foram encontradas múltiplas consultas para o CPF informado:")
                for i, consulta in enumerate(consultas_encontradas):
                    print(f"{i + 1}. {consulta}")

                consulta_escolhida = int(input("Digite o número da consulta que deseja cancelar: "))
                if consulta_escolhida <= len(consultas_encontradas):
                    consulta = consultas_encontradas[consulta_escolhida - 1]
                    consultas.remove(consulta)
                    with open("consultas.csv", "w") as consulta_file:
                        consulta_file.writelines(consultas)
                    print("Consulta deletada com sucesso")
                else:
                    print("Número de consulta inválido!")
        else:
            print("Não há consultas existentes para esse CPF!")


def buscar_consultas():
    print('''
    ==============================
    Buscar Consultas:
    ==============================
    ''')
    opcoes = input('''
    Selecione a opção de busca:
    [1] - Buscar consultas por mês e ano
    [2] - Buscar consultas por dia, mês e ano
    [3] - Voltar ao menu principal
    ''')

    consultas_cadastradas = open("consultas.csv", "r")
    consultas_encontradas = []

    if opcoes == "1":
        mes = input("Digite o mês desejado (formato numérico): ")
        ano = input("Digite o ano desejado: ")

        for linha in consultas_cadastradas:
            dados = linha.split(";")
            data = dados[3].split("/")
            if len(data) == 3 and data[1] == mes and data[2].rstrip("\n") == ano:
                consultas_encontradas.append({
                    "cpf": dados[0],
                    "nome": dados[1],
                    "plano": dados[2],
                    "data": dados[3],
                    "horario": dados[4],
                    "motivo": dados[5].rstrip("\n")
                })

    elif opcoes == "2":
        dia = input("Digite o dia desejado: ")
        mes = input("Digite o mês desejado (formato numérico): ")
        ano = input("Digite o ano desejado: ")

        for linha in consultas_cadastradas:
            dados = linha.split(";")
            data = dados[3].split("/")
            if len(data) == 3 and data[0] == dia and data[1] == mes and data[2].rstrip("\n") == ano:
                consultas_encontradas.append({
                    "cpf": dados[0],
                    "nome": dados[1],
                    "plano": dados[2],
                    "data": dados[3],
                    "horario": dados[4],
                    "motivo": dados[5].rstrip("\n")
                })

    consultas_cadastradas.close()

    if len(consultas_encontradas) > 0:
        print("Consultas encontradas:")
        for consulta in consultas_encontradas:
            print(f'''
            =====================================
            CPF: {consulta["cpf"]}
            Nome: {consulta["nome"]}
            Plano de Saúde: {consulta["plano"]}
            Data: {consulta["data"]}
            Horário: {consulta["horario"]}
            Motivo: {consulta["motivo"]}
            =====================================
            ''')
    else:
        print("Nenhuma consulta encontrada com os critérios especificados.")


def encontrar_paciente(cpf):
    with open("pacientes.csv", "r") as arquivo:
        for linha in arquivo:
            dados_paciente = linha.strip().split(";")
            if dados_paciente[0] == cpf:
                return {"cpf": dados_paciente[0], "nome": dados_paciente[1], "plano": dados_paciente[2]}
    return None


def cadastrar_consulta(cpf, nome, plano, data, horario, motivo):
    with open("consultas.csv", "a") as arquivo:
        arquivo.write(f"{cpf};{nome};{plano};{data};{horario};{motivo}\n")


def buscar_agendamentos(cpf):
    agendamentos = []
    with open("consultas.csv", "r") as arquivo:
        for linha in arquivo:
            dados_consulta = linha.strip().split(";")
            if dados_consulta[0] == cpf:
                agendamentos.append({"data": dados_consulta[3], "horario": dados_consulta[4],
                                     "motivo": dados_consulta[5]})
    return agendamentos


def verificar_formato_data(data):
    try:
        datetime.strptime(data, "%d/%m/%Y")
        return True
    except ValueError:
        return False


def verificar_formato_horario(horario):
    try:
        datetime.strptime(horario, "%H:%M")
        return True
    except ValueError:
        return False


def verificar_horario(horario):
    horarios_permitidos = ["08:00", "08:30", "09:00", "09:30", "10:00", "10:30", "11:00", "11:30", "14:00", "14:30",
                           "15:00", "15:30", "16:00", "16:30", "17:00", "17:30"]
    return horario in horarios_permitidos


def verificar_disponibilidade(data, horario):
    with open("consultas.csv", "r") as arquivo:
        for linha in arquivo:
            dados_consulta = linha.strip().split(";")
            if dados_consulta[3] == data and dados_consulta[4] == horario:
                return False
    return True


def listar_horarios_disponiveis(data):
    horarios_disponiveis = ["08:00", "08:30", "09:00", "09:30", "10:00", "10:30", "11:00", "11:30", "14:00", "14:30",
                            "15:00", "15:30", "16:00", "16:30", "17:00", "17:30"]

    with open("consultas.csv", "r") as arquivo:
        for linha in arquivo:
            dados_consulta = linha.strip().split(";")
            if dados_consulta[3] == data and dados_consulta[4] in horarios_disponiveis:
                horarios_disponiveis.remove(dados_consulta[4])

    return horarios_disponiveis


def verificar_cpf_existente_consulta(cpf):
    pacientes_cadastrados = open("consultas.csv", "r")
    for paciente in pacientes_cadastrados:
        cpf_cadastrado = paciente.split(";")[0]
        if cpf == cpf_cadastrado:
            pacientes_cadastrados.close()
            return True
    pacientes_cadastrados.close()
    return False
