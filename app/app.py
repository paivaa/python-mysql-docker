from typing import List, Dict
from flask import Flask
import mysql.connector
import json

app = Flask(__name__)


def cor_favorita() -> List[Dict]:
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'pessoas'
    }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM cor_favorita')
    results = [{nome: cor} for (nome, cor) in cursor]
    cursor.close()
    connection.close()

    return results


@app.route('/')
def index() -> str:
    return json.dumps({'cor_favorita': cor_favorita()})


if __name__ == '__main__':
     app.run(debug=True, port=5000, host="0.0.0.0")