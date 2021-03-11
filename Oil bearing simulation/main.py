# -*- coding: utf-8 -*-
"""
Created on Sun May 26 02:48:19 2019

@author:
"""

import numpy as np
import matplotlib.pyplot as plt
from Steady import function_steady6 
from Dynamic_1 import function_d14segment 
from Dynamic_2 import function_d24segment 

beta = 5*np.pi/180
len1 = 0.5
ps = 10**(-10)
lod = 1
omega = 1

"""Lund: L/D =1, groove angle = 20 """
e = np.array([0.103, 0.15, 0.224, 0.352, 0.46, 0.559, 0.65, 0.734, 0.773, 0.793, 0.811, 0.883])
"""ATT = np.array([75.99, 70.58, 63.54, 55.41, 49.27, 44.33, 39.72, 35.16, 32.82, 31.62, 30.39, 25.02])
SOM = np.array([1.47, 0.991, 0.635, 0.358, 0.235, 0.159, 0.108, 0.071, 0.056, 0.05, 0.044, 0.024])
Kxx = np.array([1.53, 1.56, 1.62, 1.95, 2.19, 2.73, 3.45, 4.49, 5.23, 5.69, 6.22, 9.77,])
Kxy = np.array([10.14, 7.29, 5.33, 3.94, 3.57, 3.36, 3.34, 3.5, 3.65, 3.75, 3.88, 4.69])
Kyx = np.array([-3.01, -2.16, -1.57, -0.97, -0.8, -0.48, -0.23, 0.03, 0.18, 0.26, 0.35, 0.83])
Kyy = np.array([1.5, 1.52, 1.56, 1.48, 1.55, 1.48, 1.44, 1.44, 1.45, 1.45, 1.46, 1.53])
Cxx = np.array([20.34, 14.66, 10.8, 8.02, 7.36, 6.94, 6.89, 7.15, 7.42, 7.6, 7.81, 9.17])
Cxy = np.array([1.53, 1.58, 1.7, 1.63, 1.89, 1.78, 1.72, 1.7, 1.71, 1.71, 1.72, 1.78])
Cyx = np.array([1.53, 1.58, 1.7, 1.63, 1.89, 1.78, 1.72, 1.7, 1.71, 1.71, 1.72, 1.78])
Cyy = np.array([6.15, 4.49, 3.41, 2.37, 2.19, 1.74, 1.43, 1.2, 1.1, 1.06, 1.01, 0.83])"""

""" mesh"""
m = 61 
n = 21

""" kreiranje niza s nulama """
SN = np.zeros(np.size(e)) 
phi_d = np.zeros(np.size(e))
phi_r = np.zeros(np.size(e)) 
K_xx = np.zeros(np.size(e)) 
K_xy = np.zeros(np.size(e)) 
K_yx = np.zeros(np.size(e)) 
K_yy = np.zeros(np.size(e)) 
C_xx = np.zeros(np.size(e)) 
C_xy = np.zeros(np.size(e)) 
C_yx = np.zeros(np.size(e)) 
C_yy = np.zeros(np.size(e)) 

""" main loop """
for i in range(np.size(e)):
    epsi = e[i]

    kut,hpot1,theta2,theta1,theta4,theta3,sirin,hpot,theta,p,Fx, Fy, W, phi_r[i] = function_steady6(m, n, epsi, lod, beta, len1, ps)
    print('hpot1 = %.4f' %hpot1[i])
    print('hpot = %.4f' %hpot[i])
    print('theta = %.4f' %theta[i])
    print('att = %.4f' %phi_r[i])
    WXD1,WZD1 = function_d14segment(m, n, epsi, lod, beta, len1, ps, omega, p, phi_r[i])
    WXD2,WZD2 = function_d24segment(m, n, epsi, lod, beta, len1, ps, omega, p, phi_r[i])
    """figure"""
    """surf(p)"""
    SN[i] = 1/(6*Fx)
    phi_d[i] = phi_r[i]*180/np.pi
    K_xx[i] = -WXD1.real/Fx
    K_yx[i] = -WZD1.real/Fx
    K_xy[i] = -WXD2.real/Fx
    K_yy[i] = -WZD2.real/Fx
    C_xx[i] = -WXD1.imag/Fx/omega
    C_yx[i] = -WZD1.imag/Fx/omega
    C_xy[i] = -WXD2.imag/Fx/omega
    C_yy[i] = -WZD2.imag/Fx/omega
    
    print('eccentricity ratio = %.3f' %epsi)
    print(' ')
    print('attitude angle = %.4f' %phi_d[i])
    print(' ')
    print('sommerfeled NO. = %.4f' %SN[i])
    print(' ')
    print('Fx = ', Fx)
    print('Fy = ', Fy)
    print(' ')
    print('K_xx = %.4f  ;  K_xy = %.4f' %(K_xx[i],K_xy[i]))
    print('K_yx = %.4f  ;  K_yy =  %.4f' %(K_yx[i],K_yy[i]))
    print('C_xx = %.4f  ;  C_xy = %.4f' %(C_xx[i],C_xy[i]))
    print('C_yx = %.4f  ;  C_yy = %.4f' %(C_yx[i],C_yy[i]))
    print('******************************************')

    
