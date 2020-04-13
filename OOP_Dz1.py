

class Products():
	def __init__(self, name, category, unit, price):
		self.name = name
		self.category = category
		self.unit = unit
		self.price = price

	def is_eatable(self):
		if self.category != 'HC':
			return True
		else:
			return False

	def price_total(self):
		return self.unit*self.price

class Basket():
	def __init__(self):
		self.list = []

	def add_product(self, name, category, unit, price):
		product = Products(name, category, unit, price)
		self.list.append(product)

	def price_total(self):
		sum = 0
		for i in self.list:
			sum += i.price_total()
		return ('Total: %s hrn' %(sum))

	def eatable_products(self):
		for i in self.list:
			if i.is_eatable():
				return ('Everything is eatable!')
			else:
				return ('Not everything is eatable!')


glass_cleaner = Products('glass_cleaner', 'HC', 1, 43)
butter = Products('butter', 'food', 2, 46)
juice = Products('juice', 'drink', 3, 25)
soap = Products('soap', 'HC', 1, 21)
croissant = Products('croissant', 'food', 4, 8)

fill_basket = Basket()
fill_basket.add_product('glass_cleaner', 'HC', 1, 43)
fill_basket.add_product('butter', 'food', 2, 46)
fill_basket.add_product('juice', 'drink', 3, 25)
fill_basket.add_product('soap', 'HC', 2, 21)
fill_basket.add_product('croissant', 'food', 4, 8)

print(fill_basket.price_total())
print(fill_basket.eatable_products())




