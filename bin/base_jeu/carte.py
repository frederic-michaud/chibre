# coding: utf8
from rang import *
from couleur import *
class carte:

	def __init__(self,Rang = None,Couleur = None,ide = None):
		if Rang is not None and couleur is not None:		
			self.rang = Rang
			self.couleur = Couleur
		if ide is not None:
			self.rang = rang(ide = ((ide-1) % 9) + 1 )
			self.couleur = couleur(ide = 1+int((ide-1)/9))
		else :
			raise TypeError("cette carte n'est pas bien définie")
			
		
	def better(self, autre,jeu):
		pass
	
	
	def valeur(self,jeu):
		valeur = valeurs[self.rang.nom]
		if self.couleur == jeu.atout:
			if self.rang.nom == "9":
				valeur = 10
			elif self.rang.nom == "valet":
				valeur = 11
		return valeur
	
	def id(self):
		valeur = valeurs[self.rang.nom]
		return valeur

	def __eq__(self, other):
	    return self.rang  == other.rang and self.couleur == other.couleur

	def __repr__(self):
		return "{rang} de {couleur}".format(rang = self.rang.nom,couleur = self.couleur.nom)
