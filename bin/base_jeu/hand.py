# coding: utf8

from carte import *
class hand:
	def __init__(self,perm = None):
		if perm is not None:
			self.cartes = [carte(Ide = i) for i in sorted(perm)]
		else:
			self.cartes = []
		

	def joue(self, carte):
	    if carte in self.cartes :
			pass

	def __repr__(self):
		if len(self.cartes)>0:
			return "\n".join([carte.__repr__() for carte in self.cartes])
		else:
			return "Il n'y a pas de carte dans ce jeu"

