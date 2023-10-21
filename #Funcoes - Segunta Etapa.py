saldo = 0
extrato = list()
contsaq = 0


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


def movimentacao_conta(conta):
    print(conta)
    for e in range(len(extrato)):
        print(extrato[e])
        print(f'Saldo\nR$: {saldo:.2f}')


while True:
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
        contsaq +=1
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
