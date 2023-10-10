saldo = 0
extrato = ''

while True:
  print('''MENU
    [ D ]EPOSITAR
    [ S ]ACAR
    [ E ]XTRATO
    [ Q ]AIR DO PROGRAMA''')
  menu = (input('Escolha a opção no menu: '))
  print('-'*20)
  if menu in 'Dd':
    valor = float(input("Digite o valor do depósito: "))
    if valor > 0:
      saldo += valor
      extrato += f'Deposito feito: \nR${valor:.2f}\n'
      print(f'Saldo:\n R$: {saldo}')
    else:
      print('Operação falhou! O valor informado está invalido')
      continue
  elif menu in 'Ss':
    valor = float(input("Digite o valor que ira retirar: "))
    if valor <= saldo and valor <= 500:
      saldo -= valor
      extrato += f'Saque de feito: \nR${valor:.2f}\n'
      print(f'Saldo:\n R$: {saldo}')
    elif valor > 500:
      print('Operação falhou! Permitido tirar no maximo R$: 500,00')
    else:
      print('Operação falhou! Conta não possuí o valor requerido!')
      continue
  elif menu in 'Ee':
    print(extrato)
    print(f'Saldo:\n R$: {saldo}')
  elif menu in 'Qq':
    print('Obrigado pela preferência, volte sempre!')
    break
  else:
      print('Operação falhou! Digite uma opção valida!')
      continue
print('FIM DO PROGRAMA')