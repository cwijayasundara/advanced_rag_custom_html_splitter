from unstructured.partition.html import partition_html
from langchain_core.documents import Document

""" write a function to extract table rows from an html file"""


def extract_table_rows(filename_content):
    html_elements = partition_html(text=filename_content)

    tables = [el for el in html_elements if el.category == "Table"]

    table_rows = []

    for table in tables:
        table_html = table.metadata.text_as_html
        rows = table_html.split('<tr>')
        for row in rows:
            if not row or row.startswith('<table>'):
                continue
            table_rows.append(Document(page_content=row))

    return table_rows


""" write a function to extract other elements than tables from an html file"""


def extract_other_elements(filename_content):
    html_elements = partition_html(text=filename_content)

    other_elements = [el for el in html_elements if el.category != "Table"]

    other_elements_rows = []

    for element in other_elements:
        other_elements_rows.append(Document(page_content=element.text))

    return other_elements_rows
