# coding: utf8
class rang:
	noms = 	["6","7","8","9","10","valet","dame","roi","as"]
	points = [0,0,0,0,10,2,3,4,11]
	forces = [1,2,3,4,5,6,7,8,9]
	atouts = [1,1,1,5,2,8,2,3,4]
	
	ids = range(1,10)
	noms_to_ids = dict(zip(noms,ids))
	ids_to_noms = dict(zip(ids,noms))
	ids_to_points = dict(zip(ids,points))
	ids_to_forces = dict(zip(ids,forces))
	ids_to_atouts = dict(zip(ids,atouts))

	def __init__(self,Nom = None,Ide = None):
		pass
		if Nom is not None:		
			if Nom in self.noms:
				self.nom = Nom
				self.__ide__()
			else:
				raise TypeError("Ce rang n'existe pas")
		elif Ide is not None:
			self.nom = self.ids_to_noms[Ide]
			self.ide = Ide
		else:
			raise TypeError("Ce rang n'est pas bien défini")
			
	
	def __eq__(self, other):
	    return (self.nom  == other.nom) 
	
	def __ide__(self):
		self.ide = self.noms_to_ids[self.nom]
		
	def valeur_point(self):
		return self.ids_to_points[self.ide]
		
	def valeur_force(self):
		return self.ids_to_forces[self.ide]
		
	def valeur_atout(self):
		return self.ids_to_atouts[self.ide]

		
		

