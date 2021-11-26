from datetime import datetime
from time import sleep

from rich import box
from rich.align import Align
from rich.console import Console, Group
from rich.layout import Layout
from rich.live import Live
from rich.panel import Panel
from rich.progress import BarColumn, Progress, SpinnerColumn, TextColumn
from rich.syntax import Syntax
from rich.table import Table
from rich.text import Text


class Entete:

    """
    Plateau de boss final. 
    C'est une classe qui permet d'ajouter une animation avant d'entrer dans la salle de boss.
    """

    def make_layout() -> Layout:
        """Création de la présentation de structure."""
        layout = Layout(name="root")

        layout.split(
            Layout(name="header", size=3),
            Layout(name="main", ratio=1),
            Layout(name="footer", size=7),
        )
        layout["main"].split_row(
            Layout(name="side"),
            Layout(name="body", ratio=2, minimum_size=60),
        )
        layout["side"].split(Layout(name="box1"), Layout(name="box2"))
        return layout


    def make_message_de_jeu() -> Panel:
        """Les messages"""
        message_de_jeu = Table.grid(padding=1)
        message_de_jeu.add_column(style="green", justify="right")
        message_de_jeu.add_column(no_wrap=True)
        message_de_jeu.add_row(
            "Le combat va commencer.",
            "Préparez-vous.",
        )

        intro_message = Text.from_markup(
            """Vous êtes entré dans la tourelle du donjon ! """
        )

        message = Table.grid(padding=1)
        message.add_column()
        message.add_column(no_wrap=True)
        message.add_row(intro_message, message_de_jeu)

        message_panel = Panel(
            Align.center(
                Group(intro_message, "\n", Align.center(message_de_jeu)),
                vertical="middle",
            ),
            box=box.ROUNDED,
            padding=(1, 2),
            title="[b red]Vous y êtes arrivé !",
            border_style="bright_blue",
        )
        return message_panel

    def __rich__(self) -> Panel:
        grid = Table.grid(expand=True)
        grid.add_column(justify="center", ratio=1)
        grid.add_column(justify="right")
        grid.add_row(
            "[b]Salle de boss[/b] Dragons Unfurled",
            datetime.now().ctime().replace(":", "[blink]:[/]"),
        )
        return Panel(grid, style="white on blue")


    def make_syntax() -> Syntax:
        code = """\
    # Calcul de dégats:
    frappe_armure = rd.randint(1,20) 
    d = type_attaque // 2 - 5  
    jet_critique = int(frappe_armure == 20) 
    pv = randint(1,20*(1+jet_critique)) + d + bonus
        """
        syntax = Syntax(code, "python", line_numbers=True)
        return syntax

    def make_syntax2() -> Panel:
        return "Félicitation !"

    def lance_la_page():
        console = Console()
        job_progress = Progress(
            "{task.description}",
            SpinnerColumn(),
            BarColumn(),
            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
        )
        job_progress.add_task("[green]Ouverture de la salle")
        job_progress.add_task("[magenta]Réveil du boss", total=200)
        job_progress.add_task("[cyan]Apparition de coffres", total=400)

        total = sum(task.total for task in job_progress.tasks)
        overall_progress = Progress()
        overall_task = overall_progress.add_task("Préparation du combat", total=int(total))

        progress_table = Table.grid(expand=True)
        progress_table.add_row(
            Panel(
                overall_progress,
                title="Chargement général",
                border_style="green",
                padding=(2, 2),
            ),
            Panel(job_progress, title="[b]Actions en cours", border_style="red", padding=(1, 2)),
        )

        layout = Entete.make_layout()
        layout["header"].update(Entete())
        layout["body"].update(Entete.make_message_de_jeu())
        layout["box2"].update(Panel(Entete.make_syntax(), border_style="green"))
        layout["box1"].update(Panel(Entete.make_syntax2(), border_style="red"))
        layout["footer"].update(progress_table)

        with Live(layout, refresh_per_second=10, screen=True):
            while not overall_progress.finished:
                sleep(0.1)
                for job in job_progress.tasks:
                    if not job.finished:
                        job_progress.advance(job.id)

                completed = sum(task.completed for task in job_progress.tasks)
                overall_progress.update(overall_task, completed=completed)
