import requests

class Sheety():
    def __init__(self, link):
        self.sheet_link = link
        self.header = {
            "Content-Type": "application/json"
        }

    def upload_data(self, full_data: list):
        for data in full_data:
            row_content = {
                'opportunity': data
            }
            response = requests.post(url=self.sheet_link, json=row_content, headers=self.header)