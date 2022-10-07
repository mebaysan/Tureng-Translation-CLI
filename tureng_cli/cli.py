import click
from tureng_cli.utilities.helpers import bind_commands_to_cli
from tureng_cli.commands.translate import translate
from tureng_cli.commands.sentence import sentence


@click.group()
def cli():
    pass


if __name__ == "__main__":
    bind_commands_to_cli(cli, [sentence])
    cli()
