#!/usr/bin/python3

from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

def read_json_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def read_csv_file(filepath):
    products = []
    with open(filepath, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # Convert types as needed
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            products.append(row)
    return products

@app.route('/products')
def products():
    source = request.args.get('source')
    id_param = request.args.get('id')
    products_list = []
    error = None
    product_found = None

    if source not in ['json', 'csv']:
        error = "Wrong source"
    else:
        # Lire le fichier correspondant
        try:
            if source == 'json':
                products_list = read_json_file('products.json')
            elif source == 'csv':
                products_list = read_csv_file('products.csv')
        except Exception as e:
            error = f"Error reading data: {e}"

        # Filtrer par id si demandé
        if not error and id_param:
            try:
                id_int = int(id_param)
                product_found = next((p for p in products_list if p['id'] == id_int), None)
                if not product_found:
                    error = "Product not found"
            except ValueError:
                error = "Invalid id parameter"

    return render_template(
        'product_display.html',
        products=products_list if not product_found else [product_found],
        error=error
    )


if __name__ == '__main__':
    app.run(debug=True, port=5000)