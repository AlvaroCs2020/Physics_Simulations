import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from matplotlib import font_manager as fm, rcParams
import numpy as np
import sys
import math

#def u(x,y):
#	return x**2 - y**2
#def v(x,y):
#	return 2*x*y
def u(x,y):
	return math.e**(3*x)*math.cos(3*y) + 2
def v(x,y):
	return math.e**(3*x)*math.sin(3*y)
def order_of_magnitude(num):
    if num == 0:
        return 0
    else:
        return int(math.floor(math.log10(abs(num))))	
fig, (ax, ax2) = plt.subplots(ncols=2, figsize=(12, 6))
resolution = int(sys.argv[1])
xmin, xmax, ymin, ymax = 2, 5, math.pi/4, math.pi/2
#xmin, xmax, ymin, ymax = -1, 1, -1, 1

clearence = abs(xmin-xmax) * 0.1

xl = np.linspace(xmin, xmax, resolution)
yl = np.linspace(ymin, ymax, resolution)

#Plotear plano de las variables
for i in xl:
	for j in yl:
		ax.add_patch(Circle((i,j),0.01, color = '#aa0000'))
ax.set_xlim(xmin=xmin-clearence,xmax=xmax+clearence)
ax.set_ylim(ymin=ymin-clearence,ymax=ymax+clearence)
ax.set_xlabel('$X$')
ax.set_ylabel('$jY$')
ax.set_title('Plano de la variable $x + jy$')
ax.set_aspect('equal')

umin = u(xmin,ymin)
umax = u(xmax,ymax)
vmin = v(xmin,ymin)
vmax = v(xmax,ymax)

for i in xl:
	for j in yl:
		umin = u(i,j) if u(i,j) < umin else umin
		umax = u(i,j) if umax < u(i,j) else umax
		vmin = v(i,j) if v(i,j) < vmin else vmin
		vmax = v(i,j) if vmax < v(i,j) else vmax
		try:
			print(order_of_magnitude(v(i,j)), " : ", v(i,j))
		except:
			pass
		magnitude = order_of_magnitude(v(i,j)) if order_of_magnitude(u(i,j)) < order_of_magnitude(v(i,j)) else order_of_magnitude(u(i,j))
		ax2.add_patch(Circle((u(i,j),v(i,j)),0.05 * 10**(magnitude), color = '#aa0000'))

ax2.set_xlim(xmin=umin-clearence,xmax=umax+clearence)
ax2.set_ylim(ymin=vmin-clearence,ymax=vmax+clearence)

ax2.set_xlabel('$U$')
ax2.set_ylabel('$jV$')
ax2.set_title('Plano de la funcion $u + jv$')
ax2.set_aspect('equal')
ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')
ax2.axhline(y=0, color='k')
ax2.axvline(x=0, color='k')
#plt.title('Mapeo de una funcion de variable compleja')
plt.show()