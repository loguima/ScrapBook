from common.constantes import *
from extract.extract_main import ExtractMain
from load.loaddata import LoadData
from load.loadimages import LoadImages
from transform.transform import Transform

if __name__ == '__main__':
    ExtractMain(URL_TO_SCRAP, EXTRACTED_DIR)
    Transform(EXTRACTED_DIR, TRANSFORMED_DIR)
    LoadData(TRANSFORMED_DIR, LOADED_DIR)

    LoadImages(TRANSFORMED_DIR, IMAGES_DIR)
