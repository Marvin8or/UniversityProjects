# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 05:58:26 2020

@author: Gabriel
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import matplotlib.animation as animation
from Main import D,ufield,vfield,nx,ny,nt,x,y,t1,dx,dy,dt
import cProfile
from numba import njit,prange
import time as tim1

up = np.ones((nt,nx,ny))
            

@njit(parallel=True)
def iteration_by_t_njit(up,t1,x,y,ufield,vfield,dt,dx,dy):
    up[0,np.round(0.4*nx):np.round(0.42*nx),np.round(0.4*ny):np.round(0.42*ny)] = 3
    for it in prange(len(t1)-1):
        for i in range(1,len(x)-1):
            for j in range(1,len(y)-1):
                if ufield[it,i,j] and vfield[it,i,j] >= 0:
                    up[it+1,i,j] = up[it,i,j] \
                                   + D * dt/(dx**2) * (up[it,i+1,j] - 2*up[it,i,j] + up[it,i-1,j]) \
                                   + D * dt/(dy**2) * (up[it,i,j+1] - 2*up[it,i,j] + up[it,i,j-1]) \
                                   - 50 *ufield[it,i,j] * dt/dx * (up[it,i,j] - up[it,i,j-1]) \
                                   - 50 *vfield[it,i,j] * dt/dy * (up[it,i,j] - up[it,i-1,j])
                else:
                    up[it+1,i,j] = up[it,i,j] \
                                   + D * dt/(dx**2) * (up[it,i+1,j] - 2*up[it,i,j] + up[it,i-1,j]) \
                                   + D * dt/(dy**2) * (up[it,i,j+1] - 2*up[it,i,j] + up[it,i,j-1]) \
                                   - 50 *ufield[it,i,j] * dt/dx * (up[it,i+1,j] - up[it,i,j]) \
                                   - 50 *vfield[it,i,j] * dt/dy * (up[it,i,j+1] - up[it,i,j])
                              
        up[it+1,0,:] =up[it+1,1,:]
        up[it+1,-1,:] =up[it+1,-2,:]  
        up[it+1,:,0] =up[it+1,:,1]
        up[it+1,:,-1] =up[it+1,:,-2] 
    
    return up

def iteration_by_t(up,t1,x,y,ufield,vfield,dt,dx,dy):
    up[0,int(np.round(0.4*nx)):int(np.round(0.42*nx)),int(np.round(0.4*ny)):int(np.round(0.42*ny))] = 3
    for it in range(len(t1)-1):
        for i in range(1,len(x)-1):
            for j in range(1,len(y)-1):
                if ufield[it,i,j] and vfield[it,i,j] >= 0:
                    up[it+1,i,j] = up[it,i,j] \
                                   + D * dt/(dx**2) * (up[it,i+1,j] - 2*up[it,i,j] + up[it,i-1,j]) \
                                   + D * dt/(dy**2) * (up[it,i,j+1] - 2*up[it,i,j] + up[it,i,j-1]) \
                                   - 50 *ufield[it,i,j] * dt/dx * (up[it,i,j] - up[it,i,j-1]) \
                                   - 50 *vfield[it,i,j] * dt/dy * (up[it,i,j] - up[it,i-1,j])
                else:
                    up[it+1,i,j] = up[it,i,j] \
                                   + D * dt/(dx**2) * (up[it,i+1,j] - 2*up[it,i,j] + up[it,i-1,j]) \
                                   + D * dt/(dy**2) * (up[it,i,j+1] - 2*up[it,i,j] + up[it,i,j-1]) \
                                   - 50 *ufield[it,i,j] * dt/dx * (up[it,i+1,j] - up[it,i,j]) \
                                   - 50 *vfield[it,i,j] * dt/dy * (up[it,i,j+1] - up[it,i,j])
                              
        up[it+1,0,:] =up[it+1,1,:]
        up[it+1,-1,:] =up[it+1,-2,:]  
        up[it+1,:,0] =up[it+1,:,1]
        up[it+1,:,-1] =up[it+1,:,-2] 
    
    return up
          
t11 = tim1.time()
up = iteration_by_t_njit(up,t1,x,y,ufield,vfield,dt,dx,dy)
time_e = tim1.time() - t11
print(time_e)
cP = cProfile.run('iteration_by_t_njit(up,t1,x,y,ufield,vfield,dt,dx,dy)')
# cProfile.run('iteration_by_t(up,t1,x,y,ufield,vfield,dt,dx,dy)')




X,Y = np.meshgrid(x,y) 
fig = plt.figure(figsize=(10,10))
ax = plt.subplot(1,1,1)
cont = ax.contourf(X,Y,up[0,:,:],levels = 100,cmap = cm.jet)
fig.colorbar(cont)

def update(nt):
    ax.cla()
    ax.set_xlabel('$x$')
    ax.set_ylabel('$y$');
    ax.set_title('t=%f' %(t1[nt]))
    ax.contourf(X,Y,up[nt,:,:],levels = 100,cmap = cm.jet)
    return ax

# # Writer = animation.writers['ffmpeg']
# # writer = Writer(fps=3,metadata=dict(artist='Me'),bitrate=-1)
       
ani = animation.FuncAnimation(fig, update,
                              interval=10,frames=len(up),
                              repeat=False)
# # ani.save('konvekcija_slučaj2.mp4',writer)
plt.show()
        