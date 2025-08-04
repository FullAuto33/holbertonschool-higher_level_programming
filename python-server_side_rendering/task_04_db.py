# On importe les bibliotheques
from flask import Flask, render_template, request     # Flask pour le serveur, render_template pour afficher du HTML, request pour récupérer les paramètres d'URL
import sqlite3                                        # Pour accéder à la base de données SQLite
import json                                           # Pour lire les fichiers JSON
import csv                                            # Pour lire les fichiers CSV
import os                                             # Pour vérifier l'existence de fichiers

# On initialise l'app
app = Flask(__name__)

# Chemin pour la page d'accueil
@app.route('/')
def home():
    return render_template('index.html')

# Chemin pour la page À propos
@app.route('/about')
def about():
    return render_template('about.html')

# Chemin pour la page de contact
@app.route('/contact')
def contact():
    return render_template('contact.html')

# Chemin pour afficher les items à partir d’un fichier JSON
@app.route('/items')
def items():
    try:
        # Ouverture du fichier items.json
        with open('items.json') as f:
            data = json.load(f)  # Chargement du contenu JSON
        items = data.get('items', [])  # Récupération de la clé items
        return render_template('items.html', items=items)
    except FileNotFoundError:
        return "Items file not found", 404  # Erreur si fichier introuvable
    except json.JSONDecodeError:
        return "Error decoding JSON", 500  # Erreur si le JSON est mal formé

# Fonction utilitaire pour lire un fichier JSON
def read_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

# Fonction utilitaire pour lire un fichier CSV
def read_csv(file_path):
    products = []  # Liste de produits
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)  # Lecture ligne par ligne sous forme de dictionnaire
        for row in reader:
            row['id'] = int(row['id'])              # Conversion de l'ID en entier
            row['price'] = float(row['price'])      # Conversion du prix en float
            products.append(row)
    return products

# Fonction pour récupérer les données depuis la base SQLite
def fetch_data_from_sqlite():
    conn = sqlite3.connect('products.db')           # Connexion à la base SQLite
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Products')        # Requête SQL pour tous les produits
    rows = cursor.fetchall()                        # Récupération des résultats
    conn.close()                                    # Fermeture de la connexion

    products = []
    for row in rows:
        product = {
            'id': row[0],
            'name': row[1],
            'category': row[2],
            'price': row[3]
        }
        products.append(product)

    print(products)  # Affichage en console (debug)
    return products

# Route principale pour afficher les produits depuis JSON, CSV ou SQL
@app.route('/products')
def products():
    source = request.args.get('source')       # Récupération de la source depuis l'URL 
    product_id = request.args.get('id')       # Récupération de l'ID si précisé

    file_path = ''  # Chemin du fichier

    # Détermination du fichier en fonction de la source
    if source == 'json':
        file_path = 'products.json'
    elif source == 'csv':
        file_path = 'products.csv'
    elif source == 'sql':
        products = fetch_data_from_sqlite()  # Récupération depuis SQL
    else:
        return render_template('product_display.html', error="Wrong source")  # Source invalide

    # Vérifie si le fichier JSON ou CSV existe (si ce n'est pas une source SQL)
    if source != 'sql' and not os.path.exists(file_path):
        return render_template('product_display.html', error="File not found")

    # Lecture du contenu en fonction du format
    if source == 'json':
        products = read_json(file_path)
    elif source == 'csv':
        products = read_csv(file_path)

    # Filtrage par ID si fourni
    if product_id:
        try:
            product_id = int(product_id)  # Conversion en entier
            products = [p for p in products if p['id'] == product_id]  # Filtrage
            if not products:
                return render_template('product_display.html', error="Product not found")  # Si aucun produit ne correspond
        except ValueError:
            return render_template('product_display.html', error="Invalid id")  # Si l'ID n'est pas un entier

    # Affichage de la page avec les produits
    return render_template('product_display.html', products=products)

# Lancement de l'application Flask
if __name__ == '__main__':
    app.run(debug=True, port=5000)
