''' Node Object '''
class Node:
	def __init__(self, data):
		self.next = None
		self.data = data

''' Circle List Object '''
class CircleList:		
	def __init__(self):
		self.reference = None

	''' Find Last Element '''
	def find_last_node(self):
		if(self.reference == None):
			return None

		temp = self.reference

		while(temp.next != self.reference):
			temp = temp.next
		
		return temp

	''' List Size '''
	def listSize(self):
		if(self.reference == None):
			return 0

		if(first_node == first_node.next):
			return 1

		temp = self.reference
		count = 0
		while(temp.next != self.reference):
			temp = temp.next
			count = 0

		return count

	''' Add Element at Begin '''
	def add_begin_circle(self, data):
		new_node = Node(data)

		if(self.reference == None):
			self.reference = new_node
			new_node.next = self.reference
			return

		last_node = self.find_last_node()
		last_node.next = new_node
		new_node.next = self.reference
		self.reference = new_node

    ''' Add Element at End '''
	def add_end_circle(self, data):
		new_node = Node(data)
		
		if(self.reference == None):
			self.reference = new_node
			new_node.next = self.reference
			return

		last_node = self.find_last_node()
		last_node.next = new_node
		new_node.next = self.reference

    ''' Add Element at Position pos '''
	def add_pos_circle(self, data, pos):
		new_node = Node(data)
		
		if(self.reference == None):
			self.reference = new_node
			new_node.next = self.reference
			return

		if(pos > self.listSize()):
			raise ListSize('Position out of the list')

		count = 0
		temp_a = self.reference
		temp_b = temp_a.next
		while(pos < count):
			temp_a = temp_b
			temp_b = temp_a.next

		temp_a.next = new_node
		new_node.new_node = temp_b
		
    ''' Remove Element at Begin '''
	def remove_begin_circle(self):
		if(self.reference == None):
			raise ListEmpty('List Empty')

		first_node = self.reference
		if(first_node == first_node.next):
			self.reference = None

		last_node = self.find_last_node()
		self.reference = first_node.next
		last_node.next = self.reference

	''' Remove Element at End '''
	def remove_end_circle(self):
		if(self.reference == None):
			raise ListEmpty('List Empty')

		last_node = self.reference

	''' Remove Element at End '''
	def remove_pos_circle(self, pos):
		if(self.reference == None):
			raise ListEmpty('List Empty')

		if(pos > self.listSize()):
			raise ListSize('Position out of the list')

		if(first_node == first_node.next and pos == 0):
			self.reference = None

		count = 0
		temp_a = self.reference
		temp_b = temp_a.next
		while(pos < count):
			temp_a = temp_b
			temp_b = temp_a.next

		temp_a.next = temp_b.next