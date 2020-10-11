import requests
from bs4 import BeautifulSoup

from common.constantes import *


class Transform:
    """ Extract and parse contents of a page """

    def __init__(self, url, extract_dir):
        self._url = url
        contents = requests.get(self.url).text
        self._soup = BeautifulSoup(contents, "html.parser")
        self._browse()

    def _browse(self):
        pass
        """ Browse main directory, categort directory, files product. Transform each file to give loaded data """

    def _parse(self):
        elements = [None, None, None, None, None, None, None, None, None, None]

        elements[TITLE] = self._soup.find('h1').get_text()

        elements[PRODUCT_PAGE_URL] = self._soup.find_all('p')[3].get_text()

        # In order : universal_product_code, category, price_including_tax, price_excluding_tax, number_available,
        # review_rating
        trs = self._soup.find_all('tr')
        for i, result in enumerate(trs):
            elements[i + 2] = result.td.get_text()

        elements[IMAGE_URL] = self._soup.find('img')['src']
