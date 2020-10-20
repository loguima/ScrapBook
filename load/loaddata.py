import csv

from common.constantes import *
from load.load import Load


class LoadData(Load):
    """ Read the transformed data and make csv files, one for each category """

    def write(self, category_name, products_dict):
        category_file_csv = self.loaded_dir.path(category_name + '.csv')
        with open(category_file_csv, mode='w', encoding='utf-8', newline='') as csv_file:
            fieldnames = [PRODUCT_PAGE_URL, UNIVERSAL_PRODUCT_CODE, TITLE, PRICE_INCLUDING_TAX,
                          PRICE_EXCLUDING_TAX, NUMBER_AVAILABLE, PRODUCT_DESCRIPTION, CATEGORY,
                          REVIEW_RATING, IMAGE_URL]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames, extrasaction='ignore')

            writer.writeheader()
            writer.writerows(products_dict)
