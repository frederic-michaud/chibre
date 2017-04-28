import numpy as np
class jeu:
	def __init__(self):
		donne = (np.random.permutation(36) +1).reshape(4,9)
		self.mains = [main(perm = i) for i in donne]

