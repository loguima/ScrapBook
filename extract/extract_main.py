
import shutil
import os
from urllib.parse import urljoin

from extract.extract import Extract
from extract.extract_category import ExtractCategory


class ExtractMain(Extract):
    """ Extract contents of the first page and browse the categories """

    def _extract(self):
        """ Remove / (re)create main directory. Browse categories """
        base_extract_dir = os.path.join(os.getcwd(), self._extract_dir)
        shutil.rmtree(base_extract_dir, ignore_errors=True, onerror=None)
        os.makedirs(base_extract_dir, exist_ok=True)

        # Extract categories from the page : label and url
        categories = self._soup.select('div.side_categories ul.nav.nav-list li ul li a')
        for i, result in enumerate(categories):
            url_category = urljoin(self._url, result['href'])
            category = result.get_text().strip()
            extract_dir = os.path.join(base_extract_dir, category)
            ExtractCategory(url_category, extract_dir)
