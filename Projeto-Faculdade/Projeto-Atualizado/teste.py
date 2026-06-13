pedido_de_compra = {
    "pedidos": [
        {
            "nome_cliente": "Carlos",
            "nome_produto": "Leite",
            "item_id": 0,
            "status_pedido": "Aguardo",
            "criado_em": [
                {"ano": 2026, "mes": 10, "dia": 16, "hora": 17, "minuto": 13}
            ],
            "quantidade": 120,
        }
    ]
}
usuario_logado = {"nome": None, "administrador": None, "logado": False}


def permitir_pedidos(pedido_de_compra: dict, usuario_logado: dict):
    while True:
        print(f"Que pedido deseja visualizar, {usuario_logado['nome']}?")
        print(
            "1 - Visualizar Pedidos em Aguardo\n"
            "2 - Visualizar Pedidos Confirmados\n"
            "3 - Visualizar Pedidos Recusados\n"
            "0 - Sair"
        )

        op = int(input("-> "))

        if op == 0:
            return

        elif op == 1:

            pedidos_aguardo = []

            for indice, pedido in enumerate(pedido_de_compra["pedidos"]):

                if pedido["status_pedido"] == "Aguardo":

                    pedidos_aguardo.append(indice)

                    data = pedido["criado_em"][0]

                    print(
                        f"[{len(pedidos_aguardo)-1}] "
                        f"NOME: {pedido['nome_cliente']} | "
                        f"PRODUTO: {pedido['nome_produto']} | "
                        f"ID PRODUTO: {pedido['item_id']} | "
                        f"QUANTIDADE: {pedido['quantidade']} | "
                        f"STATUS: {pedido['status_pedido']} | "
                        f"CRIADO EM: "
                        f"{data['ano']}/{str(data['mes']).zfill(2)}/{str(data['dia']).zfill(2)} "
                        f"{str(data['hora']).zfill(2)}:{str(data['minuto']).zfill(2)}"
                    )

            if len(pedidos_aguardo) == 0:
                print("Não há pedidos aguardando aprovação.")
                continue

            escolha = int(input("\nDigite o índice do pedido que deseja analisar: "))

            if escolha < 0 or escolha >= len(pedidos_aguardo):
                print("Pedido inválido!")
                continue

            indice_real = pedidos_aguardo[escolha]

            print("\n1 - Confirmar Pedido\n" "2 - Recusar Pedido\n" "0 - Cancelar")

            decisao = int(input("-> "))

            if decisao == 1:
                pedido_de_compra["pedidos"][indice_real]["status_pedido"] = "Confirmado"
                print("Pedido confirmado com sucesso!")
                continue

            elif decisao == 2:
                pedido_de_compra["pedidos"][indice_real]["status_pedido"] = "Recusado"
                print("Pedido recusado com sucesso!")
                continue

            elif decisao == 0:
                break

            else:
                print("Opção inválida!")
                continue
        elif op == 2:
            for pedido in pedido_de_compra["pedidos"]:
                if pedido["status_pedido"] == "Confirmado":
                    print(
                        f"NOME: {pedido['nome_cliente']} | "
                        f"PRODUTO: {pedido['nome_produto']} | "
                        f"ID PRODUTO: {pedido['item_id']} | "
                        f"QUANTIDADE: {pedido['quantidade']} | "
                        f"STATUS: {pedido['status_pedido']} | "
                        f"CRIADO EM: "
                        f"{data['ano']}/{str(data['mes']).zfill(2)}/{str(data['dia']).zfill(2)} "
                        f"{str(data['hora']).zfill(2)}:{str(data['minuto']).zfill(2)}"
                    )
        elif op == 3:
            for pedido in pedido_de_compra["pedidos"]:
                if pedido["status_pedido"] == "Recusado":
                    print(
                        f"NOME: {pedido['nome_cliente']} | "
                        f"PRODUTO: {pedido['nome_produto']} | "
                        f"ID PRODUTO: {pedido['item_id']} | "
                        f"QUANTIDADE: {pedido['quantidade']} | "
                        f"STATUS: {pedido['status_pedido']} | "
                        f"CRIADO EM: {data['ano']}/{str(data['mes']).zfill(2)}/{str(data['dia']).zfill(2)} {str(data['hora']).zfill(2)}:{str(data['minuto']).zfill(2)}"
                        
                        
                    )


permitir_pedidos(pedido_de_compra, usuario_logado)
