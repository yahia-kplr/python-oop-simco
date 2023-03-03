from product_classes import *

#################################

def sep():
    print("\n====================\n")
    
sep()

# Prompt the user to create instances of the Biens_Consommation, Articles_Menagers, and Meubles classes
#biens_consommation = prompt_for_instance(Biens_Consommation)
#articles_menagers = prompt_for_instance(Articles_Menagers)
"""
chaussures = prompt_for_instance(Chaussures)
print(vars(chaussures))
"""
#################################

class InventoryProductEntry:
	def __init__(self, product:Product, quantity):
		self.product = product
		self.quantity = quantity
		self.sales = 0
		self.expenses = 0

	def sell(self, quantity):
		if self.quantity < quantity:
			print(f"Not enough {self.product.name} stock")
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
		self.total_revenue=0
		self.total_profit = 0
		self.total_cost = 0
		self.balance= 1000

	def buy_product(self, product:Product,quantity):
		if self.balance < product.cost * quantity:
			print("Not enough money to restock")
			return False
		else:
			self.balance= self.balance - (product.cost * quantity)
			print("balance après achat", self.balance)
			return True
	
	def sell_product(self, product:Product,quantity):
		self.balance= self.balance + (product.price * quantity)
		print("balance après vente",self.balance)

	def calcul_profit(self):
		for inventory_product_entry_key in inventory_manager.inventory:
			self.total_revenue += inventory_manager.inventory[inventory_product_entry_key].sales
			self.total_cost += inventory_manager.inventory[inventory_product_entry_key].expenses

		self.total_profit = self.total_revenue - self.total_cost
		return self.total_profit

#################################

from typing import Dict

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
				if self.inventory[inventory_product_entry_key].sell(quantity):
					self.profit_tracker.sell_product(product, quantity)					
				return
		print(f"product {product.name} not found")

	def restock_product(self, product:Product, quantity):
		for inventory_product_entry_key in self.inventory:
			if self.product_exists(product):
				if (self.profit_tracker.buy_product(product, quantity)):
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

#################################

# Create an instance of the inventory manager and profit manager
inventory_manager = InventoryManager()
# Add some products to the inventory
inventory_manager.add_product(Canapes("materiau1", "couleur1", "dimension1", 100, 200, "marque1"), 10)
inventory_manager.add_product(Chaise("materiau2", "couleur2", "dimension2", 50, 100, "marque2"), 20)
inventory_manager.add_product(Table("materiau3", "couleur3", "dimension3", 150, 180,"BULTEX"),12)

inventory_manager.sell_product(inventory_manager.get_product("Chaise"),6)

inventory_manager.restock_product(inventory_manager.get_product("Canapes"),4)

#print(inventory_manager.revenue_tracker.get_revenue())

#print(inventory_manager.revenue_tracker.get_sales())

inventory_manager.list_products()

#################################

#canap = Canapes("materiau1", "couleur1", "dimension1", 100, 200, "marque1")

#profit_tracker= ProfitTracker()
#print("Profit : ",p.calcul_profit())
#print("Revenue : ",p.total_revenue, ", Cost : ",p.total_cost,", Profit : ",p.total_profit,", Balance : ",  p.balance)