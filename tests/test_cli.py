import pytest
import click

import src.pypassword.cli as cli

from click.testing import CliRunner


runner = CliRunner()

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
    result = runner.invoke(cli.main, aux_cmd)
    
    # If an argument didn't exists an exit code of 2 is raised
    assert result.exit_code == 0, "Missing '%s'" % ' '.join(cmd)

def test_main_command():
    # Test that the password is returned when the mode is 'random' and length is 12
    runner = CliRunner()
    result = runner.invoke(cli.main, ['random'])
    assert result.exit_code == 0
    assert len(result.output) == 12

    # Test that the password is returned when the mode is 'random' and length is specified
    runner = CliRunner()
    result = runner.invoke(cli.main, ['random', '-l', '20'])
    assert result.exit_code == 0
    assert len(result.output) == 20

    # Test that the password is returned when the mode is 'random' and the characters are specified in a file
    runner = CliRunner()
    with runner.isolated_filesystem():
        with open('chars.txt', 'w') as f:
            f.write('abc')
        result = runner.invoke(cli.main, ['random', '-C', 'chars.txt'])
    assert result.exit_code == 0
    assert set(result.output[:-1]) <= {'a','b','c'}

    # Test that the password is returned when the mode is 'random' and the characters are specified as a string
    runner = CliRunner()
    result = runner.invoke(cli.main, ['random', '-c', 'abc'])
    assert result.exit_code == 0
    assert set(result.output[:-1]) <= {'a','b','c'}

    # Test that the help message is returned if the mode is not specified
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    assert 'Command-line tool for generating secure passwords' in result.output

    # Test that the version is returned when the --version option is provided
    runner = CliRunner()
    result = runner.invoke(cli.main, ['--version'])
    assert result.exit_code == 0
    assert 'Pypassword' in result.output
