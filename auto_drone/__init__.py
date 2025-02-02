import os
import shutil
from pathlib import Path

name = 'auto_drone'
version = '0.1'

SOURCE_PACKAGE = os.path.split(__file__)[0]
PROJECT_PATH = os.path.split(SOURCE_PACKAGE)[0]

RESOURCES_DIR = os.path.join(PROJECT_PATH, 'resources')
IMAGE_RESOURCES_DIR = os.path.join(RESOURCES_DIR, 'images')

LOG_DIR = os.path.join(PROJECT_PATH, 'logs')
DATA_DIR = os.path.join(PROJECT_PATH, 'data')
DOC_DIR = os.path.join(PROJECT_PATH, 'docs')

TERMINAL_COLUMNS, TERMINAL_ROWS = shutil.get_terminal_size()


def __init_dirs() -> None:
    dir_list = [
        DOC_DIR,
        LOG_DIR,
        DATA_DIR
    ]
    for each_dir in dir_list:
        each_dir_path = Path(each_dir)
        if not each_dir_path.exists():
            each_dir_path.mkdir(parents=True, exist_ok=True)
    return


__init_dirs()
