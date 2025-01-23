from flask import Flask
import requests
app = Flask(__name__)
@app.route('/<date>', methods=['GET'])
@app.route('/', methods=['GET'])
def index(date=''):
    try:
        r = requests.get(f'https://sidofqa.segob.gob.mx/dof/sidof/indicadores/{date}')
        return r.json()
    except requests.exceptions.ConnectionError:
        return {}
