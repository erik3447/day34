import requests

API_ENDPOINT = "https://opentdb.com/api.php"

PARAMS = {
    "amount": 10,
    "type": "boolean",
}

def get_questions():
    response = requests.get(url=API_ENDPOINT, params=PARAMS)
    response.raise_for_status()
    data = response.json()["results"]
    return data



question_data = get_questions()

