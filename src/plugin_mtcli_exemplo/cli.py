"""
Interface CLI do plugin exemplo.

Comando:

    mt exemplo
"""

import click

from mtcli.domain.timeframe import Timeframe

from .conf import (
    BARS,
    SYMBOL,
    TIMEFRAME,
)


@click.command("exemplo")
@click.version_option(package_name="plugin-mtcli-exemplo")
@click.option(
    "-s",
    "--symbol",
    default=SYMBOL,
    show_default=True,
    type=str,
    help="Ativo.",
)
@click.option(
    "-t",
    "--timeframe",
    default=TIMEFRAME,
    show_default=True,
    type=str,
    help="Timeframe base.",
)
@click.option(
    "-b",
    "--bars",
    default=BARS,
    show_default=True,
    type=click.IntRange(min=1),
    help="Quantidade de candles base.",
)
def exemplo(symbol: str, timeframe: str, bars: int) -> None:
    """
    Exibe o comando exemplo no terminal.

    Exemplos:

        mt exemplo

        mt exemplo --symbol WIN$N

        mt exemplo --symbol WIN$N --timeframe m5 --bars 20
    """
    try:
        Timeframe.from_string(timeframe)
    except ValueError as exc:
        raise click.BadParameter(
            str(exc),
            param_hint="--timeframe",
        ) from exc

    click.echo(f"Ativo: {symbol} Timeframe: {timeframe} Bars: {bars}")
