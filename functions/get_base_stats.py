from bs4 import BeautifulSoup


def get_base_stats(html):
    """Uses provided scrapped html data for fetching pokedex data"""
    html = html
    soup = BeautifulSoup(html, "html.parser")
    base_stats_table = soup.find_all('table', attrs={'class': 'vitals-table'})[3]
    table_body = base_stats_table.find('tbody')
    rows = table_body.find_all('tr')

    raw_base_stats = []

    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        raw_base_stats.append([ele for ele in cols if ele])

    base_stats = {'hp': raw_base_stats[0][0],
                  'attack': raw_base_stats[1][0],
                  'defense': raw_base_stats[2][0],
                  'sp_attack': raw_base_stats[3][0],
                  'sp_defense': raw_base_stats[4][0],
                  'speed': raw_base_stats[5][0],
                  }

    return base_stats
