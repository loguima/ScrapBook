from common.directory import Directory
from extract.extract import Extract
from extract.extract_product import ExtractProduct


class ExtractCategory(Extract):
    """ Extract contents of categories and browse the products """

    def create_dir(self):
        """ Create category's directory. """
        self.extracted_dir = Directory(self.extracted_dir)

    def browse(self):
        """  Browse products for all pages of the category """

        soup = self.soup
        loop = True
        while loop:
            self.browse_current_page(soup)
            is_next = soup.select_one('li.next a')
            if is_next:
                url_next = self.urlpath(is_next['href'])
                soup = self.make_soup(url_next)
            else:
                loop = False

    def browse_current_page(self, soup):
        """ Browse products from current page of the category """
        products = soup.select('div.image_container a')
        for result in products:
            url_product = self.urlpath(result['href'])
            ExtractProduct(url_product, self.extracted_dir.directory)
