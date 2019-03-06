import requests


def call_metrolink():
    url = "https://api.tfgm.com/odata/Metrolinks"
    headers = {
        'Ocp-Apim-Subscription-Key': "<>",
        'Authorization': "Bearer <>",
    }
    response = requests.request("GET", url, headers=headers)
    print(response.text)
    return response.text


def main() -> int:
    call_metrolink()


if __name__ == "__main__":
    print(main())
