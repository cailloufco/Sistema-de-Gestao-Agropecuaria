from assets import menus

from reportlab.lib.styles import getSampleStyleSheet

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table
from reportlab.lib.units import cm
from reportlab.platypus import Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4

from rich import print
from rich.table import Table as tabelinha
from rich.console import Console
from rich import box

from time import sleep

def gerar_relatorios_animais(cadastro: dict):

    pdf = SimpleDocTemplate("relatorio_animais.pdf")

    styles = getSampleStyleSheet()

    conteudo = []

    conteudo.append(Paragraph("Relatório Fazenda Sertão", styles["Title"]))

    conteudo.append(Paragraph("Animais cadastrados", styles["Heading2"]))

    conteudo.append(Spacer(1, 20))

    dados = [
        ["ID", "Nome", "Raça", "Idade", "Peso", "Genero", "Preço", "Status"],
    ]
    """
    "id": "00123-A",
    "nome": "Belinha",
    "idade": 3,
    "raça": "Nelore",
    "peso": 324,
    "tipo": "Vaca",
    "genero": "F",
    "preco": 3.370,
    "status": "Doente",
    "ano": "2023",
    "lote": "A",
    """
    for animal in cadastro["animais"]:
        dado = [
            animal["id"],
            animal["nome"],
            animal["raça"],
            animal["idade"],
            animal["peso"],
            animal["genero"],
            str(animal["preco"]) + "R$",
            animal["status"],
        ]
        dados.append(dado)

    largura, altura = A4

    tabela = Table(dados)
    tabela.hAlign = "LEFT"
    tabela.setStyle(
        TableStyle(
            [
                ("ALIGN", (0, 0), (-1, -1), "CENTER"),
                # aumenta o espaço dentro das células
                ("LEFTPADDING", (0, 0), (-1, -1), 15),
                ("RIGHTPADDING", (0, 0), (-1, -1), 15),
                ("TOPPADDING", (0, 0), (-1, -1), 8),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
                ("GRID", (0, 0), (-1, -1), 1.3, colors.black),
            ]
        )
    )

    conteudo.append(tabela)

    pdf.build(conteudo)

    print("[bold italic light_green]Relatorio dos Animais Gerado ![/]")


def gerar_relatorios_produtos(cadastro: dict):

    pdf = SimpleDocTemplate("relatorio_produtos.pdf")

    styles = getSampleStyleSheet()

    conteudo = []

    conteudo.append(Paragraph("Relatório Fazenda Sertão", styles["Title"]))

    conteudo.append(Paragraph("Animais cadastrados", styles["Heading2"]))

    conteudo.append(Spacer(1, 20))

    dados = [["ID", "Nome", "Quantidade", "Preco", "Status"]]
    """
     "id": 1,
            "nome": "Queijo",
            "quantidade": 52,
            "preco": 5.99,
            "status": "Disponível",
    """
    for produto in cadastro["produtos"]:
        dado = [
            produto["id"],
            produto["nome"],
            produto["quantidade"],
            str(produto["preco"]) + "R$",
            produto["status"],
        ]
        dados.append(dado)
    from reportlab.lib.pagesizes import A4

    largura, altura = A4

    tabela = Table(dados)
    tabela.hAlign = "LEFT"
    tabela.setStyle(
        TableStyle(
            [  # padding : 8, 15
                ("ALIGN", (0, 0), (-1, -1), "CENTER"),
                # aumenta o espaço dentro das células
                ("LEFTPADDING", (0, 0), (-1, -1), 15),
                ("RIGHTPADDING", (0, 0), (-1, -1), 15),
                ("TOPPADDING", (0, 0), (-1, -1), 8),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
                ("GRID", (0, 0), (-1, -1), 1.3, colors.black),
            ]
        )
    )

    conteudo.append(tabela)

    pdf.build(conteudo)

    print("[bold italic light_green]Relatorio dos Produtos Gerado ![/]")


def registro_de_auditoria(registro_de_auditoria: list):
    pdf = SimpleDocTemplate("registro_de_auditoria.pdf")
    styles = getSampleStyleSheet()
    conteudo = []
    conteudo.append(Paragraph("Relatório Fazenda Sertão", styles["Title"]))
    conteudo.append(Paragraph("Registro de Auditoria", styles["Heading3"]))
    conteudo.append(Spacer(1, 20))
    dados = [["Registro"]]

    console = Console()
    tabelaRich = tabelinha(title="[italic bold]Registro de Auditoria[/]")
    tabelaRich.add_column("Registro" , justify="center")


    """
     "id": 1,
            "nome": "Queijo",
            "quantidade": 52,
            "preco": 5.99,
            "status": "Disponível",
    """
    if not registro_de_auditoria:
        print("Nenhum Registro Capturado...")
        return
    for registro in registro_de_auditoria:
        dado = [
            registro
        ]
        tabelaRich.add_row(registro)
        dados.append(dado)
    
    

    tabela = Table(dados)
    tabela.hAlign = "LEFT"
    tabela.setStyle(
        TableStyle(
            [  # padding : 8, 15
                ("ALIGN", (0, 0), (-1, -1), "CENTER"),
                # aumenta o espaço dentro das células
                ("LEFTPADDING", (0, 0), (-1, -1), 15),
                ("RIGHTPADDING", (0, 0), (-1, -1), 15),
                ("TOPPADDING", (0, 0), (-1, -1), 8),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
                ("GRID", (0, 0), (-1, -1), 1.3, colors.black),
            ]
        )
    )

    conteudo.append(tabela)


    console.print(tabelaRich)

    print("Você deseja o PDF do Registro de Auditoria? ( S - N )")
    op = input('->').upper()

    if op == "S":
        pdf.build(conteudo)

        print("[bold italic light_green]Registro de Auditoria Gerado ![/]")
        sleep(1.2)

