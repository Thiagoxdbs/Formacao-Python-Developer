user = {'nome': '',
        'logradouro': '',
        'bairro': '',
        'usuario': '',
        'senha': '',
        'contas' : {'ID_0': {'ID': 0,
                            'saldo' :  0,
                            'extrato' : list()},
                    'ID_1': {'ID': 0,
                            'saldo' :  0,
                            'extrato' : list()},
                    'ID_2': {'ID': 0,
                            'saldo' :  0,
                            'extrato' : list()},
                    'ID_3': {'ID': 0,
                            'saldo' :  0,
                            'extrato' : list()},
                    'ID_4': {'ID': 0,
                            'saldo' :  0,
                            'extrato' : list()},
                    'ID_5': {'ID': 0,
                            'saldo' :  0,
                            'extrato' : list()},
                    'ID_6': {'ID': 0,
                            'saldo' :  0,
                            'extrato' : list()},
                    'ID_7': {'ID': 0,
                            'saldo' :  0,
                            'extrato' : list()},
                    'ID_8': {'ID': 0,
                            'saldo' :  0,
                            'extrato' : list()},
                    'ID_9': {'ID': 0,
                            'saldo' :  0,
                            'extrato' : list()}}
        }
TASK = False
VALIDACAO_LOGIN = False
contsaq = 0
CONTA_TRUE = True
LOGADO = True
CONTAS_QUANTIDADE = 0
CONTAS_FOR = 0

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
    global CONTAS_QUANTIDADE
    global CONTAS_FOR
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
        user['contas']['ID_0'] = {'ID': 1,
                'saldo' :  0,
                'extrato' : list(),
                }
        CONTAS_QUANTIDADE = 1
        TASK = True
        return user
    elif True is not validacao_cadastro:
        criar_conta_bancaria = input('Deseja criar mais uma conta bancaria? \n[S]im \n[N]ão\n').upper().lstrip(' ')
        validacao_conta_bancaria = criar_conta_bancaria == 'S'
        if validacao_conta_bancaria:
            for c in user['contas']:
                if CONTAS_QUANTIDADE == CONTAS_FOR:
                    user['contas'][c]['ID'] = CONTAS_QUANTIDADE
                    print(f'Conta criada com SUCESSO! --> {c}')
                    saldo = user['contas'][c]['saldo']
                    print(f'Saldo\nR$: {saldo:.2f}')
                    CONTAS_QUANTIDADE += 1
                CONTAS_FOR += 1
            CONTAS_FOR = 0

    else:
        print("Voltando para o INICIO!")

# SAQUE


def sub(conta):
    global user
    global VALIDACAO_QUANTIDADE
    VAL = True
    saque_valor = float(input(conta))
    #VERIFICAR
    CONT = 0
    for c in user['contas']:
        if CONTA_ID == CONT:
            validacao_saque = saque_valor <=  user['contas'][c]['saldo'] and saque_valor > 0
        CONT += 1
    VALIDACAO_QUANTIDADE = contsaq <= 3
    if validacao_saque and VALIDACAO_QUANTIDADE:
        for c in user['contas']:
            for e in range(9):
                if CONTA_ID == e and VAL:
                    user['contas'][c]['saldo'] -= saque_valor
                    saldo = int(user['contas'][c]['saldo'])
                    print(f'Saldo:\n R$: {saldo:.2f}')
                    extrato = f'Deposito\n{saldo:.2f}'
                    user['contas'][c]['extrato'].append(extrato)
                    VAL = False
    elif VALIDACAO_QUANTIDADE == False:
        print('Já foram feitos 3 saques')
    else:
        print('Não é existe o valor solicitado!')
    return user

# DEPOSITO


def soma(conta):
    print(conta)
    global saldo
    VAL = True
    deposito_valor = float(input())
    if deposito_valor > 0:
        for c in user['contas']:
            for e in range(9):
                if CONTA_ID == e and VAL:
                    user['contas'][c]['saldo'] += deposito_valor
                    saldo = user['contas'][c]['saldo']
                    extrato = f'Deposito\n{saldo:.2f}'
                    user['contas'][c]['extrato'].append(extrato)
                    print(f'Saldo:\n R$: {saldo:.2f}')
                    VAL = False
    return user

# EXTRATO


def movimentacao_conta(conta):
    print(conta)
    cont = 0
    for e in user['contas']:        
        if CONTA_ID == cont:
            extra = user['contas'][e]['extrato'][cont]
            print(extra)
        cont += 1
    saldo = int(user['contas'][e]['saldo'])
    print(f'Saldo\nR$: {saldo:.2f}')
    return user

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
    CONTAGEM = 0
    if LOGADO:
        for c in user['contas']:
            CONTAGEM += 1
            VALIDACAO_Q_CONTA = int(user['contas'][c]['ID']) > 0
            if VALIDACAO_Q_CONTA:
                print(f'Conta --> {c} - Digite [{CONTAGEM}]')
                saldo = user['contas'][c]['saldo']
                print(f'Saldo\nR$: {saldo:.2f}')
                LOGADO = False
    if CONTA_TRUE:
        conta = int(input('Qual conta deseja acessar?\n'))
        CONTA_TRUE = False
    CONTA_ID = conta - 1
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
        for c in user['contas']:
            if CONTA_ID == c:
                saldo = int(user['contas'][c]['saldo'])
                print(f'{saldo:.2f}')
        break
    else:
        print('OPÇÃO INVALIDA')
