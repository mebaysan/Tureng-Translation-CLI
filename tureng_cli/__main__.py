import click
from tureng_cli.commands.translate import translate
from tureng_cli.commands.sentence import sentence


@click.group()
def cli():
    pass


cli.add_command(translate)
cli.add_command(sentence)
cli()
