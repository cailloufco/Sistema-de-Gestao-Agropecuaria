# lista = {'nome':['caio','jose','nycole']}

# for nome in lista['nome']:
#     if nome == 'nycole':
#         print('teste')
#     print(nome)

# nome = input("Digite seu nome: ")


# if nome :
#     print("Nome digitado:", nome)
# else:
#     print("Nenhum nome foi digitado.")

# print ("print colorida \033[31m vermelho \033[0m")
# print ("print colorida \033[32m verde \033[0m")
# print ("print colorida \033[33m amarelo \033[0m")
# print ("print colorida \033[34m azul \033[0m")


# usuarios_cadastrados = {
#     'usuario':[{'nome':'Caio',
#                 'senha':'Caio123',
#                 'idade':18}]
# }

## dava pra ter usado isso daqui pra nao usar o zip

# while True:
#     op = int(input('criar usuario: 1 cria , 2 exibe:'))
#     if op == 1:
#         nome = input('digite seu nome: ')
#         senha = input('digite sua senha: ')
#         idade = int(input('digite sua idade: '))
#         usuarios_cadastrados['usuario'].append(
#             {
#                 'nome':nome,
#                 'senha':senha,
#                 'idade':idade
#             }
#         )
#     if op == 2:
#         for nome in usuarios_cadastrados['usuario']:
#             print(nome['nome'])
