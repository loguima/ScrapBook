import json
import re
from os import listdir
from urllib.parse import urljoin

from bs4 import BeautifulSoup

from common.constantes import *
from common.directory import Directory


class Transform:
    """ Transform contents of a product's page """

    def __init__(self, extracted_dir, transformed_dir):
        self.extracted_dir = Directory("working_dir", extracted_dir, init=False)
        self.transformed_dir = Directory("working_dir", transformed_dir)
        self.reg_int = re.compile(r"\d+")  # Like an integer
        self.reg_dec = re.compile("([0-9]+)\.([0-9]+)")  # Like a decimal
        self.rating = {'One': '1/5', 'Two': '2/5', 'Three': '3/5', 'Four': '4/5', 'Five': '5/5'}
        self.browse()

    def browse(self):
        """ Browse categories, products. Grouped by category, give transformed products """

        for category_name in self.extracted_dir.listdir():
            category = {}
            products = []
            category[category_name] = products
            category_extracted_dir = self.extracted_dir.path(category_name)
            for product_file in listdir(category_extracted_dir):
                # Absolute path of the file
                product_file = self.extracted_dir.path(category_extracted_dir, product_file)
                products.append(self.transform_product(product_file, category_name))

            category_file = self.transformed_dir.path(category_name + ".json")
            with open(category_file, 'w', encoding='utf-8') as json_file:
                json.dump(category, json_file)

    def transform_product(self, product_file, category_name):
        """ Get html contents, give pertinent datas """
        with open(product_file, "r", encoding='utf-8') as f:
            contents = f.read()
            soup = BeautifulSoup(contents, "html.parser")

        elements = {}
        elements[TITLE] = soup.find('h1').get_text()
        elements[PRODUCT_PAGE_URL] = product_file.split('/')[8].replace(SEPARATOR, '/')  # File name give url
        trs = soup.find_all('tr')
        elements[UNIVERSAL_PRODUCT_CODE] = trs[0].td.get_text()
        elements[CATEGORY] = category_name
        elements[PRICE_INCLUDING_TAX] = self.reg_dec.search(trs[2].td.get_text())[0]
        elements[PRICE_EXCLUDING_TAX] = self.reg_dec.search(trs[3].td.get_text())[0]
        elements[NUMBER_AVAILABLE] = self.reg_int.search(trs[5].td.get_text())[0]
        elements[IMAGE_URL] = urljoin(URL_TO_SCRAP, soup.find('img')['src'])
        elements[PRODUCT_DESCRIPTION] = soup.find_all('p')[3].get_text()
        star_rating = soup.find('p', attrs={'class': 'star-rating'}).attrs['class'][1]
        elements[REVIEW_RATING] = self.rating[star_rating]  # Transform star rating in ratio

        return elements


if __name__ == '__main__':
    Directory.chdir()
    Transform(EXTRACTED_DIR, TRANSFORMED_DIR)
