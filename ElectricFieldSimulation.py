import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from matplotlib.widgets import Button

class ElectricFieldSimulation:
    def __init__(self):
        self.charges = []
        self.nx, self.ny = 120, 120
        self.Ex, self.Ey = np.zeros((self.ny, self.nx)), np.zeros((self.ny, self.nx))
        self.x = np.linspace(-2, 2, self.nx)
        self.y = np.linspace(-2, 2, self.ny)
        self.fig, (self.ax, self.ax2) = plt.subplots(ncols=2, figsize=(10, 5))
        
    def load_charges(self):
        self.charges.append((-1 ,(1.2,-0.6)))
        self.charges.append((1,(1.2,0.6)))
        self.charges.append((1 ,(-1.2,-0.6)))
        self.charges.append((-1,(-1.2,0.6)))

    def E(self, q, r0, x, y):		#Return the electric field vector E=(Ex,Ey) due to charge q at r0
        den = np.hypot(x-r0[0], y-r0[1])**3
        return q * (x - r0[0]) / den, q * (y - r0[1]) / den

    def compute_e_f(self):
        X, Y = np.meshgrid(self.x, self.y)
        for (q,(i,j)) in self.charges:
            ex, ey = self.E(q=q, r0 = (i,j), x=X, y=Y)
            self.Ex += ex
            self.Ey += ey
    
    def add_charge(self,x,y,q):
        self.charges.append((q,(x,y)))

    def on_button_clicked(self, event):
        self.add_charge(0,0,10)
        self.compute_e_f()
        self.ax.clear()
        self.plot_e_l()
        self.fig.canvas.draw()
        print("botonaso")

    def buttons_layout(self):
        self.fig.canvas.mpl_connect("button_press_event", self.on_button_clicked)

        button = Button(self.ax2, 'Add central charge', color='red', hovercolor='green')
        button.on_clicked(self.on_button_clicked)
        button.ax.set_position([0.65, 0.8, 0.15, 0.05])

    def plot_e_l(self):
        
        color = 2 * np.log(np.hypot(self.Ex, self.Ey))

        self.ax.streamplot(self.x, self.y, self.Ex, self.Ey, color=color, linewidth=0.6, cmap=plt.cm.inferno,
                        density=2, arrowstyle='->', arrowsize=1.1)

        charge_colors = {True: '#aa0000', False: '#0000aa'}

        for q, pos in self.charges:
            self.ax.add_artist(Circle(pos, 0.05, color=charge_colors[q>0]))

        self.ax.set_xlabel('$x$')
        self.ax.set_ylabel('$y$')
        self.ax.set_xlim(-2,2)
        self.ax.set_ylim(-2,2)
        self.ax.set_aspect('equal')

def main():
    
    simulation = ElectricFieldSimulation()
    simulation.load_charges()
    simulation.compute_e_f()
    simulation.buttons_layout()
    simulation.plot_e_l()
    plt.show()

if __name__ == '__main__':
    main()
