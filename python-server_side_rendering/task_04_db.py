# On importe les bibliotheques
from flask import Flask, render_template, request     # Flask pour le serveur web, render_template pour afficher un template HTML, request pour récupérer les paramètres d'URL
import json                                           # Pour lire les fichiers JSON
import csv                                            # Pour lire les fichiers CSV
import sqlite3                                        # Pour se connecter à une base de données SQLite

# On initialise l'application
app = Flask(__name__)

# initialise le chemin pour aller au produit
@app.route('/products')
def products():
    # Récupération des paramètres d'URL
    source = request.args.get("source")
    product_id = request.args.get("id")

    data = []  # Liste vide qui contiendra les produits chargés

    # Si la source est un fichier JSON
    if source == "json":
        with open("products.json", "r") as f:
            data = json.load(f)  # Chargement des données JSON

    # Si la source est un fichier CSV
    elif source == "csv":
    try:
        # Ouverture du fichier CSV en mode lecture avec encodage UTF-8
        with open("products.csv", "r", encoding="utf-8") as f:
            # On utilise DictReader pour lire chaque ligne sous forme de dictionnaire
            reader = csv.DictReader(f)
            data = []  # Liste vide pour stocker les produits valides

            # Parcours de chaque ligne (produit) du fichier CSV
            for row in reader:
                # Vérifie que toutes les colonnes nécessaires sont présentes
                if "id" in row and "name" in row and "category" in row and "price" in row:
                    # Ajoute le produit à la liste après avoir retiré les espaces inutiles
                    data.append({
                        "id": row["id"].strip(),
                        "name": row["name"].strip(),
                        "category": row["category"].strip(),
                        "price": row["price"].strip()
                    })
    except FileNotFoundError:
        # Si le fichier CSV n'est pas trouvé, on affiche une erreur dans le template
        return render_template("product_display.html", error="CSV file not found")
    except Exception as e:
        # En cas d'erreur générale lors de la lecture du fichier, on affiche un message d'erreur
        return render_template("product_display.html", error=f"CSV error: {str(e)}")

    # Si la source est une base de données SQLite
    elif source == 'sql':
        products = from_sql()  # Appel de la fonction personnalisée pour récupérer les données SQL
        if products is None:
            # S'il y a une erreur SQL, on affiche une erreur dans le template
            return render_template('product_display.html', error="Database error", products=[])
        else:
            data = products  # On récupère les données SQL dans data

    # Si la source n’est pas reconnue
    else:
        return render_template("product_display.html", error="Wrong source")

    # Si un identifiant est fourni, on filtre la liste des produits pour ne garder que celui qui correspond
    if product_id:
        data = [item for item in data if str(item.get("id")) == product_id or str(item.get("id")) == str(product_id)]
        if not data:
            return render_template("product_display.html", error="Product not found")  # Si aucun produit trouvé avec cet ID

    # Affichage des produits (ou du produit filtré) dans le template HTML
    return render_template("product_display.html", products=data)

# Fonction auxiliaire pour lire les produits depuis une base SQLite
def from_sql():
    try:
        # Connexion à la base de données SQLite
        connexion = sqlite3.connect('products.db')
        cursor = connexion.cursor()

        # Requête SQL pour récupérer les colonnes nécessaires
        cursor.execute('SELECT id, name, category, price FROM Products')
        rows = cursor.fetchall()  # Récupération des résultats

        connexion.close()  # Fermeture de la connexion

        # Transformation des lignes SQL en liste de dictionnaires
        products = []
        for row in rows:
            products.append({'id': row[0], 'name': row[1], 'category': row[2], 'price': row[3]})
        return products

    except Exception as e:
        # En cas d'erreur, on affiche l'erreur dans la console et on retourne None
        print(f"Database error: {e}")
        return None

# Point d'entrée de l'application Flask
if __name__ == "__main__":
    app.run(debug=True, port=5000)  # Lancement du serveur en mode debug sur le port 5000
