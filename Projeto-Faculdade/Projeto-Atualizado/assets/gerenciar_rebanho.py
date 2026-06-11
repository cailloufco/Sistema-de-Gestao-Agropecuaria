from time import sleep


def exibir_menu_de_gerenciar_rebanho():
    print(
        f'{"\n"*4}Gerenciar Rebanho\n 1 - Cadastrar Animal\n 2 - Visualizar Animais\n 3 - Editar Animal\n 4 - Excluir Animal\n 0 - Voltar ao Menu Anterior\n'
    )


def cadastrar_animal(cadastro: dict):
    id = max(cadastro["animais"]["id"]) + 1

    nome = input("Digite o nome do animal: ")

    idade = int(input("Digite a idade do animal: "))
    raça = input("Digite a raça do animal: ")
    peso = float(input("Digite o peso do animal: "))
    tipo = input("Digite o tipo do animal: ")
    genero = input("Digite o gênero do animal: ")
    status = input("Digite o status do animal: ")
    op = input("O animal está disponível para venda? (S/N): ").upper()
    if op == "S":
        preco = float(input("Digite o preço do animal: "))
    else:
        preco = "Indisponivel"

    cadastro["animais"].append(
        {
            "id": id,
            "nome": nome,
            "idade": idade,
            "raça": raça,
            "peso": peso,
            "tipo": tipo,
            "genero": genero,
            "preco": preco,
            "status": status,
        }
    )
    print(f"Animal {nome} da raça {raça} cadastrado com sucesso!")


def exibir_animais(cadastro: dict, usuario_logado: dict):
    print(
        f'{"\n"*4}Qual animal você deseja visualizar, {usuario_logado["nome"]}? \n     *****MENU*****\n 1 - Busca por ID do animal\n 2 - Buscar por Tipo dos animais\n 3 - Buscar por status\n 4 - Verificar animais à venda\n 0 - Sair da busca\n'
    )
    op = int(input("-> "))
    if op == 1:
        id = int(input("Digite o ID do animal que deseja buscar: "))
        for animal in cadastro["animais"]:
            if animal["id"] == id:
                print(
                    f'ID: {animal["id"]} | Nome: {animal["nome"]} | Raça: {animal["raça"]} | Tipo: {animal["tipo"]} | Preço: {animal["preco"]} | Status: {animal["status"]}'
                )
                break
        else:
            print(f"Animal ID {id} não encontrado.")
    elif op == 2:
        tipo = input("Digite o tipo do animal que deseja buscar: ")
        animal_encontrado = False
        for animal in cadastro["animais"]:
            if animal["tipo"] == tipo:
                print(
                    f'ID: {animal["id"]} | Nome: {animal["nome"]} | Raça: {animal["raça"]} | Tipo: {animal["tipo"]} | Preço: {animal["preco"]} | Status: {animal["status"]}'
                )
                animal_encontrado = True
        if not animal_encontrado:
            print(f"Animais do tipo {tipo} não encontrados.")
    elif op == 3:
        status = input("Digite o status do animal que deseja buscar: ")
        animal_encontrado = False
        for animal in cadastro["animais"]:
            if animal["status"] == status:
                print(
                    f'ID: {animal["id"]} | Nome: {animal["nome"]} | Raça: {animal["raça"]} | Tipo: {animal["tipo"]} | Preço: {animal["preco"]} | Status: {animal["status"]}'
                )
                animal_encontrado = True
        if not animal_encontrado:
            print(f"Animais com status {status} não encontrados.")
    elif op == 4:
        animais_a_venda = False
        for animal in cadastro["animais"]:
            if animal["preco"] != "Indisponivel":
                print(
                    f'ID: {animal["id"]} | Nome: {animal["nome"]} | Raça: {animal["raça"]} | Tipo: {animal["tipo"]} | Preço: {animal["preco"]} | Status: {animal["status"]}'
                )
                animais_a_venda = True
        if not animais_a_venda:
            print("Nenhum animal disponível para venda encontrado.")
    elif op == 0:
        print("Saindo da busca...")
        sleep(1.6)
    else:
        print("Opção inválida! Saindo da busca...")
        sleep(1.6)


def editar_animal(cadastro: dict):
    id = int(input("Digite o ID do animal que deseja editar: "))
    for animal in cadastro["animais"]:
        if animal["id"] == id:
            print(
                f'ID: {animal["id"]} | Nome: {animal["nome"]} | Raça: {animal["raça"]} | Tipo: {animal["tipo"]} | Preço: {animal["preco"]} | Status: {animal["status"]}'
            )
            print(
                "Digite os novos dados do animal (deixe em branco para manter o valor atual):"
            )
            nome = input("Nome: ")
            idade = int(input("Idade: "))
            raça = input("Raça: ")
            peso = float(input("Peso: "))
            tipo = input("Tipo: ")
            genero = input("Gênero: ")
            status = input("Status: ")

            op = input("O animal está disponível para venda? (S/N): ").upper()
            if op == "S":
                preco = float(input("Digite o preço do animal: "))
            else:
                preco = "Indisponivel"

            if nome:
                animal["nome"] = nome
            if idade:
                animal["idade"] = idade
            if raça:
                animal["raça"] = raça
            if peso:
                animal["peso"] = peso
            if tipo:
                animal["tipo"] = tipo
            if genero:
                animal["genero"] = genero
            if status:
                animal["status"] = status
            animal["preco"] = preco

            print(f"Animal ID {id} atualizado com sucesso!")


def excluir_animal(cadastro: dict):
    id = int(input("Qual animal deseja excluir? (Digite o ID): "))
    for animal in cadastro["animais"]:
        if animal["id"] == id:
            print(f"Você tem certeza que deseja excluir o animal ID {id}? (S/N)")
            confirmacao = input("-> ").upper()
            if confirmacao == "S":
                cadastro["animais"].remove(animal)
                print(f"Animal ID {id} excluído com sucesso!")
                break
            else:
                print("Exclusão cancelada.")
                break
    else:
        print(f"Animal ID {id} não encontrado.")
