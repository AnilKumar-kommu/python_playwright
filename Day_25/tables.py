import pytest
from playwright.sync_api import Page,expect


def test_verify_tabel(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    table=page.locator("table[name=BookTable] tbody")
    expect(table).to_be_visible()

    #count the number of rows in a table
    rows=table.locator("tr") #equal to this table[name='BookTable'] tbody tr
    expect(rows).to_have_count(7)

    row_count=rows.count()
  #  print("Number of rows is available in the teable: ",row_count)

    #count the total number of columns/header in the table
    columns=rows.locator("th")
    expect(columns).to_have_count(4)
    colunms_con=columns.count()
   # print("Number of columns is available in the table: ",colunms_con)

    # read all the data from the 2nd pf the table

    secound_row_cells=rows.nth(2).locator("td")
    secound_row_texts=secound_row_cells.all_inner_texts()
    expect(secound_row_cells).to_have_text(['Learn Java', 'Mukesh', 'Java', '500'])
   # print("second row of cells is available in the table: ",secound_row_texts)

    # for text in secound_row_texts:
    #     print(text)

    #read all the data from the table (excluding the header)
    #
    # all_row_data=rows.all()
    # for row in all_row_data[1:]:
    #      cols=row.locator("td").all_inner_texts()
    #      print(cols)

    # print book name author is mukesh

    all_row_data = rows.all()
    for row in all_row_data[1:]:
        author_name = row.locator("td").nth(1).inner_text()
        if author_name == "Mukesh":
           book_name=row.locator("td").nth(0).inner_text()
           print(f"\n {author_name} \t {book_name}")





