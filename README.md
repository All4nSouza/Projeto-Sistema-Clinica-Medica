<!DOCTYPE html>
<html>
<head>
  <h1>Documentação do Código Python</h1>
      <h1>Código desenvolvido para sistema de uma clínica médica</h1>
    <p>O seguinte código foi desenvolvido como parte de um trabalho acadêmico na disciplina de Introdução à Programação, no curso de Engenharia Elétrica na UFCG. O objetivo do código é implementar funcionalidades básicas para um sistema de uma clínica médica.</p>
    <p>Cada uma dessas partes é composta por diversas funções que contribuem para o funcionamento completo do sistema.</p>
    <h1>Como Testar: </h1>
    <h2>Para testar o código a seguir, é necessário copiar para uma pasta os arquivos.py e as duas planilhas existentes. Em seguida, execute o arquivo main.py em seu compilador e teste as funcionalidades!<h2>
   
</head>
<body>
  <h1>Funcionabilidades</h1>
  <h2>Parte de "Clientes"</h2>
    <p>Na parte de "Clientes", temos as seguintes funcionalidades:</p>
    <ul>
        <li>Cadastrar novos pacientes</li>
        <li>Cancelar cadastro</li>
        <li>Alterar cadastro do paciente</li>
        <li>Voltar</li>
    </ul>
    <h2>Parte de "Consultas"</h2>
    <p>Já na parte de "Consultas", as funcionalidades disponíveis são:</p>
    <ul>
        <li>Agendar consultas</li>
        <li>Consultar agendamentos</li>
        <li>Voltar</li>
    </ul>
  <h1>Explicação dos Arquivos: </h1>
  <h2>Arquivo main.py</h2>

  <h2>Importações:</h2>
  <ul>
    <li><strong>from clientes import menu_clientes</strong>: importa a função menu_clientes do módulo clientes.</li>
    <li><strong>from consultas import menu_consultas</strong>: importa a função menu_consultas do módulo consultas.</li>
  </ul>

  <h2>Função menu():</h2>
  <p>A função exibe um menu principal para o controle de consultas médicas. O menu apresenta as seguintes opções:</p>
  <ul>
    <li>[1] - Clientes</li>
    <li>[2] - Consultas</li>
    <li>[3] - SAIR</li>
  </ul>
  <p>O usuário pode digitar o número da opção desejada. Dependendo da opção escolhida, a função executa a respectiva função.</p>

  <h2>Função sair():</h2>
  <p>A função exibe uma mensagem de saída e encerra o programa utilizando a função exit().</p>

  <h2>Bloco __name__:</h2>
  <p>O bloco __name__ == "__main__" verifica se o arquivo está sendo executado diretamente (não importado como um módulo).</p>
  <p>Se o arquivo estiver sendo executado diretamente, a função menu() é chamada para iniciar o programa.</p>
 
   <h1>Arquivo functions_clientes</h1>

  <h2>Função menu_clientes():</h2>
  <p>A função exibe um menu para o gerenciamento de clientes. O menu apresenta as seguintes opções:</p>
  <ul>
    <li>[1] - Cadastrar Novos Pacientes</li>
    <li>[2] - Cancelar Cadastro</li>
    <li>[3] - Alterar Cadastro do Paciente</li>
    <li>[4] - Voltar</li>
  </ul>
  <p>O usuário pode digitar o número da opção desejada. Dependendo da opção escolhida, a função executa a respectiva função.</p>

  <h2>Função cadastrar_pacientes():</h2>
  <p>A função permite ao usuário cadastrar um novo paciente. Ela solicita o nome, CPF e número do plano de saúde do paciente.</p>
  <p>Os dados são validados e, em seguida, são gravados no arquivo "pacientes.csv" utilizando a função gravar_paciente(). Se ocorrer algum erro durante a gravação, uma mensagem de erro é exibida.</p>

  <h2>Função obter_nome():</h2>
  <p>A função solicita ao usuário que digite o nome do paciente. Ela realiza algumas validações, como verificar se o nome não está vazio e se não contém números.</p>
  <p>O nome digitado é retornado em letras maiúsculas.</p>

  <h2>Função obter_cpf():</h2>
  <p>A função solicita ao usuário que digite o CPF do paciente. Ela verifica se o CPF possui 11 dígitos e se já está cadastrado.</p>
  <p>Se o CPF for válido e não estiver cadastrado, ele é retornado.</p>

  <h2>Função obter_plano_saude():</h2>
  <p>A função solicita ao usuário que digite o número do plano de saúde do paciente. Ela verifica se o número possui 8 dígitos e se não está cadastrado.</p>
  <p>Se o número do plano for válido e não estiver cadastrado, ele é retornado.</p>

  <h2>Função gravar_paciente(cpf, nome, plano):</h2>
  <p>A função recebe os dados do paciente (CPF, nome e plano de saúde) e os grava no arquivo "pacientes.csv", separados por ponto e vírgula (;).</p>

  <h2>Função verificar_cpf_existente(cpf):</h2>
  <p>A função verifica se um CPF já está cadastrado no arquivo "pacientes.csv". Para cada linha do arquivo, o CPF é extraído e comparado com o CPF informado.</p>
  <p>Se o CPF estiver cadastrado, a função retorna True. Caso contrário, retorna False.</p>

  <h2>Função verificar_plano_existente(plano):</h2>
  <p>A função verifica se um número de plano de saúde já está cadastrado no arquivo "pacientes.csv". Para cada linha do arquivo, o número do plano é extraído e comparado com o número informado.</p>
  <p>Se o número do plano estiver cadastrado, a função retorna True. Caso contrário, retorna False.</p>

  <h2>Função cancelar_cadastro_paciente():</h2>
  <p>A função permite ao usuário cancelar o cadastro de um paciente. Ela solicita o CPF do paciente a ser cancelado e realiza algumas validações.</p>
  <p>Se o CPF for válido e estiver cadastrado, o cadastro é removido do arquivo "pacientes.csv". Caso contrário, uma mensagem de erro é exibida.</p>

  <h2>Função alterar_cadastro_paciente():</h2>
  <p>A função permite ao usuário alterar o cadastro de um paciente. Ela solicita o CPF do paciente a ser alterado e realiza algumas validações.</p>
  <p>Se o CPF for válido e estiver cadastrado, são exibidos os dados do paciente e o usuário pode optar por mantê-los ou alterá-los.</p>
  <p>Se os dados forem alterados, o arquivo "pacientes.csv" é atualizado com as novas informações.</p>

  <h2>Arquivos Utilizados:</h2>
  <ul>
    <li><strong>pacientes.csv</strong>: arquivo utilizado para armazenar os dados dos pacientes cadastrados.</li>
  </ul>

  <p>É importante ressaltar que, para que o código funcione corretamente, o arquivo "pacientes.csv" deve estar presente no mesmo diretório do script Python.</p>
  
  <h1>Arquivo functions_consultas.py</h1>

