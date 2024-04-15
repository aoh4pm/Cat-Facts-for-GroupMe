import requests


class Cats:
    def __init__(self, base):
        self.base = base

    def get_random_fact(self):
        endpoint_url = f"{self.base}/fact"
        r = requests.get(endpoint_url)
        fact = r.json()["fact"]
        return fact
