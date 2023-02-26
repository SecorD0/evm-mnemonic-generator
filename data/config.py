import os
import sys
from pathlib import Path

if getattr(sys, 'frozen', False):
    ROOT_DIR = Path(sys.executable).parent.absolute()
else:
    ROOT_DIR = Path(__file__).parent.parent.absolute()

FILES_DIR = os.path.join(ROOT_DIR, 'files')

ERRORS_FILE = os.path.join(FILES_DIR, 'errors.log')

MNEMONICS_FILE = os.path.join(FILES_DIR, 'mnemonics.txt')
