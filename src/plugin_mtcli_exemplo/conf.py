"""
Configurações do plugin plugin-mtcli-exemplo.

As configurações são carregadas do arquivo mtcli.ini,
através do sistema de configuração do mtcli.

Seção utilizada:

    [exemplo]

Exemplo de configuração:

    [exemplo]
    symbol = WIN$N
    digitos = 0
    timeframe = m1
    bars = 50
"""

from mtcli.conf import conf

# ==========================================================
# SEÇÃO DE CONFIGURAÇÃO
# ==========================================================

cfg = conf.section("exemplo")


# ==========================================================
# FUNÇÕES AUXILIARES
# ==========================================================


def _get_int(key: str, default: int, minimum: int) -> int:
    """
    Obtém uma configuração inteira com validação.

    Args:
        key: Nome da configuração.
        default: Valor padrão.
        minimum: Valor mínimo permitido.

    Returns:
        Valor inteiro válido ou valor padrão.
    """
    try:
        value = cfg.get(key, cast=int, default=default)
    except (TypeError, ValueError):
        return default

    if value < minimum:
        return default

    return value


# ==========================================================
# SÍMBOLO
# ==========================================================

SYMBOL = str(cfg.get("symbol", default="WIN$N") or "WIN$N").strip()


# ==========================================================
# FORMATAÇÃO DE PREÇO
# ==========================================================

DIGITOS = _get_int("digitos", default=0, minimum=0)


# ==========================================================
# TIMEFRAME
# ==========================================================

TIMEFRAME = str(cfg.get("timeframe", default="m1") or "m1").strip().lower()


# ==========================================================
# QUANTIDADE DE CANDLES
# ==========================================================

BARS = _get_int("bars", default=50, minimum=1)
