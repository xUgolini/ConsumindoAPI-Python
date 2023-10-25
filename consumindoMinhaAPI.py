import json
import requests

# GET /hoteis
URL = 'http://127.0.0.1:5000'
body_request = {

}
headers = {'Content-Type': 'application/json'}

resposta_hoteis = requests.get(URL + '/hoteis', json=body_request, headers=headers)

# Verifica se a resposta contém dados JSON válidos
if resposta_hoteis.status_code == 200:
    try:
        hoteis = resposta_hoteis.json()
        print(hoteis['hoteis'])
    except json.JSONDecodeError:
        print("A resposta não contém dados JSON válidos.")
else:
    print("Erro:", resposta_hoteis.status_code)

