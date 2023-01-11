from bs4 import BeautifulSoup


def get_pokedex_data(html):
    """Uses provided scrapped html data for fetching pokedex data"""
    html = html
    soup = BeautifulSoup(html, "html.parser")
    base_stats_table = soup.find_all('table', attrs={'class': 'vitals-table'})[0]
    table_body = base_stats_table.find('tbody')
    rows = table_body.find_all('tr')

    raw_pokedex_data = []

    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        raw_pokedex_data.append([ele for ele in cols if ele])

    pokedex_data = {'number': raw_pokedex_data[0][0],
                    'type': raw_pokedex_data[1][0],
                    'species': raw_pokedex_data[2][0],
                    'height': raw_pokedex_data[3][0],
                    'weight': raw_pokedex_data[4][0],
                    # 'abilities': raw_pokedex_data[5][0],
                    # 'local': raw_pokedex_data[6][0],
                    }

    return pokedex_data
