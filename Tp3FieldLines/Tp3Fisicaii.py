import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from matplotlib.widgets import Button
from matplotlib.widgets import Slider

#global variables
fig, (ax) = plt.subplots(ncols=1, figsize=(10, 5))
c_3v = "#00E8EC"
c_4v = "#00D3EC"
c_5v = "#00C5EC"
c_6v = "#00BEEC"
c_7v = "#00ACEC"
c_8v = "#00A4EC"
c_9v = "#007DEC"
c_10v = "#0039EC"
c_11v = "#1D00EC"
c_12v = "#5200EC"
c_13v = "#8400EC"
points_experiment1= np.array([ #5v 
        [-6, -7, c_5v],
        [-1, -6, c_5v],
        #[10, -6, c_5v],
        [3, 0, c_5v],
        [2, 4, c_5v],
        [-1, 6, c_5v],
        #3v [, ],
        [0, 1, c_3v],
        [1, 0, c_3v],
        [-1, 0, c_3v],
        [0, -1, c_3v],
        [0.65, 0.65, c_3v],
        [-0.65, -0.65, c_3v],
        #9v#[, ],
        [14, 0, c_9v],
        [16, 9, c_9v],
        [14, 4, c_9v],
        [15, -6, c_9v],
        [16, 10, c_9v],
        [16, -10, c_9v],
        #12v[, ],
        [21, 0.5, c_12v],
        [19, 0, c_12v],
        [22, 0, c_12v],
        [20, -1, c_12v],
        [20, 1, c_12v],
        [19.4, 0.6, c_12v],
        #10v[, ],
        [25, -9, c_10v],
        [16.8, 0, c_10v],
        [25, 9, c_10v],
        [22, 7, c_10v],
        [22, -7, c_10v],
        [7, -3, c_10v],
        #8v [, ],
        [11, 0, c_8v],
        [11.4, 3, c_8v],
        [11.4, -3, c_8v],
        [12, -9, c_8v],
        [12, 9, c_8v],
        [11.6, -5.8, c_8v]
])
points_experiment2=np.array([ 
#6v            ,c_],
[11.4	,-2.8,c_6v],
[11.4	,2.8,c_6v],
[11	    ,2,c_6v],
[11.2	,4.4,c_6v],
[11.2	,-4.4,c_6v],
[11	    ,0,c_6v],
#[3v,,c_],
[4.8    ,0,c_3v],
[4.6    ,-1.8,c_3v],
[4.6    ,1.8,c_3v],
[4.4    ,3,c_3v],
[4.4    ,-3,c_3v],
[4.2    ,5.4,c_3v],
#4v,,c_],
[6.8    ,0,c_4v],
[6.8    ,2,c_4v],
[6.8    ,-2,c_4v],
[6.8    ,-5,c_4v],
[6.8    ,5,c_4v],
[6.4    ,7.2,c_4v],
#[11v,,c_],
[18.6	,0,c_11v],
[19.8	,1.4,c_11v],
[20.8	,1,c_11v],
[20.8	,-1,c_11v],
[20.4	,1.2,c_11v],
[20.4	,-1.2,c_11v],
#7v,,c_],
[13.8	,0,c_7v],
[13.6	,-1,c_7v],
[9.8	,1.6,c_7v],
[9.8	,-1.6,c_7v],
[10	    ,-7,c_7v],
#9v,,c_],
[14.8	,0,c_9v],
[14.8	,1,c_9v],
[14.8	,-1,c_9v],
[15.2	,-2.8,c_9v],
[15.2	,2.8,c_9v],
[15.8	,5,c_9v]
])
points_experiment3 = np.array([
[17.2,0,c_13v],							
[17.6,1,c_13v],							
[17.6,-1,c_13v],							
[17.6,-4,c_13v],							
[17.6,4,c_13v],							
[17.6,5,c_13v],							
[13.4,0,c_11v],							
[14.1,1,c_11v],							
[13.1,-1,c_11v],							
[13.1,1,c_11v],							
[13.4,2.4,c_11v],							
[14.8,-2,c_11v],							
[10	 ,0,c_8v],						
[9.4 ,-1.6,c_8v],							
[9.8 ,-2.6,c_8v],							
[10	 ,-3,c_8v],						
[10	 ,3,c_8v],						
[10	 ,-4,c_8v],						
[5.4 ,0,c_5v],							
[5.4 ,-1,c_5v],							
[5.4 ,1,c_5v],							
[5.2 ,2,c_5v],							
[5.2 ,-2,c_5v],							
[5.2 ,-4,c_5v],							
[2.2 ,0,c_3v],							
[2.4 ,-1,c_3v],							
[2.4 ,1,c_3v],							
[2.4 ,2,c_3v],							
[2.4 ,-2,c_3v],							
[2.4 ,-3,c_3v],							
[7	 ,0,c_6v],						
[7	 ,-1,c_6v],						
[7	 ,1,c_6v],						
[6.8 ,2,c_6v],							
[7	 ,-2,c_6v],						
[7	 ,-4,c_6v]	
])
voltage_group = points_experiment1[:5]
sorted_indices = np.argsort(voltage_group[:, 1])
sorted_array = voltage_group[sorted_indices]
print(sorted_array)
sorted_array = sorted_array[::-1]
#x = np.sort(np.array(sorted_array[:, 0]))
#y = np.sort(np.array(sorted_array[:, 1]))
x = np.array(voltage_group[:, 0])
y = np.array(voltage_group[:, 1])
x = x.astype(float)
y = y.astype(float)
#x = x[::-1]
#ax.plot(x,y)

