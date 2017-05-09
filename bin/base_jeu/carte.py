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
	
	
	def valeur_force(self,couleur_atout,couleur_plie):
		"""fonction qui détermine la force d'une carte dans une plie étant donné la couleur de la plie et l'atout"""
		valeur = self.rang.valeur_force()
		if self.couleur != couleur_plie :
			valeur = 0
		if self.couleur == couleur_atout:
			valeur = 9 + self.rang.valeur_force()
			if self.rang.nom == "9":
				valeur = 19
			elif self.rang.nom == "valet":
				valeur = 20
		return valeur
	
	def valeur_point(self,partie):
		"""fonction qui détermine le nombre de point que vaut une carte en sachant l'atout"""
		valeur = self.rang.valeur_point()
		if self.couleur == partie.atout:
			if self.rang.nom == "9":
				valeur = 14
			elif self.rang.nom == "valet":
				valeur = 20
		return valeur
	
	def __ide__(self):
		self.ide = self.rang.ide + 9*(self.couleur.ide-1)

	def __eq__(self, other):
	    return self.rang  == other.rang and self.couleur == other.couleur
	    
	def __ne__(self, other):
		return not(self.__eq__(other))

	def __repr__(self):
		return "{rang} de {couleur}".format(rang = self.rang.nom,couleur = self.couleur.nom)
