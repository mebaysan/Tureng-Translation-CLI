def extract_translate_header_text(soup):
    # get header text
    header = soup.find("h2")
    header_text = "".join([i for i in header.strings])
    return header_text


def extract_translate_table_headers(soup):
    # get table
    table = soup.find_all("table")[0]
    rows = table.find_all("tr")

    # handle header row
    table_header = rows[0]

    # table header
    table_headers = table_header.find_all("th")
    table_id = "#"
    table_category = table_headers[1].string
    table_turkish = table_headers[2].string
    table_english = table_headers[3].string
    table_header_text = " \t".join(
        [table_id, table_category, table_turkish, table_english]
    )
    return table_header_text


def extract_translate_table_rows(soup):
    # get table
    table = soup.find_all("table")[0]
    rows = table.find_all("tr")

    # handle result rows
    table_rows = rows[1:]

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

    return table_rows_texts


def check_is_there_translation_result(soup):
    # get tables to check is there a result table
    result = soup.find_all("table", class_="searchResultsTable")
    return True if len(result) >= 1 else False


def extract_translate_no_translation_header_text(soup):
    # get header text
    header = soup.find("h1")
    header_text = "".join([i for i in header.strings])
    return header_text


def extract_translate_no_translation_possible_words(soup):
    # get possible list
    possible_list = soup.find("ul", {"class": "suggestion-list"})
    possible_words = possible_list.find_all('a')
    possible_words_list = "\n".join([word.string for word in possible_words])
    return possible_words_list
