from urllib import request

from common.constantes import *
from common.directory import Directory
from load.load import Load


class LoadImages(Load):
    """ Read the transformed datas and write images files, grouped by category """

    def write(self, category_name, products_dict):
        """ Create category's dir, browse products and, for each, write image """
        category_images_dir = self.loaded_dir.path(category_name)
        Directory(category_images_dir)
        for product in products_dict:
            image_url = product[IMAGE_URL]
            image_file = image_url.split('/')
            # Extract last item (name of the image + '.jpg')
            image_file = image_file[len(image_file) - 1]
            # Absolute path of the file
            image_file = self.loaded_dir.path(category_name, image_file)
            request.urlretrieve(image_url, image_file)
