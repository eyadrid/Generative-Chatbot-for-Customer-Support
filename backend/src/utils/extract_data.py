import requests
from bs4 import BeautifulSoup

class DataExtractor:
    def __init__(self, url):
        self.url = url

    def fetch_data(self):
        response = requests.get(self.url)
        response.raise_for_status()  
        return response.content

    def parse_data(self):
        content = self.fetch_data()
        soup = BeautifulSoup(content, 'html.parser')
        return soup
