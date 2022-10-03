import os
from unicodedata import name
from flask import Flask, render_template, json, request, jsonify

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('jogador.html')

@app.route('/jogador')
def renderjogador():
    return render_template('jogador.html')

@app.route('/api/jogador', methods=['POST'])
def jogador():

    json = request.get_json()
    name = json['name'].upper()
    team = json['team'].upper()
    combo = json['combo'].upper()
    return jsonify(name=name,team = team, combo = combo)



if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)