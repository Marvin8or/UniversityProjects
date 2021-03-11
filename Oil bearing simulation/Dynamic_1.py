# -*- coding: utf-8 -*-
"""
Created on Tue May 28 23:42:19 2019

@author: franko
"""

import numpy as np
"""import"""
# m = 61
# n = 21
# epsi = 0.883
# lod = 1
# groovx = 10*np.pi/180
# groovz = 0.5
# ps = 0
# omega = 1
# p = np.zeros([m+1,n+1])
# phi = 0

def function_d14segment(m, n, epsi, lod, groovx, groovz, ps, omega, p, phi):
    ORF = 1.8
    DTH = 2.0*np.pi/(m-1)
    DZ = 1.0/(n-1)
    switch1 = np.zeros([m+1,n+1])
    p1 = np.zeros([m+1,n+1],dtype=complex)
    h = np.zeros([m+1,n+1])
    hpot = np.zeros([m+1])
    hpot1 = np.zeros([m+1])
    theta = np.zeros([m+1])
    theta1 = np.zeros([m+1])
    theta2 = np.zeros([m+1])
    theta3 = np.zeros([m+1])
    theta4 = np.zeros([m+1])
    kut = np.zeros([m+1])
    sirin = np.zeros([n+1])
    
    i1 = round(groovx/DTH)
    j1 = round(groovz/DZ)

    ig1 = int(((m-1)*0.67/4)-i1) #8
    ig2 =int(((m-1)*0.67/4)+i1) #12
    ig3 = int(((m-1)*1.67/4)-i1) #23
    ig4 = int(((m-1)*1.67/4)+i1) #27
    ig5 = int(((m-1)*2.67/4)-i1) #38
    ig6 = int(((m-1)*2.67/4)+i1) #42
    ig7 = int(((m-1)*3.67/4)-i1) #53 
    ig8 = int(((m-1)*3.67/4)+i1) #57
    jg1 = int(((n-1)/2)-j1) 
    jg2 = int(((n-1)/2)+j1)
    alfa = ((1/lod)*(DTH/DZ))**2
    Accuracy = 10**(-8)

 
    """Dodatne početne postavke za prvi segmenat"""
    
    
    ig11 = 1 #45-fizl/2
    ig21 = 8 #2
    
    ig31 = 8 #18
    ig41 = 24 #22
    
    ig51 = 24 #38
    ig61 = 39 #42
    
    ig71 = 39 #59 
    ig81 = 54 #59
    ig91 = 62 #61
    
    psizrac=4
    deltazrac=psizrac-1
       
   

    """first groove"""
    for J in range(jg1,jg2+1):
        for I in range(ig1,ig2+1):
            p1[I,J] = ps
            switch1[I,J] = 1                                                     
                   
    """second groove"""
    for J in range(jg1,jg2+1):
        for I in range(ig3,ig4+1):
            p1[I,J] = ps
            switch1[I,J] = 1
                
    """third groove"""
    for J in range(jg1,jg2+1):
        for I in range(ig5,ig6+1):
            p1[I,J] = ps
            switch1[I,J] = 1
            
    """fourth groove"""
    for J in range(jg1,jg2+1):
        for I in range(ig7,ig8+1):
            p1[I,J] = ps
            switch1[I,J] = 1
            
        
    eps1=np.sqrt(epsi**2+deltazrac**2+2*epsi*deltazrac*np.cos(phi))
    arg1=epsi*np.sin(phi)/(deltazrac+epsi*np.cos(phi))
    fi1=np.arctan(arg1)
    
    eps2=np.sqrt(epsi**2+deltazrac**2-2*epsi*deltazrac*np.cos(np.pi/2+phi))
    arg2=(deltazrac+epsi*np.sin(phi))/(epsi*np.sin(phi))
    fi2=np.arctan(arg2)
    
    eps3=np.sqrt(epsi**2+deltazrac**2-2*epsi*deltazrac*np.cos(phi))
    arg3=epsi*np.sin(phi)/(-deltazrac+epsi*np.cos(phi))
    fi3=np.pi+np.arctan(arg3)
    
    eps4=np.sqrt(epsi**2+deltazrac**2-2*epsi*deltazrac*np.cos(np.pi/2-phi))
    arg4=(-deltazrac+epsi*np.sin(phi))/(epsi*np.sin(phi))
    fi4=np.arctan(arg4)


    """segment broj 3 - prvi dio"""       
    for I in range(ig11,ig21):
        x = (I)*DTH
        theta3[I] = -phi + x
        hpot1[I] = 1+(psizrac-1)+eps3*np.cos(theta3[I]+ phi-fi3)  
            
        for J in range(1,n+1):                    
            h[I,J] = 1+(psizrac-1)+eps3*np.cos(theta3[I]+phi-fi3) 
            
    """segment broj 4"""       
    for I in range(ig31,ig41):
        x = (I)*DTH
        theta4[I] =-phi + x
        hpot1[I] = 1+(psizrac-1)+eps4*np.cos(theta4[I]+ phi-fi4)  
            
        for J in range(1,n+1):                
            h[I,J] = 1+(psizrac-1)+eps4*np.cos(theta4[I]+phi-fi4) 
              

    """segment broj 1"""
    for I in range(ig51,ig61):
        x = (I)*DTH
        theta1[I] = -phi + x
        hpot1[I] = 1+(psizrac-1)+eps1*np.cos(theta1[I]+ phi-fi1)
                  
        for J in range(1,n+1):
            h[I,J] = 1+(psizrac-1)+eps1*np.cos(theta1[I]+phi-fi1)                             
                                
    """segment broj 2"""                    
    for I in range(ig71,ig81):
        x = (I)*DTH
        theta2[I] = -phi + x
        hpot1[I] = 1+(psizrac-1)+eps2*np.cos(theta2[I]+ phi-fi2)

        for J in range(1,n+1):
            h[I,J] = 1+(psizrac-1)+eps2*np.cos(theta2[I] + phi - fi2)       
        
    """segment broj 3 - drugi dio"""
    for I in range(ig81,ig91):
        x = (I)*DTH
        theta3[I] = - phi+ x
        hpot1[I] = 1+(psizrac-1)+eps3*np.cos(theta3[I] + phi - fi3)   
       
        for J in range(1,n+1): 
            h[I,J] =  1+(psizrac-1)+eps3*np.cos(theta3[I]  + phi - fi3)         

        
    """svi segmenti"""  
    for I in range(m):
        x = (I)*DTH   
        kut[I]=x 
        theta[I] =  x - phi
            
            
        for J in range(n):
            sirin[J]=J   
    
    n1 = 0
    sum2 = 0
    er = 1
    
    """FDM za stacionarno stanje"""  
    A1 = np.zeros([m,n],dtype=complex) #dodano
    A2 = np.zeros([m,n],dtype=complex) #dodano
    A3 = np.zeros([m,n],dtype=complex) #dodano
    A4 = np.zeros([m,n],dtype=complex) #dodano
    A5 = np.zeros([m,n],dtype=complex) #dodano
    A6 = np.zeros([m,n],dtype=complex) #dodano
    A7 = np.zeros([m,n],dtype=complex) #dodano
    A8 = np.zeros([m,n],dtype=complex) #dodano
    A9 = np.zeros([m,n],dtype=complex) #dodano
    A10 = np.zeros([m,n],dtype=complex) #dodano
    A11 = np.zeros([m,n],dtype=complex) #dodano
    for J in range(1,n):
        for I in range(1,m):
            seta = I*DTH
            cc1 = h[I+1,J]-h[I-1,J]
            A1[I,J] = h[I,J]**(3) + 0.75*cc1*h[I,J]**2
            A2[I,J] = h[I,J]**(3) - 0.75*cc1*h[I,J]**2
            A3[I,J] = alfa*h[I,J]**(3)
            A4[I,J] = alfa*h[I,J]**(3)
            A5[I,J] = -6*np.cos(seta)*(1+alfa)*h[I,J]**(2)
            A6[I,J] = 3*np.cos(seta)*h[I,J]**(2) + 1.5*np.cos(seta)*h[I,J]*cc1 - 1.5*np.sin(seta)*DTH*h[I,J]**(2)
            A7[I,J] = 3*np.cos(seta)*h[I,J]**(2) - 1.5*np.cos(seta)*h[I,J]*cc1 + 1.5*np.sin(seta)*DTH*h[I,J]**(2)
            A8[I,J] = 3*alfa*np.cos(seta)*h[I,J]**(2)
            A9[I,J] = 3*alfa*np.cos(seta)*h[I,J]**(2)
            A10[I,J] = -(DTH**2)*(-3*np.sin(seta)+1j*6*omega*np.cos(seta))
            A11[I,J] = 2*(h[I,J]**(3))*(1+alfa)
            
    """main loop for calculating pressure"""
    while (er > Accuracy) and (n1 < 10**3):
        for J in range(1,n):
            for I in range(1,m):
                if (switch1[I,J] != 1):
                    po = p1[I,J]
                    p1[I,J] = (A1[I,J]*p1[I+1,J] + A2[I,J]*p1[I-1,J] + A3[I,J]*p1[I,J+1] + \
                        A4[I,J]*p1[I,J-1] + A5[I,J]*p[I,J] + A6[I,J]*p[I+1,J] + A7[I,J]*p[I-1,J] + \
                        A8[I,J]*p[I,J+1] + A9[I,J]*p[I,J-1] + A10[I,J])/A11[I,J]
                    """Gauss-Seidel over-relaxation"""
                    p1[I,J] = po+ORF*(p1[I,J]-po)
                    """first B.C's (no cavitation)"""
                    if p[I,J] < 0:
                        p1[I,J] = 0.0
        sum1 = sum(sum(p1))
        
        """symmetry B.C's (dp/dz = 0)"""
        p1[:,0] = p1[:,2]
        
        """B.C's (no cavitation) (dp/dtheta = 0)"""
        """estimate error"""
        er = abs(1-sum2/sum1)
        sum2 = sum1
        n1 = n1+1
        
    """calculating dynamic load carrying capacity (Trapezoidal Integration)
    integration in axial direction"""
    inty = np.zeros(m,dtype=complex) #Zamjena?
    for I in range(m):
        inty[I]=0
        for J in range(1,n):
            inty[I] = inty[I]+p1[I,J]+p1[I,J-1]
        inty[I] = inty[I]*0.5*DZ
        
    """axialw, tangew: axial and tangential component of load"""
    axialw = 0
    tangew = 0
    
    """integration in circumferential direction"""
    for I in range(1,m):
        x = (I)*DTH
        x2 = (I-1)*DTH
        axialw = axialw+np.cos(x)*inty[I]+np.cos(x2)*inty[I-1]
        tangew = tangew+np.sin(x)*inty[I]+np.sin(x2)*inty[I-1]
    WXD1 = axialw*0.5*DTH
    WZD1 = tangew*0.5*DTH

    return[WXD1,WZD1]