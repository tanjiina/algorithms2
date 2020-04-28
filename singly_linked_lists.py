class Node: 
	def __init__(self, value):
		self.value = value
		self.next = None

class SLL:
	def __init__(self):
		self.head = None

	def addToFront(self, value):
		new_node = Node(value)
		new_node.next = self.head
		self.head = new_node
		return self

2


	def addToBack(self, value):
		if self.head == None:
			self.addToFront(value)
		else:
			runner = self.head
			while runner.next:
				runner = runner.next	
			runner.next = Node(value)
		return self

	def displaySLL(self):
		runner = self.head
		# print(runner.value)
		# print(runner.next)
		# print(runner.next.value)
		# while runner != None: == while runner:
		# display_string = ""
		while runner: 
			# display_string += str(runner.value) , "-->"
			print(runner.value)
			runner = runner.next
		
		return self
	def contains (self, value):
		runner = self.head
		while runner:
			if runner.value == value:
				return True
			runner = runner.next
		return False
		

sll1 = SLL()

sll1.addToFront(9).addToFront(7).addToFront(5).addToFront(12).addToBack(13).contains(12)

# print(sll1)

sll1.displaySLL()