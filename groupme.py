import requests
import random
import string


class GroupMe:
    def __init__(self, access_token):
        self.base = 'https://api.groupme.com/v3/'
        self.access_token = access_token

    def get_groups_info(self):
        endpoint_url = f"{self.base}groups"
        payload = {
            "token": self.access_token
        }
        r = requests.get(endpoint_url, params=payload)

        groups_info = r.json()

        groups_ids = []
        for group in groups_info["response"]:
            group_info = {
                "name": group['name'],
                "group_id": group['group_id']
            }
            groups_ids.append(group_info)

        for group in sorted(groups_ids, key=lambda _: group["name"]):
            print(f"Group Name: {group['name']}, ID: {group['group_id']}")

        return r

    def get_group_single(self, group_id):
        endpoint_url = f"{self.base}groups/{group_id}"
        payload = {
            "token": self.access_token
        }
        r = requests.get(endpoint_url, params=payload)
        return r

    def get_messages(self, group_id):
        endpoint_url = f"{self.base}groups/{group_id}/messages?{self.access_token}"
        payload = {
            "limit": 25
        }

        r = requests.get(endpoint_url, params=payload)
        return r

    def send_group_message(self, group, message_text):
        endpoint_url = f"{self.base}groups/{group}/messages"

        payload = {
            "token": self.access_token,
        }
        data = {
            "message": {
                "source_guid": self.random_guid(),
                "text": message_text
            }
        }

        p = requests.post(endpoint_url, json=data, params=payload)
        return p

    def images(self, image):
        endpoint_url = "https://image.groupme.com/pictures"

        p = requests.post(endpoint_url, data=image, params=self.access_token)
        return p

    @staticmethod
    def random_guid():
        n = 8
        random_guid = ''.join(random.choices(string.ascii_lowercase + string.digits, k=n))
        return random_guid

