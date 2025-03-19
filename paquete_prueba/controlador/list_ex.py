from modelo.node import Node

class list:
	def __init__(self):
		self.first_pte = None
		self.current_pte = None

	def empty(self):
		return self.first_pte is None

	def insert_list(self,age)
		try:
			new_node = Node()
			new_node.info = age
			new_node.next_pte = None
			
			if self.empty():
				first_pte = new_node
			
			else:
				new_node.next_pte = first_pte
				firts_pte = new_node
				current_pte = first_pte
			return True
		except Exception as e:
			raise Exception("ocurrio un error, no se puede ingresar nodo")
				
		