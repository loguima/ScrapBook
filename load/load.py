import json
import csv

from common.directory import Directory
from common.constantes import *

class Load:
    """ Read the transformed datas and make csv files, one for each category """
    def __init__(self, transformed_dir, loaded_dir):
        """ (Re)create main directory : loaded """
        self.transformed_dir = Directory("working_dir", transformed_dir, init=False)
        self.loaded_dir = Directory("working_dir", loaded_dir)
        self.browse()

    def browse(self):
        """ For each category, read the .json file, create a .csv file """
        for category_file in self.transformed_dir.listdir():
            category_file = self.transformed_dir.path(category_file)
            with open(category_file, 'r', encoding='utf-8') as json_file:
                category_dict = json.load(json_file)
                self.write_csv(category_dict)

    def write_csv(self, category_dict):
        category_name = list(category_dict)[0]  # Category's name is in first key
        products_dict = category_dict[category_name]
        category_file_csv = self.loaded_dir.path(category_name + '.csv')
        with open(category_file_csv, mode='w', encoding='utf-8') as csv_file:
            fieldnames = [PRODUCT_PAGE_URL, UNIVERSAL_PRODUCT_CODE, TITLE, PRICE_INCLUDING_TAX,
                          PRICE_EXCLUDING_TAX, NUMBER_AVAILABLE, PRODUCT_DESCRIPTION, CATEGORY,
                          REVIEW_RATING, IMAGE_URL]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames, extrasaction='ignore')

            writer.writeheader()
            writer.writerows(products_dict)