<h2>Importação de bibliotecas:</h2>
<pre><code>from datetime import datetime</code></pre>
<p>Importa a classe <code>datetime</code> do módulo <code>datetime</code>. Essa classe permite manipular datas e horários no Python.</p>

<h2>Definição de funções:</h2>
<ul>
    <li>
        <h3>menu_consultas()</h3>
        <p>Exibe um menu com opções para o usuário e realiza chamadas às funções correspondentes de acordo com a opção selecionada.</p>
    </li>
    <li>
        <h3>agendar_consultas()</h3>
        <p>Solicita informações do paciente e realiza o agendamento de uma consulta, verificando a disponibilidade de horários.</p>
        <p>O processo de agendamento de consultas envolve a solicitação de informações do paciente, como CPF, nome, plano, data, horário e motivo da consulta. Essas informações são fornecidas pelo usuário.</p>
        <p>Em seguida, a função verifica se a data e o horário fornecidos estão no formato correto e se o horário está dentro dos horários permitidos para agendamento.</p>
        <p>Também é verificado se já existe uma consulta agendada para a mesma data e horário. Caso exista, o agendamento não é realizado.</p>
        <p>Se todas as verificações passarem, a consulta é cadastrada no arquivo "consultas.csv" com os dados fornecidos.</p>
    </li>
    <li>
        <h3>consultar_agendamentos()</h3>
        <p>Consulta as consultas agendadas para um CPF específico e permite imprimir os recibos das consultas.</p>
        <p>O usuário informa um CPF para consultar os agendamentos associados a esse CPF.</p>
        <p>A função busca no arquivo "consultas.csv" as consultas agendadas para o CPF informado e retorna uma lista com os agendamentos encontrados.</p>
        <p>Além disso, o usuário tem a opção de imprimir os recibos das consultas, caso deseje.</p>
    </li>
    <li> 
        <h3>cancelar_consulta()</h3>
        <p>Cancela uma consulta agendada para um CPF específico.</p>
        <p>O usuário informa um CPF e a função verifica se existe uma consulta agendada para esse CPF.</p>
        <p>Se houver uma consulta agendada, ela é removida do arquivo "consultas.csv".</p>
    </li>
    <li>
        <h3>buscar_consultas()</h3>
        <p>Permite buscar consultas com base em critérios como mês e ano ou dia, mês e ano.</p>
        <p>O usuário pode escolher entre buscar consultas por mês e ano ou por dia, mês e ano.</p>
        <p>A função realiza a busca no arquivo "consultas.csv" com base nos critérios informados e retorna uma lista com as consultas encontradas.</p>
    </li>
    <li>
        <h3>encontrar_paciente(cpf)</h3>
        <p>Busca um paciente pelo CPF no arquivo "pacientes.csv" e retorna um dicionário com os dados do paciente encontrado.</p>
        <p>A função recebe um CPF como parâmetro e busca no arquivo "pacientes.csv" pelo CPF correspondente.</p>
        <p>Se o paciente for encontrado, os dados são retornados em um dicionário.</p>
    </li>
    <li>
        <h3>cadastrar_consulta(cpf, nome, plano, data, horario, motivo)</h3>
        <p>Cadastra uma consulta no arquivo "consultas.csv" com os dados fornecidos.</p>
        <p>A função recebe os dados do paciente (CPF, nome, plano, data, horário e motivo) como parâmetros.</p>
        <p>Esses dados são adicionados ao arquivo "consultas.csv" como um novo registro de consulta.</p>
    </li>
    <li>
        <h3>buscar_agendamentos(cpf)</h3>
        <p>Busca os agendamentos de consultas para um CPF específico e retorna uma lista com os agendamentos encontrados.</p>
        <p>A função recebe um CPF como parâmetro e busca no arquivo "consultas.csv" pelos agendamentos associados a esse CPF.</p>
        <p>Os agendamentos encontrados são retornados em uma lista.</p>
    </li>
    <li>
        <h3>verificar_formato_data(data)</h3>
        <p>Verifica se a data fornecida está no formato correto (dd/mm/aaaa).</p>
        <p>A função recebe uma data como parâmetro e verifica se ela está no formato correto.</p>
        <p>Se estiver no formato correto, retorna verdadeiro (True); caso contrário, retorna falso (False).</p>
    </li>
    <li>
        <h3>verificar_formato_horario(horario)</h3>
        <p>Verifica se o horário fornecido está no formato correto (hh:mm).</p>
        <p>A função recebe um horário como parâmetro e verifica se ele está no formato correto.</p>
        <p>Se estiver no formato correto, retorna verdadeiro (True); caso contrário, retorna falso (False).</p>
    </li>
    <li>
        <h3>verificar_horario(horario)</h3>
        <p>Verifica se o horário fornecido está dentro dos horários permitidos para agendamento.</p>
        <p>A função recebe um horário como parâmetro e verifica se ele está dentro dos horários permitidos.</p>
        <p>Se estiver dentro dos horários permitidos, retorna verdadeiro (True); caso contrário, retorna falso (False).</p>
    </li>
    <li>
        <h3>verificar_disponibilidade(data, horario)</h3>
        <p>Verifica se já existe uma consulta agendada para a data e horário fornecidos.</p>
        <p>A função recebe uma data e um horário como parâmetros e verifica se já existe uma consulta agendada para essa data e horário.</p>
        <p>Se não houver consulta agendada, retorna verdadeiro (True); caso contrário, retorna falso (False).</p>
    </li>
    <li>
        <h3>listar_horarios_disponiveis(data)</h3>
        <p>Lista os horários disponíveis para agendamento em uma determinada data.</p>
        <p>A função recebe uma data como parâmetro e lista os horários disponíveis para agendamento nessa data.</p>
        <p>Esses horários são obtidos a partir das consultas agendadas para a data informada.</p>
    </li>
    <li>
        <h3>verificar_cpf_existente_consulta(cpf)</h3>
        <p>Verifica se existe uma consulta agendada para o CPF fornecido.</p>
        <p>A função recebe um CPF como parâmetro e verifica se existe uma consulta agendada para esse CPF no arquivo "consultas.csv".</p>
        <p>Se houver uma consulta agendada, retorna verdadeiro (True); caso contrário, retorna falso (False).</p>
    </li>
</ul>

<h2>Chamada da função menu_consultas():</h2>
<pre><code>Inicia o programa, exibindo o menu principal e aguardando as ações do usuário.</code></pre>

<h2>Utilização de arquivos CSV:</h2>
<p>O código utiliza arquivos CSV ("consultas.csv" e "pacientes.csv") para armazenar os dados das consultas agendadas e dos pacientes. Esses arquivos são manipulados para realizar as operações de agendamento, consulta, cancelamento e busca.</p>

<h2>Menu principal:</h2>
<p>O usuário pode selecionar as opções digitando o número correspondente. Cada opção chama uma função específica para realizar a ação desejada.</p>
