from random import randint

TASK = False
VALIDACAO_LOGIN = False
user = {'nome': '',
        'logradouro': '',
        'bairro': '',
        'usuario': '',
        'senha': '',
        'contas' : dict()
        }

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
        user['nome'] = str(input('Nome:\n'))
        user['cpf'] = str(input('CPF: \n')).strip('.')
        logradouro_user = str(input('Local: \n'))
        bairro_user = str(input('Bairro: \n'))
        cidade_user = str(input('Cidade: \n'))
        estado_user = str(input('Estado: \n'))
        endereço = f'{logradouro_user} - {bairro_user} - {cidade_user}/{estado_user}'
        user['endereço'] = f'{endereço}'
        user['usuario'] = str(input('Usuario: \n'))
        user['senha'] = str(input('Senha: \n'))
        ID_0 = {'ID': 1,
                'saldo' :  0,
                'extrato' : list(),
                }
        user['contas'] = ID_0
        TASK = True
        return user
    elif True is not validacao_cadastro:
        criar_conta_bancaria = input('Deseja criar mais uma conta bancaria? \n[S]im \n[N]ão\n').upper().lstrip(' ')
        validacao_conta_bancaria = criar_conta_bancaria == 'S'
        if validacao_conta_bancaria:
            ...
    else:
        print("Voltando para o INICIO!")

# SAQUE


def sub(conta):
    global user
    saque_valor = float(input(conta))
    validacao_saque = saque_valor <=  user['1']['saldo'] and saque_valor > 0
    VALIDACAO_QUANTIDADE = contsaq <= 3
    if validacao_saque and VALIDACAO_QUANTIDADE:
        saldo = int(user['contas']['ID_0']['saldo'])
        saldo -= saque_valor
        print(f'Saldo:\n R$: {saldo:.2f}')
        extra = f'Deposito\n{saldo:.2f}'
        int(user['contas']['ID_0']['extrato']).append(extra)
    elif VALIDACAO_QUANTIDADE == False:
        print('Já foram feitos 3 saques')
    else:
        print('Não é existe o valor solicitado!')
    return user

# DEPOSITO


def soma(conta):
    print(conta)
    global saldo
    deposito_valor = float(input())
    if deposito_valor > 0:
        saldo = int(user['contas']['ID_0']['saldo'])
        saldo = + deposito_valor
        extra = f'Deposito\n{saldo:.2f}'
        int(user['contas']['ID_0']['extrato']).append(extra)
        print(f'Saldo:\n R$: {saldo:.2f}')
    return user

# EXTRATO


def movimentacao_conta(conta):
    print(conta)
    for e in range(len(user['extrato'])):
        print(int(user['contas']['ID_0']['extrato'])[e])
        saldo = int(user['contas']['ID_0']['saldo'])
        print(f'Saldo\nR$: {saldo:.2f}')


while True:
    opcao_cad_log = cadastro_login(
        "Digite uma opção:\n \n[L]OGIN \n[C]adastro \n[S]air\n\n --> ")
    cadastro = opcao_cad_log == 'C'
    login = opcao_cad_log == 'L'
    sair = opcao_cad_log == 'S'
    if cadastro:
        user = cadastrando('Deseja abrir sua primeira conta? \n')
    elif login:
        login_user = str(input('Digite seu Usuario: \n'))
        senha_user = str(input('Digite sua Senha: \n'))
        if TASK:
            VALIDACAO_LOGIN = user['senha'] == senha_user and user['usuario'] == login_user
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
    for c in user['contas']:
        ids = user['contas'][c]
        print(f'Conta --> {ids}')
        saldo = user['contas']['ID_0']['saldo']
        print(f'Saldo\nR$: {saldo:.2f}')
    conta = input('Qual conta deseja acessar?\n')
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
        saldo = int(user['contas']['ID_0']['saldo'])
        print(f'{saldo:.2f}')
        break
    else:
        print('OPÇÃO INVALIDA')
