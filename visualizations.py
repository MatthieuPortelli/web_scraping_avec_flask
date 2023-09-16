import matplotlib
import matplotlib.pyplot as plt
import os
# Utilisez la méthode 'Agg' pour la génération d'images sans interface graphique
matplotlib.use('Agg')


def create_word_histogram(most_common):
    """
    Crée un histogramme des mots les plus courants.

    :param most_common: Une liste des mots les plus courants avec leurs fréquences.
    """
    # Séparez les mots et leurs fréquences en listes distinctes
    words, frequencies = zip(*most_common[:5])  # Sélectionnez les 5 premiers mots les plus courants
    # Créez un histogramme
    plt.figure(figsize=(10, 6))
    plt.bar(words, frequencies)
    plt.xlabel('Mots')
    plt.ylabel('Fréquence')
    plt.title('Top 5 mots les plus courants')
    plt.xticks(rotation=45)
    plt.tight_layout()
    # Vérifiez si le dossier 'visualizations' existe, sinon, créez-le
    if not os.path.exists('static/visualizations'):
        os.makedirs('static/visualizations')
    # Enregistrez l'histogramme
    filename = f'static/visualizations/word_histogram.png'
    plt.savefig(filename)
    # Fermez le graphique pour libérer la mémoire
    plt.close()


def create_links_pie_chart(internal_links, external_links):
    """
    Crée un graphique en secteurs pour montrer la proportion de liens internes et externes.

    :param internal_links: Le nombre de liens internes.
    :param external_links: Le nombre de liens externes.
    """
    # Étiquettes pour les secteurs
    labels = ['Liens internes', 'Liens externes']
    # Données à afficher
    sizes = [len(internal_links), len(external_links)]
    # Couleurs des secteurs
    colors = ['#ff9999', '#66b3ff']
    # Explosion du secteur (0.1 signifie que le premier secteur sera légèrement détaché)
    explode = (0.1, 0)
    # Création du graphique en secteurs
    plt.figure(figsize=(8, 8))
    plt.pie(sizes, explode=explode, colors=colors, autopct='%1.1f%%', startangle=90)
    plt.axis('equal')  # Assurez-vous que le graphique est un cercle
    # Ajoutez une légende
    plt.legend(labels, loc="best")
    # Ajoutez un titre
    plt.title('Proportion des liens internes et externes')
    # Vérifiez si le dossier 'visualizations' existe, sinon, créez-le
    if not os.path.exists('static/visualizations'):
        os.makedirs('static/visualizations')
    # Enregistrez le graphique à secteurs
    filename = f'static/visualizations/links_pie_chart.png'
    plt.savefig(filename)
    # Fermez le graphique pour libérer la mémoire
    plt.close()
