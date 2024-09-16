import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
      response = requests.get(self.url)
      return response.content

    def load_json(self):
        # Get the raw response body and convert it directly to JSON
        json_data = requests.get(self.url).json()
        return json_data  # This will be a Python dictionary or list
