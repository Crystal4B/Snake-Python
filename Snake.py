# This class represents the Snake
class Snake:
	x = []
	y = []
	direction = 0
	length = 0
	speed = 0

	# init for our snake
	def __init__(self, length, speed):
		self.speed = speed
		self.x.append(0)
		self.y.append(0)
		self.length += 1
		for i in range(1, length):
			self.feed()

	def update(self):
		# Update position of the body
		for i in range(self.length-1, 0, -1):
			self.x[i] = self.x[i-1]
			self.y[i] = self.y[i-1]

		# Update position of the head
		if self.direction == 0:
			self.x[0] += self.speed
		elif self.direction == 1:
			self.x[0] -= self.speed
		elif self.direction == 2:
			self.y[0] -= self.speed
		elif self.direction == 3:
			self.y[0] += self.speed

	def move(self, direction):
		if direction == 'R' and self.direction != 1:
			self.direction = 0
		elif direction == 'L' and self.direction != 0:
			self.direction = 1
		elif direction == 'U' and self.direction != 3:
			self.direction = 2
		elif direction == 'D' and self.direction != 2:
			self.direction = 3

	def feed(self):
		if self.direction == 0:
			self.x.append(self.x[self.length-1]-self.speed)
			self.y.append(self.y[self.length-1])
		if self.direction == 1:
			self.x.append(self.x[self.length-1]+self.speed)
			self.y.append(self.y[self.length-1])
		if self.direction == 2:
			self.x.append(self.x[self.length-1])
			self.y.append(self.y[self.length-1]+self.speed)
		if self.direction == 3:
			self.x.append(self.x[self.length-1])
			self.y.append(self.y[self.length-1]-self.speed)
		self.length += 1