import requests

def pokedex_scrap(pokemon_name):
    """Gets pokemondb.net html data for future parsing"""
    url = "https://pokemondb.net/pokedex/" + pokemon_name
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36'}
    pokedex_scrap = requests.get(url, headers=headers)
    return(pokedex_scrap.content)