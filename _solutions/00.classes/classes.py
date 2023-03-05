class Product:
	def __init__(self, cost, price, marque):
		self.cost = int(cost)
		self.price = int(price)
		self.marque = marque
		self.name=type(self).__name__

class Meubles(Product):
	def __init__(self, materiaux, couleur, dimensions, cost, price, marque):
		super().__init__(cost, price, marque)
		self.materiaux = materiaux
		self.couleur = couleur
		self.dimensions = dimensions

class Canape(Meubles):
	def __init__(self, materiaux, couleur, dimension, cost, price, marque):
		super().__init__(materiaux, couleur, dimension, cost, price, marque)

class Chaise(Meubles):
	def __init__(self, materiaux, couleur, dimension, cost, price, marque):
		super().__init__(materiaux, couleur, dimension, cost, price, marque)

class Table(Meubles):
	def __init__(self, materiaux, couleur, dimension, cost, price, marque):
		super().__init__(materiaux, couleur, dimension, cost, price, marque)