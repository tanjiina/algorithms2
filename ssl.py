class Node:
	def __init__ (self, value):
		self.value = value
		self.next = None

class SLL:
	def __init__ (self):
		self.head = None

	def addToFront(self, value):
		new_node = Node(value)
		new_node.next = self.head
		self.head = new_node
		return self

	def addToBack(self, value):
		if self.head == None:
			self.addToFront(value)
		else:
			runner = self.head
			while runner.next:
				runner = runner.next	
			runner.next = Node(value)
		return self
	# def addToBack(self,value):
	# 	newNode = Node(value)
	# 	if self.head == None:
	# 		addToFront(value)
	# 		return self
	# 	runne = self.head
	# 	while runner.next != None:
	# 		runner = runner.next
	# 	runner.next = Node(value)
	# 	return self


	def displaySLL(self):
		runner = self.head
		# display_string = ""
		# while runner:
		#     display_string += str(runner.value), "-->"
		#     runner = runner.next
		# print(display_string)
		while runner: 
			print(runner.value)
			runner = runner.next
		#while runner:
			# print(runner.value, "-->")
			# runner = runner.next
		# print (runner.value)
		# print(runner.next)
		# print(runner.next.value)
		# print(runner.next.next)
		# print(runner.next.next.value)
		# print(runner.next.next.next)
		return self
	
	def contains (self, value):
		runner = self.head
		while runner:
			if runner.value == value:
				print("Does it contain this " +int(value)+"?")
				return True
			runner = runner.next
		return False


sll1= SLL()
sll1.addToFront(9).addToFront(7).addToFront(5).addToBack(40)
sll1.displaySLL()
print(sll1.contains(9))
# print(sll1)
