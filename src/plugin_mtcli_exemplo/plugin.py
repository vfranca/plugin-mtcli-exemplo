"""
Registro do plugin plugin-mtcli-exemplo no mtcli principal.
"""

from .cli import exemplo


def register(cli) -> None:
    """
    Registra o comando exemplo no CLI principal do mtcli.

    Args:
        cli: Grupo Click principal do mtcli.
    """
    cli.add_command(exemplo, name="exemplo")
