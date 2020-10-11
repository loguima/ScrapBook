import os
from urllib.request import urlretrieve
from extract.extract import Extract


class ExtractProduct(Extract):
    """ Extract contents of a product page """

    def _extract(self):
        extract_file = os.path.join(self._extract_dir, self._url.split('/')[4] + ".html")
        urlretrieve(self._url, extract_file)
