import click
import requests
from bs4 import BeautifulSoup
from tureng_cli.utilities.constants import CRACKER_HEADER
from tureng_cli.utilities.helpers import get_turkish_translate_url
from tureng_cli.utilities.translate.helpers import (
    extract_translate_header_text,
    extract_translate_table_headers,
    extract_translate_table_rows,
    check_is_there_translation_result,
    extract_translate_no_translation_header_text,
    extract_translate_no_translation_possible_words,
)


@click.command()
@click.option(
    "-w", "--word", prompt="Word (Turkish)", help="A word to translate from Turkish."
)
@click.option("-n", "--n-result", prompt="N Rows", help="N rows to show.", default=15)
def translate(word, n_result):
    """Command to translate a Turkish word to English

    Args:
        word (str): Turkish word
        n (int): The range of the list of translated results
    """
    target_url = get_turkish_translate_url(word)
    res = requests.get(target_url, headers=CRACKER_HEADER)
    soup = BeautifulSoup(res.text, "html.parser")

    if check_is_there_translation_result(soup):
        header_text = extract_translate_header_text(soup)
        table_header_text = extract_translate_table_headers(soup)
        table_rows_texts = extract_translate_table_rows(soup)

        # echo outputs
        click.echo(header_text)
        click.echo(table_header_text)
        click.echo("\n".join(table_rows_texts[:n_result]))
    else:
        header_text = extract_translate_no_translation_header_text(soup)
        possible_words_list = extract_translate_no_translation_possible_words(soup)
        click.echo(header_text)
        click.echo(possible_words_list)
