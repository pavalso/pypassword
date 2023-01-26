import logging

import click

from typing import (
    BinaryIO
)


class FileToSet(click.File):
    """Parameter that transforms a file text characters into a set"""
    def __init__(self, *args, **kwargs) -> None:
        super().__init__('rb', *args, **kwargs)

    def convert(self, value, param, ctx):
        fp: BinaryIO = super().convert(value, param, ctx)
        return set(char.to_bytes(2, 'big') for char in fp.read())


class StrToSet(click.ParamType):
    """Parameter that transforms a string into a set of its characters"""
    name = 'string'
    def convert(self, value, param, ctx):
        return set(char.encode('utf-8') for char in super().convert(value, param, ctx))


def setup_logger(
    *,
    handler: logging.Handler = logging.StreamHandler(),
    formatter: logging.Formatter = None,
    level: int = logging.WARNING,
    root: bool = False,
) -> None:
    """
    Function from discord.py package, adapted for this proyect
    https://github.com/Rapptz/discord.py/blob/master/discord/utils.py#L1299

    Setup a python logger.
    This function sets up a logger with the specified handler, formatter, level, and root status. 
    If no formatter is provided, a default formatter will be used with the format. 
    If root is set to True, the logger will be set as the root logger, otherwise the logger will be set to the library name specified in name.

    Parameters:
        handler (logging.Handler, optional): The logging handler to be used. Defaults to logging.StreamHandler().
        formatter (logging.Formatter, optional): The logging formatter to be used. Defaults to None.
        level (int, optional): The logging level to be used. Defaults to logging.WARNING.
        root (bool, optional): Whether to use the root logger or not. Defaults to False.
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
