import os

restaurantes = []

def nome_app():
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
""")

def menu_app():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair do programa')
  
def opcao_invalida():
    print('opcao invalida!')  
    input('digite uma tecla para voltar ao menu anterior!')
    main()

def retorne_ao_menu():
    input('digite uma tecla para voltar ao menu principal')
    main()

def cadastrar_restaurante():
    os.system('cls')
    print('cadastro de novos restaurantes\n')
    nome_do_restaurante = input('digite o nome do restaurante que deseja cadastrar: ')
    restaurantes.append(nome_do_restaurante)
    print(f'O restaurante:{nome_do_restaurante} foi cadastrado com sucesso!')
    retorne_ao_menu()

def listando_restaurante():
    for restaurante in restaurantes:
        print(f'.{restaurante}')
    retorne_ao_menu()

def opcoes_app():
    try:
        opcao_digitada = int(input('Digite uma opção: '))
        if opcao_digitada == 1:
            cadastrar_restaurante()
        elif opcao_digitada == 2:
            listando_restaurante()
        elif opcao_digitada == 3:
            print('Ativar Restaurante')
        elif opcao_digitada == 4:
            finalizando_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()    

def finalizando_app():
    os.system('cls')
    print('saindo do programa...')

def main():
    os.system('cls')
    nome_app()
    menu_app()
    opcoes_app()
    
if __name__=='__main__':
    main()
