from database import connect_to_database, create_tables
from scraper import get_html_content, scrape_page
from utils import top_n_words


def initialize_database_and_scrape_url(url):
    """
    Initialise la base de données SQLite, effectue le scraping d'une URL et récupère les données.

    :param url: L'URL à scraper.
    :return: Un dictionnaire contenant les données scrapées, les mots les plus courants, les liens internes et externes.
             En cas d'erreur, un dictionnaire avec la clé 'error' est renvoyé.
    """
    # Connexion à SQLite
    conn = connect_to_database()
    # Création de ma table
    create_tables(conn)
    # Appel à la fonction de scraping
    scraped_data = scrape_url(url)
    if isinstance(scraped_data, str):
        # Gestion d'une erreur renvoyée par scrape_url
        return f"{scraped_data}"
    if scraped_data is None:
        return {'error': 'Une erreur s\'est produite lors du scraping de l\'URL.'}
    # Trouver les n mots les plus courants dans la page scrapée
    most_common = top_n_words(scraped_data)
    # Récupérer les internal_links et external_links
    internal_links = scraped_data.get('internal_links', [])
    external_links = scraped_data.get('external_links', [])
    return scraped_data, most_common, internal_links, external_links


def scrape_url(url):
    """
    Effectue le scraping d'une URL et renvoie les données scrapées.

    :param url: L'URL à scraper.
    :return: Un dictionnaire contenant les données scrapées. En cas d'erreur, None est renvoyé.
    """
    result = get_html_content(url)
    # Vérifiez si le résultat est une chaîne de caractères (message d'erreur)
    if isinstance(result, str):
        # Gestion d'une erreur renvoyée par get_html_content
        return f"{result}"
    try:
        soup = result
        if soup is None:
            return None  # Gestion d'erreur pour la récupération du contenu HTML
    except Exception as e:
        print(f"Une erreur s'est produite lors de la récupération du contenu HTML : {e}")
        return None
    try:
        scraped_data = scrape_page(soup, url)
        if scraped_data is None:
            return None  # Gestion d'erreur pour le scraping des données
    except Exception as e:
        print(f"Une erreur s'est produite lors du scraping des données : {e}")
        return None
    return scraped_data
