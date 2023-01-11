from bs4 import BeautifulSoup

def get_base_stats(database_scrap):
    """Uses provided scrapped html data for fetching base stats"""
    database_scrap = database_scrap
    soup = BeautifulSoup(database_scrap, "html.parser")

    base_stats = []

    base_stats_table = soup.find_all('table', attrs={'class': 'vitals-table'})[3]
    base_stats_table = soup.find_all('table', attrs={'class': 'vitals-table'})[3]
    table_body = base_stats_table.find('tbody')

    rows = table_body.find_all('tr')

    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        base_stats.append([ele for ele in cols if ele])


    # Reference for base stats list index
    """
    hp = base_stats[0][0]
    attack = base_stats[1][0]
    defense = base_stats[2][0]
    sp_attack = base_stats[3][0]
    sp_defense = base_stats[4][0]
    speed = base_stats[5][0]
    """

    return base_stats