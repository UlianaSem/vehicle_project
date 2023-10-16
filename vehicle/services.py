import requests
from django.conf import settings
from rest_framework import status


def convert_rub(rub):
    url = f"{settings.EXCHANGE_RATE_URL}?to=USD&from=RUB&amount={rub}"

    payload = {}
    headers = {
        "apikey": settings.EXCHANGE_RATE_API_KEY
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    status_code = response.status_code

    if status_code == status.HTTP_400_BAD_REQUEST:
        return None

    if status_code == status.HTTP_200_OK:
        result = response.json()['result']

        return result
