# coding: utf8
class couleur:
	
	noms = 	["carreau","coeur","pique","trefle"]
	ids = range(1,5)
	noms_to_ids = dict(zip(noms,ids))
	ids_to_noms = dict(zip(ids,noms))
	
	def __init__(self,nom = None, ide = None):
		if nom is not None:		
			if nom in self.noms:
				self.nom = nom
			else:
				raise TypeError("Cette couleur n'existe pas")
		elif ide is not None:
			if ide in self.ids:
				self.nom = self.ids_to_noms[ide]
			else:
				raise TypeError("la couleur avec un numero {numero} n'existe pas".format(numero =ide))
		else:
			raise TypeError("Cette couleur n'est pas bien définie")

	def __eq__(self, other):
	    return (self.nom  == other.nom) 
