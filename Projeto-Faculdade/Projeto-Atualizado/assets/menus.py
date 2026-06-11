def menu_adm(usuario_logado: dict):
    print(f"Bem Vindo {usuario_logado['nome']}!")
    print(
        f'{"\n"*4}Bem-vindo, {usuario_logado["nome"]} \n     *****MENU*****\n 1 - Gerenciar Rebanho\n 2 - Gerenciar Produção e Derivados\n 3 - Gerenciar Estoque de Ração\n 4 - Visualizar Pedidos de Compra\n 5 - Notificações\n 0 - Menu de Cadastro\n'
    )


def menu_cliente(usuario_logado: dict):
    print(
        f'{"\n"*4}Bem-vindo, {usuario_logado["nome"]} \n     *****MENU CLIENTE*****\n 1 - Comprar\n 2 - Visualizar Estoque\n 3 - Agendar Retirada/Transporte\n 4 - Ver Meus Agendamentos\n 5 - Fazer Pedido de Compra\n 6 - Ver Meus Pedidos\n 0 - Sair\n'
    )
