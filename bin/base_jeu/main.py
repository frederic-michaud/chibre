class main:
	def __init__(self,perm = None):
		if perm is not None:
			self.cartes = [carte(ide = i) for i in sorted(perm)]
		

	def joue(self, carte):
	    if carte in self.cartes :
			pass

	def __repr__(self):
		return "\n".join([carte.__repr__() for carte in self.cartes])
