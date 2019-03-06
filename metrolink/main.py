import json
import requests


def call_metrolink(api_key: str):
    url = "https://api.tfgm.com/odata/Metrolinks"
    headers = {
        'Ocp-Apim-Subscription-Key': "{api_key_value}".format(
            api_key_value=api_key)
    }
    response = requests.request("GET", url, headers=headers)
    print(response.text)
    return response.text


def load_metrolink_api_key() -> dict:
    with open('/secrets/private-key-metrolink.json') as f:
        credentials = json.load(f)
    return credentials


def main() -> int:
    metrolink_key = load_metrolink_api_key()['primary-key']
    call_metrolink(metrolink_key)
    return 0


if __name__ == "__main__":
    print(main())
