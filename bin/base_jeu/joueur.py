# coding: utf8


class joueur:
	"""classe qui définit ce qu'est un joueur"""
	def __init__(self, Equipe = 1):
		"""constructeur qui prend en argument une équipe"""
		self.equipe = Equipe
		self.hand = base_jeu.hand()

	
	def set_joue(self,jeu,cartes):
		"""fonction qui définit comment on joue chaque donne"""
		
			
	def compatibilise(self,joueur_gagnant,cartes):
		score = sum([carte.valeur_point(self) for carte in cartes])
		if joueur_gagnant in [1,3]:
			self.equipe_1_points +=score
		else:
			self.equipe_2_points +=score

		
	def joue_plie():
		"""fonction qui définit comment on joue chaque plie"""
		for i in range(4):
			joueur_joue()
			
			
