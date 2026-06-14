from rich import print
from rich.panel import Panel
from rich import box
import time
from datetime import datetime
from assets import menus
from rich import print
from rich.table import Table
from rich.console import Console



console = Console()
table = Table(title='random')
table.add_column("ID")
table.add_column("NOME")
table.add_column("FUNÇÃO")
table.add_column("QUANTIDADE")
table.add_column("LIMIAR DO ESTOQUE")

table.add_row('12'+'teste', 'teste' , 'teste','teste','teste' )
table.add_row('teste1' , 'teste1' , 'teste1' , 'teste1' , 'teste1' )
console.print(table)