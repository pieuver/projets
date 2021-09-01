from random import *
from defs import *;
import matplotlib.pyplot as plt


##Classe Vec donne la position d'un point dans le plan
## Utile pour donner la position d'un individu au fil du temps
class Vec:
	x = 0.0 # position x
	y = 0.0 # position y
	def norme(self): # la norme euclidienne
		return (self.x**2 + self.y**2)**0.5;
	def norme_carre(self): # la norme euclidienne au carre
		return (self.x**2 + self.y**2)
	def print(self): # ecriture dans la console
		print('(',self.x, ',',self.y,')')

	# l'initialisation du Vec
	def __init__(self, X=0,Y=0):
		self.x = X
		self.y = Y
	#definition de l'addition entre Vec
	def __add__(self, other):
		resultat = Vec(self.x + other.x, self.y + other.y)
		return resultat;
	def __sub__(self,other):
		resultat = Vec(self.x - other.x, self.y - other.y)
		return resultat;
	#Definition de l'operateur +=
	def __IADD__(self, other):
		 self = self + other;	
	def __ISUB__(self, other):
		 self = self-other;	


	def __mul__(self, other):  ## pour le produit scalaire 
		resultat = self.x*other.x + self.y*other.y;
		return resultat;
	def __truediv__(self, nombre): ## division coordonnee par un scalaire
		return Vec(self.x/nombre,self.y/nombre);
	def __mul__(self, other): # multplication par un scalaire
		resultat= Vec(self.x*other,self.y*other);
		return resultat;

def vec_aleatoire(a,b,c,d):#genere un vec aleatoire a coordonnes entieres sur le carre [a,b]x[c,d]
	resultat=Vec();
	resultat.x = randint(a,b);
	resultat.y = randint(c,d);
	return resultat;
def distance(u,v): # distance entre deux points,deux vec
	w = u-v;
	return w.norme();
def distance_carre(u,v): #distance au carre
	w = u-v;
	return w.norme_carre();

