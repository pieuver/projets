
from personne import *;
import sys;
class Population:
	personnes = []
	nombre_infecte = 1
	confinement = 0
	def confinement(self):
		for i in range(1,nb_population):
			self.personnes[i].vitesse = Vec(0,0);
	def diffuse_vitesse(self):
		for i in range(0,nb_population):
			vit_aleatoire=Vec(0,0);
			if(i<int(sys.argv[1])):
				vit_aleatoire = vec_aleatoire(-1000+randint(-100,100),1000,-2000,2000)*0.043; 

		
			self.personnes[i].vitesse = vit_aleatoire;

	def collisionne(self):
		for i in range(0,nb_population):
			if self.personnes[i].infecte:
				for j in range(0,nb_population):
					if j!= i and not self.personnes[j].infecte and self.personnes[i].infecte:
						if(self.personnes[i].collision(self.personnes[j])): #Collision entre infecte et non infecte
							self.personnes[j].infecte = self.personnes[i].infecte
							self.nombre_infecte= self.nombre_infecte+1

	def __init__(self):
		for i in range(0,nb_population):
			position_aleatoire = vec_aleatoire(0,LARGEUR_FENETRE,0,HAUTEUR_FENETRE);
			vit_aleatoire = vec_aleatoire(-1000,1000,-2000,2000)*0.01; 
			self.personnes.append(Personne(position_aleatoire,vit_aleatoire));
		self.personnes[0].infecte = 1;
		self.personnes[0].vitesse= vec_aleatoire(-100,100,-200,200)


	def afficher(self,dt):

		self.collisionne();
		for i in range(0,nb_population):
			(self.personnes[i].afficher(dt))
		print("Il y a actuellement ",self.nombre_infecte, "infectes");
		if(self.nombre_infecte > MAX_INFECTES):
			print("Nous recommandons de confiner votre population")
			#self.confinement()
