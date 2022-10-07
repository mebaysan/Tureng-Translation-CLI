def extract_synonym_header_text(soup):
    # get header text
    header = soup.find("h1", class_="source-heading")
    header_text = header.string
    return header_text


def extract_synonym_table_headers(soup):
    table_header_text = " \t".join(["#", "Synonym", "Defination"])
    return table_header_text


def extract_synonym_table_rows(soup, word):
    # get table
    table = soup.find_all("div", class_="single-synonym-wrapper")[0]
    rows = table.find_all("div", class_="single-synonym")

    # table rows
    table_rows_texts = []
    for table_row in rows:
        row_id = len(table_rows_texts) + 1
        row_synonym = table_row.find_all("div", class_="synonym-link-wrapper")[0].text
        row_defination = table_row.find_all("span")[0].text
        row_text = "\t+ ".join([str(row_id), row_synonym, row_defination])
        table_rows_texts.append(row_text)

    return table_rows_texts


def check_is_there_synonym_result(soup):
    # get tables to check is there a result table
    result = soup.find_all("div", class_="single-synonym-wrapper")
    return True if len(result) >= 1 else False


def extract_synonym_no_synonym_header_text(soup, word):
    # get header text
    header_text = f"synonym examples for: {word}"
    return header_text


def extract_synonym_no_synonym_possible_words(soup):
    return "No results found!"
