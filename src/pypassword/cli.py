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

@click.option(
    '-C', 
    '--chars-file', 
    'chars_file', 
    type=FILE_TO_SET, 
    help='A file containing all the characters that can be used to generate the password'
    )

@click.option(
    '-c', 
    '--chars-list', 
    'chars_list', 
    type=STR_TO_SET, 
    help='A string containing all the characters that can be used to generate the password'
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
def main(ctx, length, chars_file, chars_list, verbose):
    """*Main docstring missing*"""
    click.echo('%s %s %s %s' % (length, chars_file, chars_list, verbose))
