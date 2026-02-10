from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# rota da página inicial

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/buscar', methods =['POST'])    
def buscar_receitas():
    ingrediente = request.form.get('ingrediente')

    url = f'https://www.themealdb.com/api/json/v1/1/filter.php?i={ingrediente}'
    response = requests.get(url)
    return response.json()





if __name__ == "__main__":
    app.run(debug = True)