"""plot results"""

"""plot Sommerfeled No. vs. eccentricity ratio"""
plt.figure()
plt.plot(e, SN, 'b-', label='this work') #vratiti na SN
"""plt.plot(e,SOM, 'b^', label='Ref')"""
plt.xlim((0,1))
plt.ylim((0,2))
plt.title('Sommerfeled No. vs. eccentricity ratio')
plt.xlabel('eccentricity ratio')
plt.ylabel('Sommerfeled NO.')
plt.legend(loc='upper right')
plt.grid()
plt.show()

"""plot attitude angle vs. eccentricity ratio"""
plt.figure()
plt.plot(e,phi_d,'b-', label='this work') #promijeniti na phi_d
"""plt.plot(e,ATT,'b^', label='Ref')"""
plt.xlim((0,1))
plt.ylim((20,90))
plt.title('attitude angle vs. eccentricity ratio')
plt.xlabel('eccentricity ratio')
plt.ylabel('attitude angle (deg)')
plt.legend(loc='upper right')
plt.grid()

""" plot stiffness vs. Sommerfeled No."""
plt.figure()
plt.plot(SN,K_xx,'r', label='K_xx') #vratiti SOM na SM
plt.plot(SN,K_xy,'b', label='K_xy')
plt.plot(SN,K_yx,'g', label='K_yx')
plt.plot(SN,-K_yx,'g:', label='- K_yx')
plt.plot(SN,K_yy,'k', label='K_yy')
"""plt.plot(SN,Kxx,'ro')#dodati LABEL i promijeniti na K_xx
plt.plot(SN,Kxy,'b^')
plt.plot(SN,Kyx,'gd')
plt.plot(SN,-Kyx,'gd')
plt.plot(SN,Kyy,'ks')"""
plt.xscale(value='log')
plt.yscale(value='log')
plt.xlim((0.0005,100))
plt.ylim((0.2,100))
plt.title('Stiffness coefficients vs. Sommerfeled No.')
plt.xlabel('SN')
plt.ylabel('stiffness coefficients')
plt.legend(loc='upper left')
 
""" plot damping vs. Sommerfeled No."""
plt.figure()
plt.plot(SN,C_xx,'r', label='C_xx')
plt.plot(SN,C_xy,'b', label='C_xy')
plt.plot(SN,C_yx,'g', label='C_yx')
plt.plot(SN,-C_yx,'g:', label='- C_xx')
plt.plot(SN,C_yy,'k', label='C_yy')
"""plt.plot(SN,Cxx,'ro', label=' ')#dodati LABEL 
plt.plot(SN,Cxy,'b^', label=' ')
plt.plot(SN,Cyx,'gd', label=' ')
plt.plot(SN,-Cyx,'gd', label=' ')
plt.plot(SN,Cyy,'ks', label=' ')"""
plt.xscale(value='log')
plt.yscale(value='log')
plt.xlim((0.0005,100))
plt.ylim((0.2,100))
plt.title('Damping coefficients vs. Sommerfeled No.')
plt.xlabel('SN')
plt.ylabel('damping coefficients')
plt.legend(loc='upper left')

"""plot stiffness coefficients vs. eccentricity ratio"""
plt.figure()
ax = plt.subplot(2,1,1)
box = ax.get_position()
plt.plot(e,K_xx,'r', label='K_xx')
plt.plot(e,K_xy,'b', label='K_xy')
plt.plot(e,K_yx,'g', label='K_yx')
plt.plot(e,K_yy,'k', label='K_yy')
"""plt.plot(e,Kxx,'ro', label=' ')
plt.plot(e,Kxy,'b^', label=' ')
plt.plot(e,Kyx,'gd', label=' ')
plt.plot(e,Kyy,'ks', label=' ')"""
plt.xlim((0,1))
plt.ylim((-10,25))
plt.title('Stiffness coefficients vs. eccentricity ratio')
plt.xlabel('eccentricity ratio')
plt.ylabel('stiffness coefficients')
ax.set_position([box.x0, box.y0, box.width*0.8, box.height*0.85])
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid()
"""plot damping coefficients vs. eccentricity ratio"""
ax1 = plt.subplot(2,1,2)
box1 = ax1.get_position()
plt.plot(e,C_xx,'r', label='K_xx')
plt.plot(e,C_xy,'b', label='K_xy')
plt.plot(e,C_yx,'g', label='K_yx')
plt.plot(e,C_yy,'k', label='K_yy')
"""plt.plot(e,Cxx,'ro', label=' ')
plt.plot(e,Cxy,'b^', label=' ')
plt.plot(e,Cyx,'gd', label=' ')
plt.plot(e,Cyy,'ks', label=' ')"""
plt.xlim((0,1))
plt.ylim((0,45))
plt.title('Damping coefficients vs. eccentricity ratio')
plt.xlabel('eccentricity ratio')
plt.ylabel('damping coefficients')
ax1.set_position([box1.x0, box1.y0, box1.width*0.8, box1.height*0.85])
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid()

