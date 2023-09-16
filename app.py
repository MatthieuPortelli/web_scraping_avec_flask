from flask import Flask, render_template, request
from core import initialize_database_and_scrape_url, scrape_url
from visualizations import create_word_histogram, create_links_pie_chart

app = Flask(__name__)
# Indiquez le dossier des modèles
app.template_folder = 'templates'


@app.route('/')
def accueil():
    """
    Affiche la page d'accueil.

    :return: Modèle HTML de la page d'accueil.
    """
    return render_template('accueil.html')


@app.route('/scrape', methods=['GET', 'POST'])
# Route Flask pour la page d'accueil ("/")
# Gère losque l'utilisateur accède à la page (GET) / lorsqu'il soumet un formulaire (POST)
def scrape():
    """
    Gère la soumission du formulaire de scraping.

    :return: Modèle HTML avec les résultats du scraping ou une page d'erreur.
    """
    # Vérifiez si la méthode de la requête est POST (formulaire soumis)
    if request.method == 'POST':
        url = request.form['url']
        if url:
            try:
                # Appelez la fonction pour obtenir les données
                scraped_data, most_common, internal_links, external_links = initialize_database_and_scrape_url(url)
                if scraped_data and most_common:
                    create_word_histogram(most_common)
                    create_links_pie_chart(internal_links, external_links)
                    # Renvoyez le modèle avec les données et l'onglet actif
                    return render_template('result.html', scraped_data=scraped_data, most_common=most_common, url=url)
                else:
                    error = "Aucune donnée n'a été trouvée pour l'URL saisie."
                    return render_template('error.html', error=error)
            except Exception as e:
                error = f"Une erreur s'est produite lors du scraping de l'url : {e}"
                return render_template('error.html', error=error)
        else:
            error = "Veuillez entrer une URL à scraper."
            return render_template('error.html', error=error)
    else:
        url = request.args.get('url')
        if url:
            scraped_data = scrape_url(url)
            # Renvoyez le modèle avec les données et l'onglet actif
            return render_template('result.html', scraped_data=scraped_data)
        else:
            error = "L'URL à scraper n'a pas été spécifiée."
            return render_template('error.html', error=error)


if __name__ == '__main__':
    app.run(debug=False)
