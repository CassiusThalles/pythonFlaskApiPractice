from flask import Flask
import requests, json

app = Flask(__name__)

@app.route('/pokemon/<name>', methods=['GET'])
def helloworld(name):
    url = 'https://pokeapi.co/api/v2/pokemon/{}'
    response = requests.get(url.format(name))
    response = json.loads(response.content)
    response = [item['ability']['name'] for item in response['abilities']]
    return json.dumps(response)

if __name__ == '__main__':
    app.run(port=8080, debug=True)