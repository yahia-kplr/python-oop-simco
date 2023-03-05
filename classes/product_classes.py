class Product:
	def __init__(self, cost, price, marque):
		self.cost = int(cost)
		self.price = int(price)
		self.marque = marque
		self.name=type(self).__name__

class Biens_Consommation(Product):
	def __init__(self, cost, price, marque):
		super().__init__(cost, price, marque)

class Articles_Menagers(Biens_Consommation):
	def __init__(self, cost, price, marque):
		super().__init__(cost, price, marque)

class Meubles(Articles_Menagers):
	def __init__(self, materiaux, couleur, dimensions, cost, price, marque):
		super().__init__(cost, price, marque)
		self.materiaux = materiaux
		self.couleur = couleur
		self.dimensions = dimensions

class Canape(Meubles):
	def __init__(self, materiaux, couleur, dimensions, cost, price, marque):
		super().__init__(materiaux, couleur, dimensions, cost, price, marque)

class Chaise(Meubles):
	def __init__(self, materiaux, couleur, dimensions, cost, price, marque):
		super().__init__(materiaux, couleur, dimensions, cost, price, marque)

class Table(Meubles):
	def __init__(self, materiaux, couleur, dimensions, cost, price, marque):
		super().__init__(materiaux, couleur, dimensions, cost, price, marque)

class Appareils_Electromenagers(Articles_Menagers):
	def __init__(self, capacites, cost, price, marque):
		super().__init__(cost, price, marque)
		self.capacites = capacites

class Refrigerateur(Appareils_Electromenagers):
	def __init__(self, efficacite, capacites, cost, price, marque):
		super().__init__(capacites, cost, price, marque)
		self.efficacite = efficacite

class Lave_vaisselle(Appareils_Electromenagers):
	def __init__(self, programme, capacites, cost, price, marque):
		super().__init__(capacites, cost, price, marque)
		self.programme = programme

class Lave_linge(Appareils_Electromenagers):
	def __init__(self, programme, capacites, cost, price, marque):
		super().__init__(capacites, cost, price, marque)
		self.programme = programme

class Ustensiles_Cuisine(Articles_Menagers):
	def __init__(self, materiaux, cost, price, marque):
		super().__init__(cost, price, marque)
		self.materiaux = materiaux

class Casserole_Poele(Ustensiles_Cuisine):
	def __init__(self, diametre, materiaux, cost, price, marque):
		super().__init__(materiaux, cost, price, marque)
		self.diametre = diametre

class Batterie_Cuisine(Ustensiles_Cuisine):
	def __init__(self, nombre_pieces, materiaux, cost, price, marque):
		super().__init__(materiaux, cost, price, marque)
		self.nombre_pieces = nombre_pieces

class Vetements_Accessoires(Biens_Consommation):
	def __init__(self, cost, price, marque):
		super().__init__(cost, price, marque)

class Vetements(Vetements_Accessoires):
	def __init__(self, taille, couleur, matiere, cost, price, marque):
		super().__init__(cost, price, marque)
		self.taille = taille
		self.couleur = couleur
		self.matiere = matiere

class Haut(Vetements):
	def __init__(self, taille, couleur, matiere, cost, price, marque):
		super().__init__(taille, couleur, matiere, cost, price, marque)

class Pantalon(Vetements):
	def __init__(self, taille, couleur, matiere, cost, price, marque):
		super().__init__(taille, couleur, matiere, cost, price, marque)

class Robe(Vetements):
	def __init__(self, taille, couleur, matiere, cost, price, marque):
		super().__init__(taille, couleur, matiere, cost, price, marque)

class Accessoires(Vetements_Accessoires):
	def __init__(self, couleur, cost, price, marque):
		super().__init__(cost, price, marque)
		self.couleur = couleur

class Chaussures(Vetements_Accessoires):
	def __init__(self, pointure, cost, price, marque):
		super().__init__(cost, price, marque)
		self.pointure = pointure

