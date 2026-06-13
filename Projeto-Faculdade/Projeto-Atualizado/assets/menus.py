def mostrar_cabecalho_tela(titulo: str):
    print("\n" + "=" * 60)
    print(titulo.center(60))
    print("=" * 60)


def menu_adm(usuario_logado: dict):
    mostrar_cabecalho_tela("MENU ADMINISTRATIVO")
    print(f"Bem-vindo, {usuario_logado['nome']}\n")
    print(" 1 - Gerenciar Rebanho")
    print(" 2 - Gerenciar Produção e Derivados")
    print(" 3 - Gerenciar Estoque de Ração")
    print(" 4 - Visualizar Pedidos de Compra")
    print(" 5 - Notificações")
    print(" 0 - Menu de Cadastro")
    print("=" * 60)


def menu_cliente(usuario_logado: dict):
    mostrar_cabecalho_tela("MENU CLIENTE")
    print(f"Bem-vindo, {usuario_logado['nome']}\n")
    print(" 1 - Comprar")
    print(" 2 - Visualizar Estoque")
    print(" 3 - Agendar Retirada/Transporte")
    print(" 4 - Ver Meus Agendamentos")
    print(" 5 - Fazer Pedido de Compra")
    print(" 6 - Ver Meus Pedidos")
    print(" 0 - Sair")
    print("=" * 60)

def mostrar_menu_inicial():
    print("\n" + "=" * 60)
    print("SISTEMA DE GESTÃO AGROPECUÁRIA".center(60))
    print("=" * 60)
    print(" 1 - Logar")
    print(" 2 - Cadastrar")
    print(" 0 - Encerrar")
    print("=" * 60)
