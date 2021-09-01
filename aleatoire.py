import matplotlib.pyplot as plt
from random import *

liste = []
for i in range(1,100):
	v = randint(-100,100);
	liste.append(v);

plt.plot(liste)
plt.show();
