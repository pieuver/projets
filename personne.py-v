from particule import *;

class Personne(Particule):
	infecte = False

	def afficher(self,dt):
		self.update(dt)
		set_color(Color.BLUE)
		if(self.infecte):
			set_fill_color(Color.RED)
		else:
			set_fill_color(Color.BLUE)
		fill_circle(self.position.x, self.position.y, self.rayon)