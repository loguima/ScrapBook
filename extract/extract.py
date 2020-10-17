from urllib import parse

import requests
from bs4 import BeautifulSoup

class Extract:
    """ Extract contents of a page """

    def __init__(self, url, extracted_dir):
        """ Get contents of a web page, prepare format BeautyfullSoup """
        self.url = url
        self.extracted_dir = extracted_dir
        self.soup = self.make_soup(url)
        self.create_dir()
        self.browse()
        self.extract()

    def make_soup(self, url):
        contents = requests.get(url).text
        return BeautifulSoup(contents, "html.parser")

    def create_dir(self):
        pass

    def browse(self):
        pass

    def extract(self):
        pass

    def urlpath(self, fragment):
        return parse.urljoin(self.url, fragment)
