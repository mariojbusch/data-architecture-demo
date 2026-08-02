import requests
import json
import os
from datetime import datetime

def run_ingestion():
    print("Starting ingestion...")

    # Exemplo de API pública (troque pela sua)
    url = "https://jsonplaceholder.typicode.com/posts"

    response = requests.get(url, timeout=30)

    if response.status_code != 200:
        raise Exception(f"API returned status {response.status_code}")

    data = response.json()

    print(f"Fetched {len(data)} records from API")

    # Salvar localmente dentro do container (depois enviamos ao GCS)
    timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    output_path = f"/tmp/api_data_{timestamp}.json"

    with open(output_path, "w") as f:
        json.dump(data, f)

    print(f"Data saved temporarily at {output_path}")

    return output_path
