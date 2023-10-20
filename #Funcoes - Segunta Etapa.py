saldo = 0
extrato = ''
contsaq = 0

#função saque
def sub(conta):
    saque_valor = float(input())
    validacao_saque =  saque_valor <= saldo and saque_valor > 0
    VALIDACAO_QUANTIDADE = contsaq <= 3
    if validacao_saque and VALIDACAO_QUANTIDADE:
        saldo =- saque_valor
        print(f'Saldo:\n R$: {saldo:.2f}')
    elif VALIDACAO_QUANTIDADE == False:
        print('Já foram feitos 3 saques')
    else:
        print('Não é existe o valor solicitado!')
    return saldo
def soma(conta):
    deposito_valor = float(input())
    if deposito_valor > 0:
        saldo =+ deposito_valor
        extrato += f'Deposito feito: \nR${deposito_valor:.2f}\n'
        print(f'Saldo:\n R$: {saldo:.2f}')
    return saldo
def movimentacao_conta(conta):
    print(extrato)
    print(f'Saldo:\n R$: {saldo:.2f}')

while True:
    print('''MENU
        [ D ]EPOSITAR
        [ S ]ACAR
        [ E ]XTRATO
        [ Q ]AIR DO PROGRAMA''')
    menu = (input('Escolha a opção no menu: ')).upper()
    print('-'*20)

    DEPOSITAR_MENU = menu[0] == 'D'
    SACAR_MENU = menu[0] == 'S'
    EXTRATO_MENU = menu[0] == 'E'
    SAIR_MENU = menu[0] == 'Q'
    
    if DEPOSITAR_MENU:
        ...
    elif SACAR_MENU:
        ...
    elif EXTRATO_MENU:
        ...
    elif SAIR_MENU:
        ...
    else: