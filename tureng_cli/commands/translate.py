import click
import requests
from bs4 import BeautifulSoup
from tureng_cli.utilities.constants import CRACKER_HEADER
from tureng_cli.utilities.helpers import get_turkish_translate_url

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

    # get header text
    header = soup.find("h2")
    header_text = "".join([i for i in header.strings])

    # get table
    table = soup.find_all("table")[0]
    rows = table.find_all("tr")

    # separate rows
    table_header = rows[0]
    table_rows = rows[1:]

    # table header
    table_headers = table_header.find_all("th")
    table_id = "#"
    table_category = table_headers[1].string
    table_turkish = table_headers[2].string
    table_english = table_headers[3].string
    table_header_text = " \t".join(
        [table_id, table_category, table_turkish, table_english]
    )

    # table rows
    table_rows_texts = []
    for table_row in table_rows:
        row_columns = table_row.find_all("td")
        if len(row_columns) >= 4:
            row_id = row_columns[0].string
            row_category = row_columns[1].string
            row_turkish = row_columns[2].find_all("a")[0].string
            row_english = row_columns[3].find_all("a")[0].string
            row_text = "\t+ ".join([row_id, row_category, row_turkish, row_english])
            table_rows_texts.append(row_text)

    # echo outputs
    click.echo(header_text)
    click.echo(table_header_text)
    click.echo("\n".join(table_rows_texts[:n_result]))