#print(x)
#print(y)


#print(sorted_array)
#ax.plot(x,y,"r--", linewidth=2.5)
def legend_first_experiment():
    plt.plot(100, 1, 'o', color=c_3v, label='3v')
    plt.plot(100, 1, 'o', color=c_5v, label='5v')
    plt.plot(100, 1, 'o', color=c_8v, label='8v')
    plt.plot(100, 1, 'o', color=c_9v, label='9v')
    plt.plot(100, 1, 'o', color=c_10v, label='10v')
    plt.plot(100, 1, 'o', color=c_12v, label='12v')
    plt.title('Primer experimento: Puntual-Puntual')
def legend_secnd_experiment():
    plt.plot(100, 1, 'o', color=c_3v, label='3v')
    plt.plot(100, 1, 'o', color=c_5v, label='5v')
    plt.plot(100, 1, 'o', color=c_6v, label='6v')
    plt.plot(100, 1, 'o', color=c_8v, label='8v')
    plt.plot(100, 1, 'o', color=c_11v, label='11v')
    plt.plot(100, 1, 'o', color=c_13v, label='13v')
    plt.title('Segundo experimento: Puntual-Plano')
def legend_thrd_experiment():
    plt.plot(100, 1, 'o', color=c_3v, label='3v')
    plt.plot(100, 1, 'o', color=c_4v, label='4v')
    plt.plot(100, 1, 'o', color=c_6v, label='6v')
    plt.plot(100, 1, 'o', color=c_7v, label='7v')
    plt.plot(100, 1, 'o', color=c_11v, label='11v')
    plt.plot(100, 1, 'o', color=c_13v, label='13v')
    plt.title('Tercer experimento: Plano-Plano')

def main():
    
    #ax.plot(x,y)
    
    for ([x,y,color]) in points_experiment3:
        ax.add_artist(Circle((float(x),float(y)), 0.3, color=color)) 
    ax.set_xlabel('$x$')
    ax.set_ylabel('$y$')
    ax.set_xlim(-15,30)
    ax.set_ylim(-14,14)
    print(x)
    #ax.plot(x,y)
    #legend_first_experiment()
    #legend_secnd_experiment()
    legend_thrd_experiment()
    plt.legend()
    plt.grid(color="black", alpha=0.5, linestyle="-", linewidth=0.5)
    
    plt.show()

if __name__ == '__main__':
    main()