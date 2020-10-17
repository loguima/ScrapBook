from common.constantes import *
from extract.extract_main import ExtractMain
from transform.transform import Transform
from load.load import Load

if __name__ == '__main__':
    ExtractMain(URL_TO_SCRAP, EXTRACTED_DIR)
    Transform(EXTRACTED_DIR, TRANSFORMED_DIR)
    Load(TRANSFORMED_DIR, LOADED_DIR)