# coding: utf8

from joueur import *
class equipe:
	"""classe qui définit ce qu'est une équipe. Chaque équipe a des points et 2 joueurs"""
	def __init__(self,Points = 0, J1 = joueur(), J2 = joueur(), Ide = 1):		
		"""constructeur de la classe equipe qui peut prendre point en argument"""
		self.points = Points
		self.joueurs = [J1,J2]
		self.ide = Ide


		
		

