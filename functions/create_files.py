from data import config
from functions.utils.touch import touch


def create_files():
    touch(config.FILES_DIR)
    touch(config.MNEMONICS_FILE, True)


create_files()
