import sys
sys.path.extend(['.','..'])
import streamlit as st
from typing import Dict
from inventory.stock_manager import *
import utils
# from streamlitApp import InventoryManager
# Define the Product, InventoryProductEntry, RevenueTracker, and InventoryManager classes as before
import streamlit as st


def run():
    inventory_manager = InventoryManager()

    #from PIL import Image
    #image = Image.open('ehtp.jpg')
    #image_univ = Image.open('class.jpg')
    #st.image(image)
    st.sidebar.title("KPLR")
    st.sidebar.markdown("What would you like to do?")

    #st.sidebar.info('What would you like to do?')
    #st.sidebar.image(image_univ)
    add_selectbox = st.sidebar.selectbox("Select a Letter:",\
        ("A. Add a product to stock",
        "R. Restock a product quantity",
        "S. Sell a product quantity",
		"D. Remove a product from stock",
		"L. List the products in stock",
		"B. Show the current balance"))
    #choose_selectbox = st.sidebar.selectbox("choose your prediction method?",("Facture","Client"))
    st.title("Inventory Manager App")
    # @st.cache(persist=True,allow_output_mutation=True)
    if add_selectbox == 'A. Add a product to stock':
        name  = st.text_input("Enter the name of the product:")
        #mettre à jour avec le mécanisme du prompt.
        quantity = st.number_input("Enter the initial quantity of the product:", 1, 100, step=1, key="quantity")
        product = Product(cost, price, marque)
        inventory_manager.add_product(product, quantity)
        #N_year_fact = st.number_input("Enter the initial quantity of the product:", 1, 100, step=1, key="N_year_fact")
        if st.button("Validation"):
            st.success(f"{name} has been added to stock with a quantity of {quantity}.", icon="✅")
    
    elif add_selectbox == 'R. Restock a product quantity':
        name  = st.text_input("Enter the name of the product:")
        quantity = st.number_input("Enter the quantity to restock: ", 1, 100, step=1, key="quantity")
        product = inventory_manager.get_product(name)
        resultat = ProfitTracker
        #N_year_fact = st.number_input("Enter the initial quantity of the product:", 1, 100, step=1, key="N_year_fact")
        if st.button("Validation"):
            if product:
				#name_inv,valeur_calcul=inventory_manager.restock_product(product, quantity)
                inventory_manager.restock_product(product, quantity)
                st.success(f"Profit actuel après restockage du produit {product.name} est : {resultat.total_profit_res} euros\n", icon="✅")
            else:
                st.warning(f"{name} is not in stock.", icon="⚠️")
				
    elif add_selectbox == 'S. Sell a product quantity':
        name  = st.text_input("Enter the name of the product:")
        quantity = st.number_input("Enter the quantity to sell: ", 1, 100, step=1, key="quantity")
        product = inventory_manager.get_product(name)
        resultat = Product
        #N_year_fact = st.number_input("Enter the initial quantity of the product:", 1, 100, step=1, key="N_year_fact")
        if st.button("Validation"):
            if product:
				#name_inv,valeur_calcul=inventory_manager.restock_product(product, quantity)
                inventory_manager.restock_product(product, quantity)
                #st.success(f"Profit actuel après restockage du produit {name_inv} est : {valeur_calcul} euros\n", icon="✅")
            else:
                st.warning(f"{name} is not in stock.", icon="⚠️")
    
    elif add_selectbox == 'D. Remove a product from stock':
        name  = st.text_input("Enter the name of the product:")
        product = inventory_manager.get_product(name)
        resultat = Product
        #N_year_fact = st.number_input("Enter the initial quantity of the product:", 1, 100, step=1, key="N_year_fact")
        if st.button("Validation"):
            if product:
				#name_inv,valeur_calcul=inventory_manager.restock_product(product, quantity)
                inventory_manager.remove_product(product)
                st.success(f"{name} has been removed from stock", icon="✅")
            else:
                st.warning(f"{name} is not in stock.", icon="⚠️")
    
    elif add_selectbox == 'L. List the products in stock':
        name  = st.text_input("Enter the name of the product:")
        quantity = st.number_input("Enter the quantity to sell: ", 1, 100, step=1, key="quantity")
        product = inventory_manager.get_product(name)
        resultat = Product
        #N_year_fact = st.number_input("Enter the initial quantity of the product:", 1, 100, step=1, key="N_year_fact")
        if st.button("Validation"):
            if product:
				#name_inv,valeur_calcul=inventory_manager.restock_product(product, quantity)
                inventory_manager.restock_product(product, quantity)
                #st.success(f"Profit actuel après restockage du produit {name_inv} est : {valeur_calcul} euros\n", icon="✅")
            else:
                st.warning(f"{name} is not in stock.", icon="⚠️")
    
    elif add_selectbox == 'B. Show the current balance':
        name  = st.text_input("Enter the name of the product:")
        quantity = st.number_input("Enter the quantity to sell: ", 1, 100, step=1, key="quantity")
        product = inventory_manager.get_product(name)
        resultat = Product
        #N_year_fact = st.number_input("Enter the initial quantity of the product:", 1, 100, step=1, key="N_year_fact")
        if st.button("Validation"):
            if product:
				#name_inv,valeur_calcul=inventory_manager.restock_product(product, quantity)
                inventory_manager.restock_product(product, quantity)
                #st.success(f"Profit actuel après restockage du produit {name_inv} est : {valeur_calcul} euros\n", icon="✅")
            else:
                st.warning(f"{name} is not in stock.", icon="⚠️")