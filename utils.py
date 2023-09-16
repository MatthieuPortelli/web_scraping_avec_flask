from collections import Counter


def top_n_words(scraped_data, n=5):
    """
    Trouve le mot le plus courant parmi tous les champs de texte de scraped_data.

    :param n: Nombre de mots les plus courants à retourner.
    :param scraped_data: Dictionnaire contenant les données scrapées.
    :return: Le mot le plus courant.
    """
    # Créer un dictionnaire pour compter la fréquence de chaque mot
    word_count = {}
    # Liste de mots à ne pas prendre en compte
    stop_words = [
        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19',
        '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37',
        '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55',
        '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73',
        '74', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '90', '91',
        '92', '93', '94', '95', '96', '97', '98', '99', '100',
        "à", "au", "aux", "avec", "ça", "ce", "ces", "dans", "de", "des", "du", "elle", "en", "et", "eux", "il", "je",
        "la", "le", "leur", "lui", "ma", "mais", "me", "même", "mes", "moi", "mon", "ne", "nos", "notre", "nous", "on",
        "ou", "par", "pas", "pour", "qu", "que", "qui", "sa", "se", "ses", "son", "sur", "ta", "te", "tes", "toi",
        "ton", "tu", "un", "une", "vos", "votre", "vous", "cette", "ci", "déjà", "dont", "elle-même", "elles",
        "elles-mêmes", "en", "encore", "est", "et", "été", "être", "eux", "eux-mêmes", "là", "le", "les", "leur",
        "leurs", "lui-même", "nous", "nous-mêmes", "on", "ont", "ou", "par", "pas", "peu", "plupart", "pour",
        "pourquoi", "qu", "quand", "que", "quel", "quelle", "quelles", "quels", "qui", "sa", "sans", "ses", "seulement",
        "si", "sien", "soi", "soi-même", "sont", "sous", "soyez", "sujet", "sur", "ta", "tandis", "tellement", "tels",
        "tes", "ton", "tous", "tout", "trop", "très", "tu", "voient", "vont", "votre", "vous", "vu", "y",
        ",", ".", "!", "?", "'", '"', ";", ":", "(", ")", "[", "]", "{", "}", "<", ">", "&", "$", "#", "@", "%", "^",
        "*", "+", "-", "=", "_", "~", "`", "|", "\\", "/", "©", "•", "(...)", "[…]", "«", "»", "–",
        "www", "com", "org", "net", "gov", "edu", "html", "http", "https", "a", "an", "the", "and", "in", "on", "at",
        "to", "for", "with", "by", "is", "are", "was", "were", "be", "am", "been", "has", "have", "had", "do", "does",
        "did", "but", "not", "of", "from", "or", "as", "if", "it", "this", "that", "which", "you", "I", "he", "she",
        "we", "they", "our", "your", "my", "his", "her", "its", "their", "me", "him", "us", "them", "mine", "yours",
        "hers", "its", "ours", "theirs", "who", "whom", "whose", "what", "when", "where", "why", "how", "all", "any",
        "both", "each", "either", "neither", "every", "no", "none", "some", "such", "only", "just"
    ]
    # Parcourir les champs de texte de scraped_data
    for field, text in scraped_data.items():
        if isinstance(text, str):  # Assurez-vous que le texte est une chaîne de caractères
            # Convertir le texte en une liste de mots en divisant par des espaces
            words = text.split()
            # Compter la fréquence de chaque mot
            for word in words:
                # Ignorer les mots de la liste des "stop words"
                if word.lower() not in stop_words:
                    if word in word_count:
                        word_count[word] += 1
                    else:
                        word_count[word] = 1
    # Trouver les n mots les plus courants
    most_common = Counter(word_count).most_common(n)
    return most_common
