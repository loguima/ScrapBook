import os
from urllib.parse import urljoin

from extract.extract import Extract
from extract.extract_product import ExtractProduct


class ExtractCategory(Extract):
    """ Extract contents of categories and browse the products """

    def _extract(self):
        """ Create category's directory. Browse products for all pages of the category """
        os.makedirs(self._extract_dir, exist_ok=True)

        soup = self._soup
        loop = True
        while loop:
            self._search_products(soup, self._extract_dir)
            is_next = soup.select_one('li.next a')
            if is_next:
                url_next = urljoin(self._url, is_next['href'])
                soup = self._make_soup(url_next)
            else:
                loop = False

    def _search_products(self, soup, extract_dir):
        """ Browse products for current page of the category """
        products = soup.select('div.image_container a')
        for i, result in enumerate(products):
            url_product = urljoin(self._url, result['href'])
            ExtractProduct(url_product, extract_dir)

