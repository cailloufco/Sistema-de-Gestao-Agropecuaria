def menu_adm (usuario_logado:dict):
    print(f"Bem Vindo {usuario_logado['nome']}!")
    print(
            f'{"\n"*4}Bem-vindo, {usuario_logado["nome"]} \n     *****MENU*****\n 1 - Gerenciar Rebanho\n 2 - Gerenciar Produção e Derivados\n 3 - Gerenciar Estoque de Ração\n 4 - Visualizar Pedidos de Compra\n 0 - Menu de Cadastro\n'
        )