import time

class User:
    def __init__(self, nome, cpf,endereco,usuario,senha,conta):
        self._nome = nome
        self._cpf = cpf
        self._endereco = endereco
        self._usuario = usuario
        self._senha = senha
        self._conta = conta
        print('Cadastro efetuado com SUCESSO!')
        print('_'*10)

    @property
    def usuario(self):
        return self._usuario

    @property
    def senha(self):
        return self._senha
    
class conta:
    def __init__(self,saldo,extrato):
        self._saldo = saldo
        self._extrato = extrato
    
    @property
    def saldo(self):
        return self._saldo
    
    def get_soma(self,soma):
        self._saldo += soma
        print(f'Deposito efetuado com SUCESSO! \nR$: {soma:.2f}')
        print('_'*10)
        self._extrato.append(f'Deposito:\n R$: {soma}')
        print(f'Saldo\n --> R$: {ID_1.saldo:.2f}')
        print('-'*14)
        return self._saldo
        
    def get_sub(self,sub):
        self._saldo -= sub
        print(f'Saque efetuado com SUCESSO! \nR$: {sub:.2f}')
        print('_'*10)
        self._extrato.append(f'Saque:\n R$: {sub}')
        print(f'Saldo\n --> R$: {ID_1.saldo:.2f}')
        print('-'*14)
        return self._saldo

    def ext(self):
        for extr in self._extrato:
            print(extr)
        print(f'Saldo\n --> R$: {ID_1.saldo:.2f}')
        print('-'*14)
            
task_login = False

while True:
    try:
        menu_escolha = (input("Digite uma opção:\n \n[L]OGIN \n[C]adastro \n[S]air\n\n --> ").lstrip(' ').upper())
        cadastro = menu_escolha == 'C'
        login = menu_escolha == 'L'
        sair = menu_escolha == 'S'
        print('-'*14)
        print('Processando...')
        time.sleep(1)
        print(3)
        time.sleep(1)
        print(2)
        time.sleep(1)
        print(1)
        time.sleep(1)
        if cadastro:
            user_1 = User(input('Nome:\n'),
                        input('CPF:'),
                        input('Endereço:\n'),
                        input('Usuário:\n'),
                        input('Senha:\n'),
                        '0001')
        elif login:
            user_input_task = input('Usuario:\n-->')
            senha_input_task = input('Senha:\n-->')
            task_user = user_1.usuario == user_input_task
            task_senha = user_1.senha == senha_input_task
            task_login = task_senha and task_user
            print('Acessando Conta...')
            time.sleep(1)
            print(3)
            time.sleep(1)
            print(2)
            time.sleep(1)
            print(1)
            time.sleep(1)
            if task_login:
                print('Login efetuado com SUCESSO!')
                print('_'*10)
                break
            else:
                print('USUARIO OU SENHA INCORRETOS!\nVoltando para o inicio.')
        elif sair:
            break
    except:
        print('ERRO INESPERADO!')

ID_1 = conta(0.00,list())

while task_login:
    try:
        print('''MENU
                [ D ]EPOSITAR
                [ S ]ACAR
                [ E ]XTRATO
                [ Q ]AIR DO PROGRAMA''')
        menu = (input('Escolha a opção no menu: ')).upper().lstrip(' ')
        print('-'*14)
        DEPOSITAR_MENU = menu[0] == 'D'
        SACAR_MENU = menu[0] == 'S'
        EXTRATO_MENU = menu[0] == 'E'
        SAIR_MENU = menu[0] == 'Q'

        if DEPOSITAR_MENU:
            ID_1.get_soma(float(input('Valor do DEPOSITO: \n --> R$:')))
        elif SACAR_MENU:
            ID_1.get_sub(float(input('Valor que deseja SACAR: \n --> R$:')))
        elif EXTRATO_MENU:
            ID_1.ext()
        elif SAIR_MENU:
            print(f'Saldo\n --> R$: {ID_1.saldo:.2f}')
            print('Saindo do programa...')
            time.sleep(1)
            print(3)
            time.sleep(1)
            print(2)
            time.sleep(1)
            print(1)
            print('Volte sempre!!!')
            break
    except:
        print('ERRO INESPERADO!')
   



