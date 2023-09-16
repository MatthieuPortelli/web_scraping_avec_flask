# Web Scraping avec Flask

Il s'agit d'un projet de web scraping utilisant Flask, Beautiful Soup et Python pour extraire des données de pages web.

## Prérequis

Avant de commencer, assurez-vous d'avoir respecté les exigences suivantes :

- Python 3.x installé sur votre machine.
- Flask installé (`pip install Flask`).
- Beautiful Soup (`pip install beautifulsoup4`).
- Requests (`pip install requests`).

## Démarrage

Clonez ce dépôt sur votre machine locale :
```bash
git clone https://github.com/votre-nom/web_scraping_avec_flask.git
cd web_scraping_avec_flask
pip install -r requirements.txt
python app.py
```

## Utilisation

Rendez-vous sur la page d'accueil à l'adresse http://127.0.0.1:5000/.  
Entrez l'URL que vous souhaitez scraper et cliquez sur le bouton "Scrape".  
Les données extraites seront affichées sur la page des résultats.  
Vous pouvez également scraper des liens externes spécifiques en cliquant dessus.  

## Structure du Projet

static/ : Dossier pour les fichiers statiques tels que le CSS et le JavaScript, mais aussi les visualizations.  
templates/ : Dossier contenant les modèles HTML de l'application.  
app.py : Contient l'application Flask et la logique de routage.  
core.py : Contient les fonctions pour initialiser la BDD et le web scraping.  
database.py : Fonctions pour se connecter à SQLite et créer une table.  
scraper.py : Fonctions pour récupérer le contenu HTML et faire le scraping avec BeautifulSoup.  
utils.py : Fonction pour trouver les n premiers mots (contient la liste des mots non pris en compte).  
visualizations.py : Fonctions pour générer des visualisations des données extraites.  
requirements.txt : Liste des packages Python requis pour le projet.  

## Personnalisation

Vous pouvez personnaliser ce projet en ajoutant plus de logique de scraping, en améliorant l'interface utilisateur ou en enrichissant les visualisations des données.

## Remerciements

Merci aux communautés Flask, Beautiful Soup et Python pour avoir créé d'incroyables outils.