import click
import requests
from bs4 import BeautifulSoup
from tureng_cli.utilities.constants import CRACKER_HEADER
from tureng_cli.utilities.helpers import get_english_sentence_url
from tureng_cli.utilities.sentence.helpers import (
    extract_sentence_header_text,
    extract_sentence_table_headers,
    extract_sentence_table_rows,
    check_is_there_sentence_result,
    extract_sentence_no_sentence_header_text,
    extract_sentence_no_sentence_possible_words,
)


@click.command()
@click.option(
    "-w",
    "--word",
    prompt="Word (English)",
    help="A word to show the sentences that are created by using the word.",
)
@click.option("-n", "--n-result", prompt="N Rows", help="N rows to show.", default=15)
def sentence(word, n_result):
    """Command to show the sentences

    Args:
        word (str): English word
        n (int): The range of the list of sentenced results
    """
    target_url = get_english_sentence_url(word)
    res = requests.get(target_url, headers=CRACKER_HEADER)
    soup = BeautifulSoup(res.text, "html.parser")
    if check_is_there_sentence_result(soup):
        header_text = extract_sentence_header_text(soup)
        table_header_text = extract_sentence_table_headers(soup)
        table_rows_texts = extract_sentence_table_rows(soup, word)

        # echo outputs
        click.echo(header_text)
        click.echo(table_header_text)
        click.echo("\n".join(table_rows_texts[:n_result]))
    else:
        
        header_text = extract_sentence_no_sentence_header_text(soup, word)
        possible_words_list = extract_sentence_no_sentence_possible_words(soup)
        click.echo(header_text)
        click.echo(possible_words_list)
