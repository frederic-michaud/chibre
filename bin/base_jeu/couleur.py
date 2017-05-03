# coding: utf8
class couleur:
	
	noms = 	["carreau","coeur","pique","trefle"]
	ids = range(1,5)
	noms_to_ids = dict(zip(noms,ids))
	ids_to_noms = dict(zip(ids,noms))
	
	def __init__(self,Nom = None, Ide = None):
		if Nom is not None:		
			if Nom in self.noms:
				self.nom = Nom
				self.__ide__()
			else:
				raise TypeError("Cette couleur n'existe pas")
		elif Ide is not None:
			if Ide in self.ids:
				self.nom = self.ids_to_noms[Ide]
				self.ide = Ide
			else:
				raise TypeError("la couleur avec un numero {numero} n'existe pas".format(numero =ide))
		else:
			raise TypeError("Cette couleur n'est pas bien définie")

	def __eq__(self, other):
		return (self.nom  == other.nom) 

	
	def __ide__(self):
		self.ide = self.noms_to_ids[self.nom]
