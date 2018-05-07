class Restaurant:
	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
	def describe_restaurant(self):
		print(f"The name of the restaurant is {self.restaurant_name}")
		print(f"It serves {self.cuisine_type} food!")
	def open_restuarant(self):
		print(f"The {self.restaurant_name} is open!")

pizza_hut = Restaurant("Pizza Hut", "Italian")
print(pizza_hut.restaurant_name)
print(pizza_hut.cuisine_type)
pizza_hut.describe_restaurant()
pizza_hut.open_restuarant()