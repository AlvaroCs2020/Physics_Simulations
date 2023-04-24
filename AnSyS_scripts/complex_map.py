import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from matplotlib import font_manager as fm, rcParams
import numpy as np
import sys

def u(x,y):
	return x**2 - y**2
def v(x,y):
	return 2*x*y

fig, (ax, ax2) = plt.subplots(ncols=2, figsize=(12, 6))
resolution = int(sys.argv[1])
xmin, xmax, ymin, ymax = -1, 1, -1, 1
clearence = abs(xmin-xmax) * 0.1

xl = np.linspace(xmin, xmax, resolution)
yl = np.linspace(ymin, ymax, resolution)

#Plotear plano de las variables
#ax = fig.add_subplot(221)
for i in xl:
	for j in yl:
		ax.add_patch(Circle((i,j),0.01, color = '#aa0000'))
ax.set_xlim(xmin=xmin-clearence,xmax=xmax+clearence)
ax.set_ylim(ymin=ymin-clearence,ymax=ymax+clearence)
ax.set_xlabel('$X$')
ax.set_ylabel('$jY$')
ax.set_title('Plano de la variable $x + jy$')
ax.set_aspect('equal')
#ax2 = fig.add_subplot(222)
#ul = u(xl,yl)
#vl = v(xl,yl)
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
		ax2.add_patch(Circle((u(i,j),v(i,j)),0.01, color = '#aa0000'))

xlim_min = umin if xmin > umin else xmin
xlim_max = umax if xmax < umax else xmax
ylim_min = vmin if ymin > vmin else ymin
ylim_max = vmax if ymax < vmax else ymax

ax2.set_xlim(xmin=xlim_min - clearence, xmax=xlim_max + clearence)
ax2.set_ylim(ymin=ylim_min - clearence, ymax=ylim_max + clearence)
ax.set_xlim(xmin=xlim_min - clearence, xmax=xlim_max + clearence)
ax.set_ylim(ymin=ylim_min - clearence, ymax=ylim_max + clearence)

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