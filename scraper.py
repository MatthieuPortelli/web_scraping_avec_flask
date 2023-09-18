import requests
from bs4 import BeautifulSoup


def get_html_content(url):
    """
    Récupère le contenu HTML d'une URL en utilisant une requête HTTP GET.

    :param url: L'URL à scraper.
    :return: Un objet BeautifulSoup représentant le contenu HTML ou un message d'erreur si une erreur survient.
    """
    try:
        # Définir un en-tête User-Agent pour simuler un navigateur Web
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
        }
        # Effectuez une requête HTTP GET avec l'en-tête défini
        response = requests.get(url, headers=headers)
        # Vérifiez si la réponse a un code d'état HTTP 2xx (pas d'erreur)
        response.raise_for_status()
    except requests.exceptions.HTTPError as errhttp:
        return f"Erreur HTTP - {errhttp}"
    except requests.exceptions.Timeout as errtimeout:
        return f"Délai de connexion expiré - {errtimeout}"
    except requests.exceptions.ConnectionError as errconnec:
        return f"Erreur de connexion - {errconnec}"
    except requests.exceptions.InvalidURL as errinvalid:
        return f"L'URL fournie est invalide - {errinvalid}"
    except IndexError as errindex:
        return f"Erreur d'index - {errindex}"
    except requests.exceptions.RequestException as e:
        return f"Erreur sur le scraping, URL : {url} - {e}"
    # Si aucune exception n'est levée, la requête a réussi
    # Obtenez le contenu de la réponse HTTP
    content = response.text
    # Utilisez BeautifulSoup pour analyser le contenu HTML
    soup = BeautifulSoup(content, 'html.parser')
    return soup


def scrape_page(soup, url):
    """
    Extrait des données spécifiques d'une page HTML.

    :param soup: Un objet BeautifulSoup représentant le contenu HTML de la page.
    :param url: L'URL de la page scrapée.
    :return: Un dictionnaire contenant les données extraites ou None si une erreur survient.
    """
    # Vérifiez si soup est None (c'est-à-dire si une erreur s'est produite lors de la récupération de la page)
    if soup is None:
        print(f"Erreur lors de la récupération de la page pour l'URL : {url}")
        return None
    try:
        # Titre de la page
        title = soup.find('title').text if soup.find('title') else ''
        # En-têtes (h1, h2, h3, etc.)
        headings = [heading.text for heading in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])]
        # Mots-clés et description
        meta_keywords = soup.find('meta', attrs={'name': 'keywords'})
        keywords = meta_keywords['content'] if meta_keywords else ''
        meta_description = soup.find('meta', attrs={'name': 'description'})
        description = meta_description['content'] if meta_description else ''
        # Texte du contenu principal
        content_text = ' '.join(paragraph.text for paragraph in soup.find_all('p'))
        # Liens internes et externes
        internal_links = [link['href'] for link in soup.find_all('a', href=True) if link['href'].startswith('/')]
        external_links = [link['href'] for link in soup.find_all('a', href=True) if not link['href'].startswith('/')]
        # Images
        images = soup.findAll('img')
        src_list = []  # Une liste pour stocker les sources des images
        for image in images:
            # Utilisez get() pour vérifier si 'src' existe
            src = image.get('src')
            if src:
                src_list.append(src)  # Ajoutez la source à la liste
            else:
                print("Image source non trouvée")
        # Dictionnaire des données
        data = {
            'url': url,
            'title': title,
            'headings': headings,
            'meta_keywords': meta_keywords,
            'keywords': keywords,
            'meta_description': meta_description,
            'description': description,
            'content_text': content_text,
            'internal_links': internal_links,
            'external_links': external_links,
            'images': src_list
        }
        return data
    except Exception as e:
        print(f"Une erreur s'est produite lors du scraping des données : {e}")
        return None
