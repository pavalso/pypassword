import logging


def setup_logger(
    *,
    handler: logging.Handler = logging.StreamHandler(),
    formatter: logging.Formatter = None,
    level: int = logging.WARNING,
    root: bool = False,
) -> None:
    """Function from discord.py package, adapted for this proyect
        https://github.com/Rapptz/discord.py/blob/master/discord/utils.py#L1299

        Initializes the logger, :root: specifies whenever root logger should be configured
        or the library at `__name__`

        If no arguments are passed, the stderr will be used
        and only warnings or above will be shown
    """
    if not formatter:
        dt_fmt = '%Y-%m-%d %H:%M:%S'
        formatter = logging.Formatter('[{asctime}] [{levelname:<8}] {name}: {msg}', dt_fmt, '{')

    if root:
        logger = logging.getLogger()
    else:
        library, _, _ = __name__.partition('.')
        logger = logging.getLogger(library)

    handler.setFormatter(formatter)
    logger.setLevel(level)
    logger.addHandler(handler)
