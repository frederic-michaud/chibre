# coding: utf8
from rang import *
from couleur import *

class carte:

	def __init__(self,Rang = None,Couleur = None,Ide = None):
		if Rang is not None and Couleur is not None:		
			self.rang = rang(Nom = Rang)
			self.couleur = couleur(Nom = Couleur)
			self.__ide__()
		elif Ide is not None:	
			self.rang = rang(Ide = ((Ide-1) % 9) + 1 )
			self.couleur = couleur(Ide = 1+int((Ide-1)/9))
			self.__ide__()
		else :
			raise TypeError("cette carte n'est pas bien définie")
			
		
	def better(self, autre,jeu):
		pass
	
	
	def valeur_force(self,jeu):
		valeur = valeurs[self.rang.nom]
		if self.couleur == jeu.atout:
			if self.rang.nom == "9":
				valeur = 10
			elif self.rang.nom == "valet":
				valeur = 11
		return valeur
	
	def valeur_point(self,jeu):
		valeur = self.rang.valeur_point()
		if self.couleur == jeu.atout:
			if self.rang.nom == "9":
				valeur = 14
			elif self.rang.nom == "valet":
				valeur = 20
		return valeur
	
	def __ide__(self):
		self.ide = self.rang.ide + 9*(self.couleur.ide-1)

	def __eq__(self, other):
	    return self.rang  == other.rang and self.couleur == other.couleur

	def __repr__(self):
		return "{rang} de {couleur}".format(rang = self.rang.nom,couleur = self.couleur.nom)
