import pytest
import click

import src.pypassword.cli as cli

from click.testing import CliRunner


cli_runner = CliRunner()

@pytest.mark.parametrize(
    'cmd',
    (
        ['--help'],
        ['--version'],
        ['random'],
        ['random', '-l', ''],
        ['random', '-c', ''],
        ['random', '-C', '']
    ),
)
def test_existance(cmd):
    # Add --help at the end in order to avoid executing the command but keep checking if the arguments exists
    aux_cmd = cmd + ['--help']
    out = cli_runner.invoke(cli.main, aux_cmd)
    
    # If an argument didn't exists an exit code of 2 is raised
    assert out.exit_code == 0, "Missing '%s'" % ' '.join(cmd)
