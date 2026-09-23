"""Línea de órdenes: `uv run cartera-clara --help`.

Cada fase añade aquí sus órdenes (docs/02-backlog.md). Sin lógica en este fichero:
cada orden solo llama a una función de su paquete.
"""

import typer

from cartera_clara import __version__

app = typer.Typer(help="Cartera Clara: tu Renta de inversor, clara.", no_args_is_help=True)


@app.callback()
def principal() -> None:
    """Cartera Clara: tu Renta de inversor, clara."""


@app.command()
def version() -> None:
    """Muestra la versión instalada."""
    typer.echo(__version__)


if __name__ == "__main__":
    app()
