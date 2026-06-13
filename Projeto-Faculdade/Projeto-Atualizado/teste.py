from datetime import datetime

cadastro = {
    "animais": [
        {
            "id": "00126-A",
            "nome": "Belinha",
            "idade": 3,
            "raça": "Holandesa",
            "peso": 500,
            "tipo": "Vaca",
            "genero": "Fêmea",
            "preco": 1500,
            "status": "Doente",
            "ano": "2023",
            "lote": "A",
        }
    ],
    "produtos": [
        {
            "id": 0,
            "nome": "Leite",
            "quantidade": 100,
            "preco": 2.5,
            "status": "Disponível",
        }
    ],
    "racao": [
        {
            "id": 0,
            "funcao": "Alimentar os animais",
            "nome": "Ração para bovinos",
            "quantidade": 50,
            "limiar_de_estoque": 10,
        }
    ],
}

while True:

    ano = input("Digite o ano de nascimento: ")
    lote = input("Digite o lote do animal: ").upper()

    contador = 1

    for animal in cadastro["animais"]:
        if animal["ano"] == ano and animal["lote"] == lote:
            contador += 1

    numero = str(contador).zfill(3)
    ano_formatado = ano[-2:]
    codigo = f"{numero}{ano_formatado}-{lote}"

    nome = input("Digite o nome do animal: ")
    raça = input("Digite a raça do animal: ")
    peso = float(input("Digite o peso do animal: "))
    tipo = input("Digite o tipo do animal: ")
    genero = input("Digite o gênero do animal: ")
    status = input("Digite o status do animal: ")

    op = input("O animal está disponível para venda? (S/N): ").upper()

    if op == "S":
        preco = float(input("Digite o preço do animal: "))
    else:
        preco = "Indisponível"

    cadastro["animais"].append(
        {
            "id": codigo,
            "nome": nome,
            "idade": datetime.now().year - int(ano),
            "raça": raça,
            "peso": peso,
            "tipo": tipo,
            "genero": genero,
            "preco": preco,
            "status": status,
            "ano": ano,
            "lote": lote,
        }
    )

    print("\nAnimal cadastrado com sucesso!")
    print(f"Nome: {nome}")
    print(f"Código: {codigo}")

    continuar = input("\nCadastrar outro animal? (S/N): ").upper()

    if continuar != "S":
        break
