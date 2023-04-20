import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from matplotlib.widgets import Button
from matplotlib.backend_bases import MouseEvent

class ElectricFieldSimulation:
    def __init__(self):
        self.charges = []
        self.nx, self.ny = 120, 120     
        self.Ex, self.Ey = np.zeros((self.ny, self.nx)), np.zeros((self.ny, self.nx))
        self.x = np.linspace(-2, 2, self.nx)
        self.y = np.linspace(-2, 2, self.ny)
        self.i,self.j, self.q = 0,0,0

        #self.fig, (self.ax, self.ax2) = plt.subplots(ncols=2, figsize=(10, 5))
        
    def load_charges(self):
        #self.charges.append((-1 ,(1.2,0)))
        #self.charges.append((1,(1.2,0)))
        self.charges.append((1 ,(-0.8,-0)))
        self.charges.append((-1,(0.8,0)))

    def E(self, q, r0, x, y):#Return the electric field vector E=(Ex,Ey) due to charge q at r0
        den = np.hypot(x-r0[0], y-r0[1])**3
        return q * (x - r0[0]) / den, q * (y - r0[1]) / den

    def compute_e_f(self):
        X, Y = np.meshgrid(self.x, self.y)
        for (q,(i,j)) in self.charges:
            ex, ey = self.E(q=q, r0 = (i,j), x=X, y=Y)
            self.Ex += ex
            self.Ey += ey
    
    def update_next_pos(self,x,y):
        self.i = x
        self.j = y
    
    def update_next_charge(self,q):
        self.q = q

    def add_charge(self):
        print(self.q,":",self.i,":",self.j)
        self.charges.append((self.q,(self.i,self.j)))