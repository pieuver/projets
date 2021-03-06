from vec import *;
from graphics import *;
from easygraphics import * # on importe des bibliotheques

class Particule(object):
	"""docstring for ClassName"""
	rayon = 10.0
	# Initialisation au vecteur nul
	position = Vec()
	vitesse=  Vec()
	acceleration = Vec()
	masse = 1.0
	F= Vec();
	gravite= 0;
	def __init__(self, pos_init=Vec(), vit_init=Vec(), acc_init=Vec(),rayon=100):
		self.position = pos_init;
		self.vitesse=vit_init;
		self.acceleration=acc_init;
	def print(self):
		print("Masse :", self.masse);
		print("Position :")
		self.position.print();
		print("Vitesse :")
		self.vitesse.print();
		print("acceleration :")
		self.acceleration.print()

	def add_force(self, f):
		self.F+=f;
	def add_acceleration(self,da):
		self.acceleration+=da;
	def add_vitesse(self, dv):
		self.vitesse+=dv;
	def add_position(self, dp):
		self.position+=dp;

	def update(self, dt):
		F=Vec();
		if(self.gravite):
			v = Vec(0,g*self.masse);
			self.add_force(v);
		self.acceleration=self.F*(1.0/self.masse);
		self.vitesse+=self.acceleration*dt;
		self.position+=self.vitesse*dt;
		if(self.position.x > LIMITE_SIMULATION_X):
			self.position.x=0;
		if(self.position.x < 0):
			self.position.x=LIMITE_SIMULATION_X;
		if(self.position.y > LIMITE_SIMULATION_Y):
			self.position.y=0;
		if(self.position.y < 0):
			self.position.y=LIMITE_SIMULATION_Y;
	#Les accesseurs
	def getRayon():
		return self.rayon;
	def getPosition():
		return self.position;
	def getVitesse():
		return self.vitesse;
	def getAcceleration():
		return self.acceleration;
	def getMasse():
		return self.masse;
	def getSommeForces():
		return self.F;
	def getGravite():
		return self.gravite;
	# Les mutateurs
	def setRayon(self,r):
		self.rayon=r;
	def setPosition(self,p):
		self.position =p;
	def setVitesse(self,v):
		self.vitesse=v;
	def setAcceleration(self, a):
		self.acceleration=a;
	def setMasse(self, m):
		self.masse=m;
	def setSommeForces(self,somme_forces):
		self.F=somme_forces;
	def setGravite(self,Gravite):
		self.gravite=Gravite

	def afficher(self, win):
		c = Circle(Point(self.position.x,self.position.y ), self.rayon);
		c.draw(win);
	def collision(self, other):
		return distance_carre(self.position, other.position) <= self.rayon**2+other.rayon**2;

