import json

from common.directory import Directory


class Load:
    """ Read the transformed datas and make csv files, one for each category """

    def __init__(self, transformed_dir, loaded_dir):
        """ (Re)create main directory """
        self.transformed_dir = Directory("working_dir", transformed_dir, init=False)
        self.loaded_dir = Directory("working_dir", loaded_dir)
        self.browse()

    def browse(self):
        """ For each category, read the .json file, create a .csv file """
        for category_file in self.transformed_dir.listdir():
            category_file = self.transformed_dir.path(category_file)
            with open(category_file, 'r', encoding='utf-8') as json_file:
                category_dict = json.load(json_file)
                category_name = list(category_dict)[0]  # Category's name is in first key
                products_dict = category_dict[category_name]
                self.write(category_name, products_dict)

    def write(self, category_name, products_dict):
        pass
