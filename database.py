import sqlite3


# Fonction pour établir la connexion à la base de données SQLite
def connect_to_database():
    """
    Établit une connexion à la base de données SQLite.

    :return: Un objet de connexion à la base de données SQLite.
    """
    conn = sqlite3.connect('web_scraping.db')
    return conn


# Fonction pour créer les tables nécessaires dans la base de données
def create_tables(conn):
    """
    Crée les tables nécessaires dans la base de données si elles n'existent pas déjà.

    :param conn: L'objet de connexion à la base de données SQLite.
    """
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS html_content (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            session TEXT,
            url TEXT UNIQUE,
            content TEXT,
            title TEXT,
            headings TEXT,
            emphasis TEXT
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS url (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            url TEXT,
            session TEXT,
            status TEXT,
            datestart DATETIME
        )
    ''')
    conn.commit()
