import numpy as np
import matplotlib.pyplot as plt

g = -9.81
v = 0
t = 0

h = float(input('Unesite visinu: '))

dt = 1e-2

H = np.array([h])
T = np.array([0])
counter = 0

while H[counter] >= 0:

	counter += 1;
	
	v += g*dt
	h += v*dt
	t += dt
	
	H = np.append(H, h)
	T = np.append(T, t)
	
	
print('\n\n\n\n')
print('Vreme utroseno u letu: ' ,round(t, 4))
print('Maksimalna dostignuta brzina: ' ,-round(v, 4))	


plt.figure()
plt.plot(T, H)
plt.xlabel('Promena vremena [s]')
plt.ylabel('Promena visine [m]')
plt.title('Kretanje tela u slobodnom padu bez dejstva otpora vazduha')
plt.show()

input('....')	



