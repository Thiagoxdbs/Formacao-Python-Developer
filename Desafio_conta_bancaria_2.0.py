TASK = False
user = list()
VALIDACAO_LOGIN = False
saldo = 0
extrato = list()
contsaq = 0

# Login


def cadastro_login(opcao):
    valor_cadastro_login = str(input(opcao)).upper().lstrip(" ")
    print("-"*len(opcao))
    VALIDACAO_CAD_LOG = valor_cadastro_login[0] == 'L' or valor_cadastro_login[
        0] == 'C' or valor_cadastro_login[0] == 'S'
    while True:
        if VALIDACAO_CAD_LOG:
            break
        else:
            print("-"*len(opcao))
            print('\nERRO!\nDigite uma opção valida\n')
            print("-"*len(opcao))
            valor_cadastro_login = str(input(opcao)).upper().lstrip(" ")
            print("-"*len(opcao))
            VALIDACAO_CAD_LOG = valor_cadastro_login[0] == 'L' or valor_cadastro_login[0] == 'C'
    return valor_cadastro_login[0]

# Cadastrando


def cadastrando(confirmacao):
    global user
    global TASK
    confirmacao_cadastro = str(input(confirmacao)).upper().lstrip()
    validacao_cadastro = confirmacao_cadastro[0] == 'S'
    if validacao_cadastro:
        user.append(str(input('Nome: \n')))  # NOME
        user.append(str(input('Data de Nascimento: \n')))  # datanascimento
        user.append(str(input('CPF: \n')).strip('.'))  # CPF
        logradouro = str(input('Local: \n'))
        bairro = str(input('Bairro: \n'))
        cidade = str(input('Cidade: \n'))
        estado = str(input('Estado: \n'))
        user.append(f'{logradouro} - {bairro} - {cidade}/{estado}')  # ENDERECO
        user.append(str(input('Usuario: \n')))
        user.append(str(input('Senha: \n')))
        return user
    else:
        print("Voltando para o INICIO!")

# SAQUE


def sub(conta):
    global saldo
    saque_valor = float(input(conta))
    validacao_saque = saque_valor <= saldo and saque_valor > 0
    VALIDACAO_QUANTIDADE = contsaq <= 3
    if validacao_saque and VALIDACAO_QUANTIDADE:
        saldo -= saque_valor
        print(f'Saldo:\n R$: {saldo:.2f}')
        extra = f'Deposito\n{saldo:.2f}'
        extrato.append(extra)
    elif VALIDACAO_QUANTIDADE == False:
        print('Já foram feitos 3 saques')
    else:
        print('Não é existe o valor solicitado!')
    return extrato

# DEPOSITO


def soma(conta):
    print(conta)
    global saldo
    deposito_valor = float(input())
    if deposito_valor > 0:
        saldo = + deposito_valor
        extra = f'Deposito\n{saldo:.2f}'
        extrato.append(extra)
        print(f'Saldo:\n R$: {saldo:.2f}')
    return extrato

# EXTRATO


def movimentacao_conta(conta):
    print(conta)
    for e in range(len(extrato)):
        print(extrato[e])
        print(f'Saldo\nR$: {saldo:.2f}')


while True:
    opcao_cad_log = cadastro_login(
        "Digite uma opção:\n \n[L]OGIN \n[C]adastro \n[S]air\n\n --> ")
    cadastro = opcao_cad_log == 'C'
    login = opcao_cad_log == 'L'
    sair = opcao_cad_log == 'S'
    if cadastro:
        user = cadastrando('Deseja criar uma conta nova? \n')
        print(user)
        continue
    elif login:
        login_user = str(input('Digite seu Usuario: \n'))
        senha_user = str(input('Digite sua Senha: \n'))
        if TASK:
            VALIDACAO_LOGIN = user[-1] == senha_user and user[-2] == login_user
        if VALIDACAO_LOGIN:
            print('LOGADO COM SUCESSO!')
            break
        else:
            while True:
                login_user = str(
                    input('USUARIO OU LOGIN INVALIDOS!\nDigite seu Usuario: \n'))
                senha_user = str(input('Digite sua Senha: \n'))
                if VALIDACAO_LOGIN:
                    print('LOGADO COM SUCESSO!')
                    break
                else:
                    print('Usuario ou senha incorretos!')
                    continuar = str(
                        input('Quer tentar novamente: \n')).upper().lstrip(' ')
                    if continuar == 'S':
                        continue
                    else:
                        break
    elif VALIDACAO_LOGIN:
        print('LOGADO COM SUCESSO!')
        break
    elif sair:
        break

while VALIDACAO_LOGIN:
    print('''MENU
        [ D ]EPOSITAR
        [ S ]ACAR
        [ E ]XTRATO
        [ Q ]AIR DO PROGRAMA''')
    menu = (input('Escolha a opção no menu: ')).upper().lstrip(' ')
    print('-'*20)

    DEPOSITAR_MENU = menu[0] == 'D'
    SACAR_MENU = menu[0] == 'S'
    EXTRATO_MENU = menu[0] == 'E'
    SAIR_MENU = menu[0] == 'Q'

    if DEPOSITAR_MENU:
        soma('Informe o valor do Deposito: \nR$: ')
    elif SACAR_MENU:
        contsaq += 1
        if contsaq <= 3:
            sub(f'Informe o valor do Saque: \nR$:')
        else:
            print('Não é possivel fazer mais saques, foram feitos 3 saques.')
    elif EXTRATO_MENU:
        movimentacao_conta('Extrato:\n')
    elif SAIR_MENU:
        print(f'Saldo \n R$: ')
        print(saldo)
        break
    else:
        print('OPÇÃO INVALIDA')
