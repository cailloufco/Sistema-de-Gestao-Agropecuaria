def cadastrar_usuario(nome: str, senha: str, adm: bool, pessoas_cadastradas: dict):

    for nome_cadastrado in pessoas_cadastradas["nome"]:
        if nome_cadastrado == nome:
            return "Usuário já existe!"
        else:
            pessoas_cadastradas["nome"].append(nome)
            pessoas_cadastradas["senha"].append(senha)
            pessoas_cadastradas["administrador"].append(adm)
            return "Usuário cadastrado!"


def logar(nome: str, senha: str, pessoas_cadastradas: dict):
    for nome_cadastrado, senha_cadastrada, adm in zip(
        pessoas_cadastradas["nome"],
        pessoas_cadastradas["senha"],
        pessoas_cadastradas["administrador"],
    ):
        if nome == nome_cadastrado and senha == senha_cadastrada:
            return {"nome": nome, "administrador": adm, "logado": True}
    return False
