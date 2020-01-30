from bs4 import BeautifulSoup
import requests

class indexClass:

    def __init__(self, url):
        self.url = url

    def index(self):
        page = requests.get('http://' + self.url)

        soup = BeautifulSoup(page.text, 'html.parser')

        ps = soup.find_all('p')

        for p in ps:
            print(p.get_text())
