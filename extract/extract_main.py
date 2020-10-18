from common.directory import Directory
from extract.extract import Extract
from extract.extract_category import ExtractCategory


class ExtractMain(Extract):
    """ Extract contents of the first page and browse the categories """

    def create_dir(self):
        """ Remove / (re)create main directory : extracted. """
        self.extracted_dir = Directory("working_dir", self.extracted_dir)

    def browse(self):
        """  Browse categories """

        # Extract categories from the page : label and url
        categories = self.soup.select('div.side_categories ul.nav.nav-list li ul li a')
        for result in categories:
            url_category = self.urlpath(result['href'])
            category = result.get_text().strip()
            extracted_dir = self.extracted_dir.path(category)
            ExtractCategory(url_category, extracted_dir)
