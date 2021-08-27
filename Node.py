from config import *

class Node:
	def __init__(self, row, col, width, total_rows, color = WHITE):
		self.row = row
		self.col = col
		self.x = row * width
		self.y = col * width
		self.color = color
		self.neighbors = []
		self.width = width
		self.total_rows = total_rows
		self.state =''

	def get_pos(self):
		return self.row, self.col

	def is_closed(self):
		return self.color == RED

	def is_open(self):
		return self.color == GREEN

	def is_barrier(self):
		return self.color == BLACK

	def is_start(self):
		return self.color == ORANGE

	def is_end(self):
		return self.color == TURQUOISE

	def getState(self):
		return self.state

	def reset(self):
		self.color = WHITE

	def make_start(self):
		self.state = 'start'

	def make_closed(self):
		self.state = 'closed'

	def make_open(self):
		self.state = 'open'

	def make_barrier(self):
		self.state = 'barrier'

	def make_end(self):
		self.state = 'end'

	def make_path(self):
		self.color = PURPLE

	def make_player(self):
		self.color = GREY

	def make_NPC(self):
		self.color = BLUE

	def draw(self, win):
	    pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

	def update_neighbors(self, grid):
		self.neighbors = []
		if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].getState == 'barrier': # DOWN
			self.neighbors.append(grid[self.row + 1][self.col])

		if self.row > 0 and not grid[self.row - 1][self.col].getState == 'barrier': # UP
			self.neighbors.append(grid[self.row - 1][self.col])

		if self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].getState == 'barrier': # RIGHT
			self.neighbors.append(grid[self.row][self.col + 1])

		if self.col > 0 and not grid[self.row][self.col - 1].getState == 'barrier': # LEFT
			self.neighbors.append(grid[self.row][self.col - 1])

	def __lt__(self, other):
		return False