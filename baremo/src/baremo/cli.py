"""Punto de entrada de la línea de órdenes: `uv run baremo --help`.

Cada fase añade aquí sus órdenes (ver docs/02-backlog.md). No meter lógica en este fichero:
cada orden solo llama a una función de su paquete.
"""

import typer

from baremo import __version__

app = typer.Typer(help="Baremo: estrategia de oferta para licitaciones públicas.", no_args_is_help=True)


@app.callback()
def principal() -> None:
    """Baremo: estrategia de oferta para licitaciones públicas."""


@app.command()
def version() -> None:
    """Muestra la versión instalada."""
    typer.echo(__version__)


if __name__ == "__main__":
    app()
