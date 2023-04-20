import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from matplotlib.widgets import Button
from matplotlib.widgets import Slider
from ElectricFieldSimulation import ElectricFieldSimulation 

#global variables
simulation = ElectricFieldSimulation()
fig, (ax, ax2) = plt.subplots(ncols=2, figsize=(10, 5))
ax_slider = fig.add_axes([0.57, 0.4, 0.35, 0.015])
charge_slider = Slider( ax=ax_slider,
                        label="Next q",
                        valmin=-10,
                        valmax=10,
                        valinit=0,
                        valstep=0.1,
                        orientation="horizontal"
                    )

def add_charge_button(event):
    simulation.add_charge()
    simulation.compute_e_f()
    ax.clear()
    plot_set_up()
    fig.canvas.draw()

def plot_set_up():
    ax.set_xlabel('$x$')
    ax.set_ylabel('$y$')
    ax.set_xlim(-2,2)
    ax.set_ylim(-2,2)
    ax.set_aspect('equal')
    color = 2 * np.log(np.hypot(simulation.Ex, simulation.Ey))

    ax.streamplot(simulation.x, simulation.y, simulation.Ex, simulation.Ey, color=color, linewidth=0.6, cmap=plt.cm.inferno,
                    density=2, arrowstyle='->', arrowsize=1.1)

    charge_colors = {True: '#aa0000', False: '#0000aa'}
    for q, pos in simulation.charges:
        ax.add_artist(Circle(pos, 0.05, color=charge_colors[q>0]))

def onclick(event): #Me recontra aseguro que el click sea en 
    if isinstance(event.xdata, (int, float, complex)):
        if(500 > event.x ):
            #print("click in")
            x , y = event.xdata, event.ydata
            simulation.update_next_pos(x,y)


# Define the function to update the plot based on the slider value
def update_charge(event):
    simulation.update_next_charge(charge_slider.val)


def main():
    fig.canvas.mpl_connect('button_press_event', onclick)

    button = Button(ax2, 'Add central charge', color='red', hovercolor='green')
    button.ax.set_position([0.65, 0.8, 0.15, 0.05])
    button.on_clicked(add_charge_button)
    charge_slider.on_changed(update_charge)

    simulation.load_charges()
    simulation.compute_e_f()

    plot_set_up()

    plt.show()

if __name__ == '__main__':
    main()