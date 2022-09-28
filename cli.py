import click
from utilities.helpers import bind_commands_to_cli
from commans.translate import translate


@click.group()
def cli():
    pass


if __name__ == "__main__":
    bind_commands_to_cli(cli, [translate])
    cli()
