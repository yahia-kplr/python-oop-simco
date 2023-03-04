import sys
sys.path.extend(['.','..'])
import streamlit as st
from typing import Dict
from ui import *
import utils
# from streamlitApp import InventoryManager
# Define the Product, InventoryProductEntry, RevenueTracker, and InventoryManager classes as before
RANDOM_SEED = 142
K_FOLDS = 10
import streamlit as st


def main():
    run()

if __name__ == '__main__':
    main()