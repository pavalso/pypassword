import click

from .utils import FileToSet, StrToSet


FILE_TO_SET = FileToSet()
STR_TO_SET = StrToSet()


def print_version(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return

    from . import __version__

    click.echo('Pypassword %s' % __version__)
    ctx.exit()

@click.command()

@click.option(
    '-l',
    '--length',
    default=12,
    help='Length of the password'
    )

@click.argument(
    'mode',
    type=click.Choice(['random'])
)

@click.option(
    '-C',
    '--chars-file',
    'chars_file_set',
    type=FILE_TO_SET,
    help='A file containing all the characters that can be used to generate the password'
    )

@click.option(
    '-c',
    '--chars-list',
    'chars_raw_set',
    type=STR_TO_SET,
    help='A string containing all the characters that can be used to generate the password, ' \
        'if --chars-file exists, this will be completely ignored'
    )

@click.option(
    '-v',
    '--verbose',
    count=True
    )

@click.option(
    '--version',
    is_flag=True,
    callback=print_version,
    expose_value=False,
    is_eager=True
    )

@click.pass_context
def main(
    ctx,
    length: int,
    mode: str,
    chars_file_set: set[bytes],
    chars_raw_set: set[bytes],
    verbose: int
    ):
    """*Proyect description*"""
    ctx.ensure_object(dict)

    ctx.obj['length'] = length
    ctx.obj['verbose'] = verbose
