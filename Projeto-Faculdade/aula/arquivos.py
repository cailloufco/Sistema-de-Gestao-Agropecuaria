# open (aonde o aquivo vai aparecer ex: '/download/projeto/qualquer-coisa/arquivo.txt' , depois usa a letra que represanta o modo que o arquivo estára sendo aberto)

# w - sobrescreve oque está escrito
# a - atualiza oque está dentro do arquivo
# r - leitura de arquivos

pessoas_cadastradas = []
arquivo = open('/media/nti0029/ESD-USB/Projeto-Faculdade/aula/pedido.txt' , 'r')
pessoas = arquivo.readline()
arquivo.close()
print(pessoas)