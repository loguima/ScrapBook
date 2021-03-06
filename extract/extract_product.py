import os

import requests

from common.constantes import SEPARATOR
from extract.extract import Extract


class ExtractProduct(Extract):
    """ Store product's page (same as book's page) """

    def extract(self):
        extract_file = self.url.replace('/', SEPARATOR)  # Translate URL to give file name
        extract_file = extract_file.replace('http:', '')  # ':' not allowed for Windows files system
        extract_file = os.path.join(self.extracted_dir, extract_file)  # Absolute path of file in category's directory
        r = requests.get(self.url)
        r.encoding = 'utf-8'
        contents = r.text
        with open(extract_file, "w", encoding='utf-8') as f:
            f.write(contents)
