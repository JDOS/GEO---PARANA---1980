import requests
import time
import os

base_url = "http://www.geo.pr.gov.br/itcg-images/fotos1980/60000/"
start = 55200
end = 57000 

# Cria a pasta de destino, se não existir
os.makedirs("fotos_baixadas", exist_ok=True)

for i in range(start, end + 1):
    url = f"{base_url}{i}.jpg"
    response = requests.get(url)
    if response.status_code == 200:
        filename = f"fotos_baixadas/{i}.jpg"
        with open(filename, "wb") as f:
            f.write(response.content)
        print(f"Arquivo encontrado e baixado: {filename}")
    else:
        print(f"Não existe: {url}")

#Cuidado! Diminuir pode ter bloqueio do server
    time.sleep(1)  # espere 1 segundo entre as tentativas