class Product:
	def __init__(self, cost, price, marque):
		self.cost = cost
		self.price = price
		self.marque = marque
		self.name=type(self).__name__
	
class Biens_Consommation(Product):
	def __init__(self,cost, price, marque):
		super().__init__(cost, price, marque)
		

class Articles_Menagers(Biens_Consommation):
	def __init__(self, cost, price, marque):
		super().__init__(cost, price, marque)

class Meubles(Articles_Menagers):
	def __init__(self, materiaux, couleur, dimension, cost, price, marque):
		super().__init__(cost, price, marque)
		self.materiaux = materiaux
		self.couleur = couleur
		self.dimension = dimension

class Canapes(Meubles):
	def __init__(self, materiaux, couleur, dimension, cost, price, marque):
		super().__init__(materiaux, couleur, dimension, cost, price, marque)

class Chaise(Meubles):
	def __init__(self, materiaux, couleur, dimension, cost, price, marque):
		super().__init__(materiaux, couleur, dimension, cost, price, marque)

class Table(Meubles):
	def __init__(self, materiaux, couleur, dimension, cost, price, marque):
		super().__init__(materiaux, couleur, dimension, cost, price, marque)

#################################@@

# Define a function that prompts the user to enter values for a given class
def prompt_for_instance(cls):
    # Get the names of the constructor arguments
    arg_names = cls.__init__.__code__.co_varnames[1:]
    # Prompt the user for the values of the arguments 
    print(cls.__name__,":")
    args = [input("Enter the value for {}: ".format(name)) for name in arg_names]
    # Create an instance of the class using the entered values
    return cls(*args)

#################################@@

def sep():
    print("\n====================\n")
    
sep()

# Prompt the user to create instances of the Biens_Consommation, Articles_Menagers, and Meubles classes
#biens_consommation = prompt_for_instance(Biens_Consommation)
#articles_menagers = prompt_for_instance(Articles_Menagers)

#chaussures = prompt_for_instance(Chaussures)
#print(vars(chaussures))

#################################@@

class InventoryProductEntry:
	def __init__(self, product:Product, quantity):
		self.product = product
		self.quantity = quantity
		self.sales = 0

	def sell(self, quantity):
		if self.quantity < quantity:
			print(f"Not enough {self.product.name} stock")
			return
		self.quantity -= quantity
		self.sales += quantity * self.product.price

	def restock(self, quantity):
		self.quantity += quantity

	def __repr__(self):
		return "{} ({}): {} in stock,  price:{}".format(type(self.product).__name__, self.product.marque, self.quantity, self.product.price)

#################################@@
from typing import Dict

class InventoryManager:
	def __init__(self):
		self.inventory : Dict[str, InventoryProductEntry] = {}

	def product_exists(self,product:Product):
		for inventory_product_entry_key in self.inventory:
			if (inventory_product_entry_key == product.name):
				return True
		return False
		
	def add_product(self, product:Product, quantity):
		#if product exists inventory, increase quantity 
		if self.product_exists(product):
			self.inventory[product.name].quantity+=quantity
		else:
			inventory_product_entry = InventoryProductEntry(product, quantity)
			self.inventory[product.name]=inventory_product_entry
			
	def remove_product(self, product:Product):
		if self.product_exists(product):
				self.inventory.pop(product.name)

	def sell_product(self, product:Product, quantity):
		for inventory_product_entry_key in self.inventory:
			if inventory_product_entry_key == product.name:
				self.inventory[inventory_product_entry_key].sell(quantity)
				self.revenue_tracker.add_sale(product, quantity)
				return
		print(f"product {product.name} not found")

	def restock_product(self, product:Product, quantity):
		for inventory_product_entry_key in self.inventory:
			if self.product_exists(product):
				self.inventory[inventory_product_entry_key].restock(quantity)
				return
		print(f"product {product.name} not found")

	def get_product(self, name):
		for inventory_product_entry_key in self.inventory:
			if inventory_product_entry_key == name:
				return self.inventory[inventory_product_entry_key].product
		print(f"product {name} not found")

	def list_products(self):
		for inventory_product_entry_key in self.inventory:
			print(self.inventory[inventory_product_entry_key])
	
	def list_products(self):
		for inventory_product_entry_key in self.inventory:
			print(self.inventory[inventory_product_entry_key])

# Create an instance of the inventory manager
#inventory_manager = InventoryManager()

import streamlit as st
from typing import Dict

# Define the Product, InventoryProductEntry, RevenueTracker, and InventoryManager classes as before

# Define a dictionary of product types and their corresponding classes
product_types = {
    "Canapes": Canapes,
    "Chaise": Chaise,
    "Table": Table
}

# Create an instance of the inventory manager
inventory_manager = InventoryManager()

# Define the Streamlit app
def app():
    # Set the page title
    #st.set_page_config(page_title="Inventory Manager")

    # Display a dropdown list of product types
    product_type = st.sidebar.selectbox("Select a product type", list(product_types.keys()))

    # Get the selected product type class
    product_class = product_types[product_type]

    # Prompt the user to enter the product details and quantity
    st.sidebar.write(f"Add {product_type}")
    materiaux = st.sidebar.text_input("Materiaux")
    couleur = st.sidebar.text_input("Couleur")
    dimension = st.sidebar.text_input("Dimension")
    cost = st.sidebar.number_input("Cost")
    price = st.sidebar.number_input("Price")
    marque = st.sidebar.text_input("Marque")
    quantity = st.sidebar.number_input("Quantity")

    # Handle the case where the user has entered all the product details and clicked the "Add" button
    if st.sidebar.button("Add"):
        # Create a new product instance and add it to the inventory manager
        product = product_class(materiaux, couleur, dimension, cost, price, marque)
        inventory_manager.add_product(product, quantity)
        st.success(f"{quantity} {product_type} added to inventory")

    # Display a dropdown list of available products
    product_names = [entry.product.name for entry in inventory_manager.inventory.values()]
    selected_product_name = st.sidebar.selectbox("Select a product to sell", product_names)

    # Handle the case where the user has selected a product and entered a quantity to sell
    sell_quantity = st.sidebar.number_input(f"Enter quantity to sell for {selected_product_name}")
    if st.sidebar.button("Sell"):
        # Find the corresponding product entry in the inventory manager and sell the specified quantity
        for entry in inventory_manager.inventory.values():
            if entry.product.name == selected_product_name:
                entry.sell(sell_quantity)
                st.success(f"{sell_quantity} {selected_product_name} sold")

    # Display the current inventory
    st.write("Current Inventory:")
    for entry in inventory_manager.inventory.values():
        st.write(entry)

    # Add a button to show the inventory
    if st.button("Show inventory"):
        st.write("Current inventory:")
        inventory_entries = inventory_manager.inventory
        if not inventory_entries:
            st.write("The inventory is empty.")
        else:
            for entry in inventory_entries:
                st.write(entry)
app()
