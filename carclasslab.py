"""
Car class Lab written by Kevin Oyowe
October 10, 2016
"""
class Car(object):
	def __init__(self, name='General', model='GM', type=None):
		# Initialize the class
		self.name  = name
		self.model = model
		self.type  = type
		self.speed = 0

		if self.name == 'Koenigsegg' or self.name =='Porshe':
			self.num_of_doors = 2
		else:
			self.num_of_doors = 4

		if self.type == 'trailer':
			self.num_of_wheels = 8
		else:
			self.num_of_wheels = 4
		
	def is_saloon(self):
		# Boolean check for saloon car
		if self.type == 'trailer':
			return False
		else:
			return True

	def drive(self, speed):
		# .drive class
		if speed == 7:
			self.speed = 77  
		elif speed == 3:
			self.speed = 1000
		return self