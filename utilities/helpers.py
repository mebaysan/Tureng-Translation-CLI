from .constants import BASE_URL_TR


def bind_commands_to_cli(cli, *args, **kwargs):
    for func in args:
        cli.add_command(*func)


def get_turkish_translate_url(word):
    return BASE_URL_TR + word
