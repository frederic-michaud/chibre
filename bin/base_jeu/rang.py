# coding: utf8
class rang:
	noms = 	["6","7","8","9","10","valet","dame","roi","as"]
	ids = range(1,10)
	noms_to_ids = dict(zip(noms,ids))
	ids_to_noms = dict(zip(ids,noms))

	def __init__(self,nom = None,ide = None):
		if nom is not None:		
			if nom in self.noms:
				self.nom = nom
			else:
				raise TypeError("Ce rang n'existe pas")
		elif ide is not None:
			self.nom = self.ids_to_noms[ide]
		else:
			raise TypeError("Ce rang n'est pas bien défini")
			
	
	def __eq__(self, other):
	    return (self.nom  == other.nom) 

		
		

