def extract_sentence_header_text(soup):
    # get header text
    header = soup.find("h1", class_="source-heading")
    header_text = header.string
    return header_text


def extract_sentence_table_headers(soup):
    table_header_text = " \t".join(["#", "Sentence"])
    return table_header_text


def extract_sentence_table_rows(soup, word):
    # get table
    table = soup.find_all("ul", class_="sentences-list")[0]
    rows = table.find_all("li")

    # table rows
    table_rows_texts = []
    for table_row in rows:
        row_id = len(table_rows_texts) + 1
        row_sentence = table_row.find_all("p", class_="sentence-item__text")[0].text
        row_sentence = row_sentence.replace(word, f"**{word}**")
        row_text = "\t+ ".join([str(row_id), row_sentence])
        table_rows_texts.append(row_text)

    return table_rows_texts


def check_is_there_sentence_result(soup):
    # get tables to check is there a result table
    result = soup.find_all("ul", class_="sentences-list")
    return True if len(result) >= 1 else False


def extract_sentence_no_sentence_header_text(soup, word):
    # get header text
    header_text = f"Sentence examples for: {word}"
    return header_text


def extract_sentence_no_sentence_possible_words(soup):
    return "No results found!"
