import numpy as np
import matplotlib.pyplot as plt

g = -9.81
ax = 0
ay = 0
vy = 0
t = 0
x = 0

h = float(input('Unesite visinu: '))
m = float(input('Unesite masu: '))
Cd = float(input('Unesite balisticki koeficijent: '))
S = float(input('Unesite povrsinu tela: '))
vx = float(input('Unesite pocetnu brzinu tela: '))

k = 0.6*Cd

dt = 1e-2

if Cd == 0:
	Vt = 0
else:
	Vt = np.sqrt((2*m*9.81)/(1.2*S*Cd))

H = np.array([h])
T = np.array([0])
R = np.array([0])
counter = 0

while H[counter] >= 0:

	counter += 1
	
	ax = - ((vx*k)*(vx*S)/m)
	vx += ax*dt
	x += vx*dt
	
	ay = g + ((vy*k)*(vy*S)/m)
	vy += ay*dt
	h += vy*dt
	
	t += dt
	
	H = np.append(H, h)
	T = np.append(T, t)
	R = np.append(R, x)

	
print('\n\n\n\n')
print('Vreme utroseno u letu: ' ,round(t, 4))
print('Predjena distanca: ' ,round(x, 4))
print('Maksimalna dostignuta brzina: ' ,round(np.sqrt(vx*vx + vy*vy), 4))

if Vt != 0:

	if round(np.sqrt(vx*vx + vy*vy), 0) == round(Vt, 0):
		print('Dostignuta je terminalna brzina.')
	
	else:
		print('Nije dostignuta terminalna brzina(',round(Vt, 4), ').')

plt.figure()
plt.plot(R, H)
plt.xlabel('Promena x ose [m]')
plt.ylabel('Promena visine [m]')
plt.title('Kretanje tela pri horizontalnom hicu')
plt.show()

input('....')	



