import sys
from pathlib import Path
import importlib

def load_module(directory, name):
    sys.path.insert(0, directory)
    importlib.import_module(name)
    sys.path.pop(0)

def load_directory(directory):
    