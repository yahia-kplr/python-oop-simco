from stock_manager import *
import utils

def main():
	inventory_manager = InventoryManager()
	
	while True:
		print("""
			What would you like to do? Enter a number:
			A. Add a product to stock
			R. Restock a product quantity
			S. Sell a product quantity
			D. Remove a product from stock
			L. List the products in stock
			B. Show the current balance
			B. Quit
		""")
		
		try:
			choice = input("Enter your choice: ")
		except ValueError:
			print("Invalid choice. Please enter a number.")
			continue
		
		if choice == "A":
			name = input("Enter the name of the product: ")
			cost = float(input("Enter the cost of the product: "))
			price = float(input("Enter the price of the product: "))
			marque = input("Enter the brand of the product: ")
			quantity = int(input("Enter the initial quantity of the product: "))
			product = Product(cost, price, marque)
			inventory_manager.add_product(product, quantity)
			print(f"{name} has been added to stock with a quantity of {quantity}.")
		
		elif choice == "R":
			name = input("Enter the name of the product: ")
			quantity = int(input("Enter the quantity to restock: "))
			product = inventory_manager.get_product(name)
			if product:
				inventory_manager.restock_product(product, quantity)
			else:
				print(f"{name} is not in stock.")
		
		elif choice == "S":
			name = input("Enter the name of the product: ")
			quantity = int(input("Enter the quantity to sell: "))
			product = inventory_manager.get_product(name)
			if product:
				inventory_manager.sell_product(product, quantity)
			else:
				print(f"{name} is not in stock.")
		
		elif choice == "D":
			name = input("Enter the name of the product: ")
			product = inventory_manager.get_product(name)
			if product:
				inventory_manager.remove_product(product)
				print(f"{name} has been removed from stock.")
			else:
				print(f"{name} is not in stock.")
		
		elif choice == "L":
			inventory_manager.list_products()
		
		elif choice == "B":
			print(f"Current balance: {inventory_manager.profit_tracker.balance} euros")
		
		elif choice == "Q":
			print("Goodbye!")
			break
		
		else:
			print("Invalid choice. Please enter a number between 1 and 7.")
	
if __name__ == '__main__':
	main()
