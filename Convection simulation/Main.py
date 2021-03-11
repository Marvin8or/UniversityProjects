# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 11:56:49 2020

@author: Gabriel
"""
import numpy as np
import scipy.interpolate as interp
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import cm 
from numba import njit
import cProfile
import time as tim1
data = np.load('velocity.npz')
def popuni(data):
    
    vx = data['vx']
    vy = data['vy']
    xd = data['x']
    yd = data['y']
    time = data['time']
    
    return vx,vy,xd,yd,time


vx,vy,xd,yd,time = popuni(data)


def interpolator(time,xd,yd,vx,vy):
    Vx = interp.RegularGridInterpolator((time,xd,yd), vx)
    Vy = interp.RegularGridInterpolator((time,xd,yd), vy)
    return Vx,Vy


Vx,Vy = interpolator(time, xd, yd, vx, vy)


nx = 100
ny = 100
nt = 3000
D = 0.3 #0.018 
Tmin = min(time)
Tmax = max(time)
x = xd[:nx]
y = yd[:ny]



x_min = min(x)
x_max = max(x)
y_min = min(y)
y_max = max(y)
t1 = np.linspace(Tmin,Tmax,nt)


dt = 0.001
dx = np.round((x[1] - x[0]),2)
dy = np.round((y[1] - y[0]),2)
X = len(x) * len(y) * len(t1)

xy = len(x) * len(y)
planes = np.linspace(xy,X,nt,endpoint=True)


@njit
def points_planes(X):
    points = np.ones((X,3))
    i = 0
    for red in range(X):
        if red < planes[i]:
            points[red,0] = t1[i]
        else:
            i = i + 1
            points[red,0] = t1[i]
    return points

t11 = tim1.time()
points = points_planes(X)
time_e = tim1.time() - t11
print(time_e)
# cProfile.run('points_planes(X)')

@njit
def shuffle(points):
    iy = 0
    ix = 0
    for red in range(X):
        if ix<len(x):
            if iy<len(y):
                points[red,1] = x[ix]
                points[red,2] = y[iy]
                iy+=1
            else:
                iy=0
                if ix == 50:
                    ix = 0
                    points[red,1] = x[ix]
                    points[red,2] = y[iy]
                else:
                    ix+=1
                    points[red,1] = x[ix]
                    points[red,2] = y[iy]
                iy+=1
    return points

# cProfile.run('shuffle(points)')

t11 = tim1.time()
points = shuffle(points)     
time_e = tim1.time() - t11
print(time_e)

values_vx = Vx(points)
values_vy = Vy(points)

ufield = values_vx.reshape(nt,nx,ny)*10
vfield = values_vy.reshape(nt,nx,ny)*10



"""
----- Provjera CFL broja -----
"""
@njit
def CLF_test(values_vx,values_vy,dx,dy):
    for i in range(len(values_vx)):
        cflx = values_vx[i]*dt/dx
        cfly = values_vy[i]*dt/dy
        if cflx > 1:
            raise ValueError('cfl on x axis is too big')
        elif cfly > 1:
            raise ValueError('cfl on y axis is too big')
            
    print('cfl numbers of x and y axes are in range')
    
    
    cflD = dx**2 * dy**2/(2*dt*(dx**2 + dy**2))
    cfldt = dx**2 * dy**2/(2*D*(dx**2 + dy**2))
    if D <= cflD:
        print('Diffusion cfl is in range')
    else:
        raise ValueError('Diffusion cfl too big')
    if dt <= cfldt:
        print('Timestep cfl is in range')
    else:
        raise ValueError('timestep cfl too big')
        
CLF_test(values_vx, values_vy, dx, dy)
# cProfile.run('CLF_test(values_vx, values_vy, dx, dy)')
def update_quiver(j,ax, fig):
    scale = 10000
    u = scale * ufield[j]
    v = scale * vfield[j]
    ax.set_title('t=%f' %(t1[j]))
    Q.set_UVC(u,v)
    return Q


def init_quiver():
    global Q
    u = ufield[0]   
    v = vfield[0]
    Q = ax.quiver(u, v, scale = 10000,scale_units = 'width')
    ax.quiverkey(Q, 20,20, 1, r'$0.2 \frac{m}{s}$', labelpos='N',
                          coordinates='figure')
    return Q

# Writer = animation.writers['ffmpeg']
# writer = Writer(fps=3,metadata=dict(artist='Me'),bitrate=-1)


# fig, ax = plt.subplots(figsize = (10,10))
# ax.xaxis.set_ticks([])
# ax.yaxis.set_ticks([])
# ax.set_aspect('equal')
# ani = animation.FuncAnimation(fig,update_quiver,
                              # frames = nt,
                              # init_func = init_quiver,
                              # interval = 400,
                              # fargs = (ax,fig),
                              # repeat = False)
# ani.save('quiver.mp4',writer)

# plt.grid()
# plt.show()
    
