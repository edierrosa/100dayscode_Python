import requests
import dotenv
from pathlib import Path
import os


# Environment variables
dotenv_path = Path(
    "path to .env")
dotenv.load_dotenv(dotenv_path=dotenv_path)


# Pixela variables
pixela_endpoint = os.environ["PIXELA_GRAPHS_ENDPOINT"]

pixela_headers = {
    "X-USER-TOKEN": os.environ["PIXELA_USER_TOKEN"],
}

pixela_graph_config = {
    "id": "graph1",
    "name": "Running Graph",
    "unit": "Km",
    "type": "float",
    "color": "sora",
}

new_graph_request = requests.post(
    url=pixela_endpoint, json=pixela_graph_config, headers=pixela_headers)
print(new_graph_request.json, new_graph_request.text)
