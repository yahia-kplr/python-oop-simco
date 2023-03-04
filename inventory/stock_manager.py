import sys
sys.path.extend(['.','..'])
from classes import *


from typing import Dict
#################################

class InventoryProductEntry:
	def __init__(self, product:Product, quantity):
		self.product = product
		self.quantity = quantity
		self.sales = 0
		self.expenses = 0

	def sell(self, quantity):
		if self.quantity < quantity:
			print(f"Le stock du produit {self.product.name} est insuffisant.")
			return False
		else:
			self.quantity -= quantity
			self.sales += quantity * self.product.price
			return True
				
	def restock(self, quantity):
		self.quantity += quantity
		self.expenses += quantity * self.product.cost

	def __repr__(self):
		return "{} ({}): {} in stock,  price:{}".format(type(self.product).__name__, self.product.marque, self.quantity, self.product.price)

#################################

class ProfitTracker:

	def __init__(self):		

		self.total_cost = 0
		self.balance= 1000

	def buy_product(self, product:Product,quantity):
		if self.balance < product.cost * quantity:
			print(f"Vous avez {self.balance} euros. Pour restocker {quantity} {product.name}, vous avez besoin de {product.cost * quantity} euros")
			return False
		else:
			self.balance= self.balance - (product.cost * quantity)
			print(f"balance après achat du produit {product.name} : {self.balance} euros")
			return True
	
	def sell_product(self, product:Product,quantity):
		self.balance= self.balance + (product.price * quantity)
		print(f"balance après vente du produit {product.name}  : {self.balance} euros")


#################################

class InventoryManager:
	def __init__(self):
		self.profit_tracker = ProfitTracker()
		self.inventory : Dict[str, InventoryProductEntry] = {}

	def product_exists(self,product:Product):
		for inventory_product_entry_key in self.inventory:
			if (inventory_product_entry_key == product.name):
				return True
		return False
		
	def add_product(self, product:Product, quantity):
		#if product exists inventory, increase quantity 
		if self.product_exists(product):
			#self.inventory[product.name].quantity+=quantity
			"Ce produit existe déja. (Une seule référence par produit)"
			pass
		else:
			inventory_product_entry = InventoryProductEntry(product, quantity)
			self.inventory[product.name]=inventory_product_entry
			
	def remove_product(self, product:Product):
		if self.product_exists(product):
				self.inventory.pop(product.name)

	def sell_product(self, product:Product, quantity):
		for inventory_product_entry_key in self.inventory:
			if inventory_product_entry_key == product.name:
				if self.inventory[inventory_product_entry_key].sell(quantity):
					self.profit_tracker.sell_product(product, quantity)
					print(f"Profit actuel après vente du produit {product.name} est : {self.calcul_profit()} euros\n")
				return
		print(f"product {product.name} not found")

	def restock_product(self, product:Product, quantity):		
		if self.product_exists(product):
			if (self.profit_tracker.buy_product(product, quantity)):
				self.inventory[product.name].restock(quantity)
				print(f"Profit actuel après restockage du produit {product.name} est : {self.calcul_profit()} euros\n")
				#return product.name,self.profit_tracker.calcul_profit()
		else:
			self.add_product(product,quantity)
			self.restock_product(product,quantity)

	def get_product(self, name):
		for inventory_product_entry_key in self.inventory:
			if inventory_product_entry_key == name:
				return self.inventory[inventory_product_entry_key].product
		print(f"product {name} not found")

	def list_products(self):
		for inventory_product_entry_key in self.inventory:
			print(self.inventory[inventory_product_entry_key])
		return self.inventory

	def calcul_profit(self):

		self.profit_tracker.total_revenue=0
		self.profit_tracker.total_profit = 0
		for inventory_product_entry_key in self.inventory:
			self.profit_tracker.total_revenue += self.inventory[inventory_product_entry_key].sales
			self.profit_tracker.total_cost += self.inventory[inventory_product_entry_key].expenses

		self.profit_tracker.total_profit = self.profit_tracker.total_revenue - self.profit_tracker.total_cost
		return self.profit_tracker.total_profit
	
# 	#################################

# Create an instance of the inventory manager
#inventory_manager = InventoryManager()

# 	# Add some products to the inventory
# inventory_manager.add_product(Canapes("materiau1", "couleur1", "dimension1", 100, 200, "marque1"), 10)
# inventory_manager.add_product(Chaise("materiau2", "couleur2", "dimension2", 50, 100, "marque2"), 20)
# inventory_manager.add_product(Table("materiau3", "couleur3", "dimension3", 150, 180,"BULTEX"),12)
# inventory_manager.add_product(Pantalon("M", "noir", "jeans", 150, 200,"Zara"),10)
# inventory_manager.add_product(Robe("S", "rose", "satin", 100, 140,"Zara"),5)

# utils.sep()
# 	# Show the content of the inventory
# print("List of products in the inventory\n")
# inventory_manager.list_products()

# 	# Remove product from the inventory
# inventory_manager.remove_product(Robe("S", "rose", "satin", 100, 140,"Zara"))

# utils.sep()
# 	# Show the content of the inventory
# print("After Removing a product\n")
# inventory_manager.list_products()

# 	#################################

# utils.sep()
# 	# Sell some products with existing quantity

# inventory_manager.sell_product(inventory_manager.get_product("Chaise"),6)
# inventory_manager.sell_product(inventory_manager.get_product("Canapes"),5)

# 	# Sell some products with unexisting quantity
# inventory_manager.sell_product(inventory_manager.get_product("Table"),20)

# 	#################################

# utils.sep()
# 	# Restock product not existing in the inventory
# inventory_manager.restock_product(Robe("S", "rose", "satin", 100, 140,"Zara"),5)

# utils.sep()

# 	# Restock product existing in the inventory
# inventory_manager.restock_product(Pantalon("M", "noir", "jeans", 150, 200,"Zara"),2)
# print("After Restocking a product\n")
# inventory_manager.list_products()

# utils.sep()

# 	# Restock product but not enough money
# inventory_manager.restock_product(Canapes("materiau1", "couleur1", "dimension1", 100, 200, "marque1"), 1000)

# 	#
