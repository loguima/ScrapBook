import requests
from bs4 import BeautifulSoup


class Extract:
    """ Extract contents of a page """

    def __init__(self, url, extract_dir):
        """ Get contents of a web page, prepare format BeautyfullSoup"""

        self._soup = self._make_soup(url)
        self._url = url
        self._extract_dir = extract_dir
        self._extract()

    def _make_soup(self, url):
        contents = requests.get(url).text
        return BeautifulSoup(contents, "html.parser")

    def _extract(self):
        pass
