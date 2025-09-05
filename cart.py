"""
TASK: Create a ShoppingCart class.

Requirements:
1. Store cart items in a dictionary (item → quantity).
2. Provide a method to add items.
3. Provide a method to remove items.
4. Provide a method to clear the cart.
5. Provide a method to calculate total price (with price list).

Example Usage:
    prices = {"Shirt": 5000, "Shoes": 12000}
    cart = ShoppingCart(prices)
    cart.add_item("Shirt", 2)
    print(cart.calculate_total())  # 10000
    cart.remove_item("Shirt", 1)
    print(cart.calculate_total())  # 5000
"""

class ShoppingCart:
	# class variable

	def __init__(self, prices):
		self.prices = prices
		self.items = {}

	def add_item(self, item, quantity=1):
		self.items[item] = self.items.get(item, 0) + quantity
	def remove_item(self, item, quantity=1):
		if item in self.items:
			self.items[item] = max(0,self.items[item] - quantity)
			self.items={k: v for k, v in self.items.items() if v > 0}
	def clear_cart(self):
		return self.items.clear()
	def calculate_total(self):
		return sum(self.prices.get(item, 0) * qty for item, qty in self.items.items())
	

cart = ShoppingCart
prices = {"Shirt": 5000, "Shoes": 12000}
cart = ShoppingCart(prices)
cart.add_item("Shirt", 2)
print(cart.calculate_total())  # 10000
cart.remove_item("Shirt", 1)
print(cart.calculate_total())  # 5000