"""plot Bezdimenzijska debljina uljnog filma"""
plt.figure()
plt.plot(theta, hpot, 'ro-', label='moj proračun') #vratiti na SN
plt.xlim((-1,6.5))
plt.ylim((0,2))
plt.title('Debljina uljnog filma u odnosu na kut')
plt.xlabel('kut')
plt.ylabel('Debljina uljnog filma')
plt.legend(loc='upper left')
plt.grid()
plt.show

"""plot Bezdimenzijski tlak uljnog filma"""


import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# create 2d x,y grid (both X and Y will be 2d)
X, Y = np.meshgrid(theta, sirin)

# get 2D z data
Z = p.T

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
                cmap='viridis', edgecolor='none')
ax.set_title('Bezdimenzijski tlak u polju segmenta');
ax.set_xlabel('Kut segmenta [rad].')
ax.set_ylabel('Bezd. širina segm. /21 ')
ax.set_zlabel('Bezdimenz. tlak p');

plt.show()

"""Konturni plot bezdimenzijskog tlaka uljnog filma"""

fig, ax = plt.subplots(figsize=(6,6))


"ax.set_aspect('equal')"
ax.set_title('Konturni plot tlaka uljnog filma')
cf = ax.contourf(X,Y,Z)
fig.colorbar(cf, ax=ax)

plt.show()

"""plot Bezdimenzijske debljine uljnog filma segmenta 3,4,1,2"""
plt.figure()
plt.plot(theta3, hpot1, 'ro-', label='segment 3') #vratiti na SN
plt.xlim((0,6.5))
plt.ylim((-0.1,3.5))
plt.title('Debljina uljnog filma segment 3')
plt.xlabel('kut')
plt.ylabel('Debljina uljnog filma')
plt.legend(loc='upper left')
plt.grid()
plt.show


plt.plot(theta4, hpot1, 'ks-', label='segment 4') #vratiti na SN
plt.xlim((0,6.5))
plt.ylim((-0.1,3.5))
plt.title('Debljina uljnog filma segment 4')
plt.xlabel('kut')
plt.ylabel('Debljina uljnog filma')
plt.legend(loc='upper right')
plt.grid()
plt.show

plt.plot(theta1, hpot1, 'b-^', label='segment 1') #vratiti na SN
plt.xlim((0,6.5))
plt.ylim((-0.1,3.5))
plt.title('Debljina uljnog filma segment 1')
plt.xlabel('kut')
plt.ylabel('Debljina uljnog filma')
plt.legend(loc='upper right')
plt.grid()
plt.show


plt.plot(theta2, hpot1, 'g-^', label='segment 2') #vratiti na SN
plt.xlim((0,6.5))
plt.ylim((-0.1,3.5))
plt.title('Debljina uljnog filma svih segmenata')
plt.xlabel('kut')
plt.ylabel('Debljina uljnog filma')
plt.legend(loc='upper right')
plt.grid()
plt.show

"""plot Bezdimenzijske debljine uljnog filma segmenta 3,4,1,2"""
plt.figure()
plt.plot(theta, hpot1, 'g-^', label='segmenti 1-4') #vratiti na SN
plt.xlim((0,6.5))
plt.ylim((-0.1,3.5))
plt.title('Bezdimenzijska debljina uljnog filma svih segmenata')
plt.xlabel('kut theta (od pravca debalansa) = fi (od x osi) - att')
plt.ylabel('Bezdimenzijska debljina uljnog filma')
plt.legend(loc='upper left')
plt.grid()
plt.show

"""plot Bezdimenzijske debljine uljnog filma segmenta 3,4,1,2"""
plt.figure()
plt.plot(kut, hpot1, 'g-^', label='segmenti 1-4') #vratiti na SN
plt.xlim((0,6.5))
plt.ylim((-0.1,3.5))
plt.title('Bezdimenzijska debljina uljnog filma svih segmenata')
plt.xlabel('kut fi (od x osi)')
plt.ylabel('Bezdimenzijska debljina uljnog filma')
plt.legend(loc='upper left')
plt.grid()
plt.show

