import matplotlib.pyplot as plt
import numpy as np

def func(z):
    return z**2


def plot_conformal_map(f, xmin, xmax, ymin, ymax, nb_grid, nb_points):
	#
	xv, yv = np.meshgrid(np.linspace(xmin, xmax, nb_grid), np.linspace(ymin, ymax, nb_points))
	xh, yh = np.meshgrid(np.linspace(xmin, xmax, nb_points), np.linspace(ymin, ymax, nb_grid))
	#xh, yh = xv, yv
	fig, (ax, ax2) = plt.subplots(ncols=2, figsize=(12, 6))
	xv = np.transpose(xv)
	yv = np.transpose(yv)

	zv = func(xv + 1j*yv)
	
	uv = np.real(zv)
	vv = np.imag(zv)

	zh = func(xh + 1j*yh)
	uh = np.real(zh)
	vh = np.imag(zh)

	#Plotear plano de las variables
	for i in range(len(yv)):
		ax.plot(xv[i], yv[i], 'b-', lw=1)
		ax.plot(xh[i], yh[i], 'r-', lw=1)
	
	#Plotear plano de la funcion
	for i in range(len(vv)):
		ax2.plot(uv[i], vv[i], 'b-', lw=1)
		ax2.plot(uh[i], vh[i], 'r-', lw=1)
	print(xv)
	print(xh)
	plt.show()

nb_grid = 9 #cantidad de curvas que van a  atravezar la grafica
nb_points = 30 #Resolucion


xmin, xmax, ymin, ymax = -10, 10, -10, 10

plot_conformal_map(func, xmin, xmax, ymin, ymax, nb_grid, nb_points)