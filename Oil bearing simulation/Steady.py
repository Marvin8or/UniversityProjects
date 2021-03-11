# -*- coding: utf-8 -*-
"""
Created on Sun May 26 03:43:49 2019 - promjena definicjje kuta

@author: 
"""

import numpy as np


"""import"""
# m = 61  #korigirano na 63 pa vraćeno na 61
# n = 21
# e =  np.array([0.103, 0.15, 0.224, 0.352, 0.46, 0.559, 0.65, 0.734, 0.773, 0.793, 0.811, 0.883])
# epsi = 0.883
# lod = 1
# groovx = 10*np.pi/180
# groovz = 0.5
# ps = 0 #promijeni na 0
def function_steady6(m, n, epsi, lod, groovx, groovz, ps):
    
   
    er2 = 1
    n2 = 0
    att = 0.01
    att1 = 0.01
    ORF = 1.8
    URF = 0.6
    DTH = 2.0*np.pi/(m-1)
    DZ = 1.0/(n-1)  
    """Naredba switch1 služi kako bi program
    kasnije mogao prepoznati na kojim se mjestima nalaze utori"""
    switch1 = np.zeros([m+1,n+1])
    p = np.zeros([m+1,n+1])
    h = np.zeros([m+1,n+1])
    h1 = np.zeros([m+1,n+1])
    hpot = np.zeros([m+1])
    hpot1 = np.zeros([m+1])
    theta = np.zeros([m+1])
    hpot2 = np.zeros([m+1])
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
    """Oznake početka i kraja segmenata"""
    
    ig11 = 1 #0
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
            p[I,J] = ps
            switch1[I,J] = 1                                                     
                   
    """second groove"""
    for J in range(jg1,jg2+1):
        for I in range(ig3,ig4+1):
            p[I,J] = ps
            switch1[I,J] = 1
                
    """third groove"""
    for J in range(jg1,jg2+1):
        for I in range(ig5,ig6+1):
            p[I,J] = ps
            switch1[I,J] = 1
            
    """fourth groove"""
    for J in range(jg1,jg2+1):
        for I in range(ig7,ig8+1):
            p[I,J] = ps
            switch1[I,J] = 1
            
  
    while (er2>Accuracy) and (n2<10**3):
        n2 = n2+1
        
        eps1=np.sqrt(epsi**2+deltazrac**2+2*epsi*deltazrac*np.cos(att))
        arg1=epsi*np.sin(att)/(deltazrac+epsi*np.cos(att))
        fi1=np.arctan(arg1)
    
        eps2=np.sqrt(epsi**2+deltazrac**2-2*epsi*deltazrac*np.cos(np.pi/2+att))
        arg2=(deltazrac+epsi*np.sin(att))/(epsi*np.sin(att))
        fi2=np.arctan(arg2)
    
        eps3=np.sqrt(epsi**2+deltazrac**2-2*epsi*deltazrac*np.cos(att))
        arg3=epsi*np.sin(att)/(-deltazrac+epsi*np.cos(att))
        fi3=np.pi+np.arctan(arg3)
    
        eps4=np.sqrt(epsi**2+deltazrac**2-2*epsi*deltazrac*np.cos(np.pi/2-att))
        arg4=(-deltazrac+epsi*np.sin(att))/(epsi*np.sin(att))
        fi4=np.arctan(arg4)

        """segment broj 3 - prvi dio"""       
        for I in range(ig11,ig21):#1-8
            x = (I)*DTH
            theta3[I] = -att + x
            hpot1[I] = 1+(psizrac-1)+eps3*np.cos(theta3[I]+ att-fi3)  
            
            for J in range(1,n+1):                    
                h[I,J] = 1+(psizrac-1)+eps3*np.cos(theta3[I]+att-fi3) 
            
        """segment broj 4"""       
        for I in range(ig31,ig41):#8-24
            x = (I)*DTH
            theta4[I] =-att + x
            hpot1[I] = 1+(psizrac-1)+eps4*np.cos(theta4[I]+ att-fi4)  
            
            for J in range(1,n+1):                
                h[I,J] = 1+(psizrac-1)+eps4*np.cos(theta4[I]+att-fi4) 
              

        """segment broj 1"""
        for I in range(ig51,ig61):#24-39
            x = (I)*DTH
            theta1[I] = -att + x
            """hpot1[I] = 1+psizrac-1+eps1*np.cos(theta1[I])"""
            hpot1[I] = 1+(psizrac-1)+eps1*np.cos(theta1[I]+ att-fi1)
                  
            for J in range(1,n+1):
                h[I,J] = 1+(psizrac-1)+eps1*np.cos(theta1[I]+att-fi1)     
    
                               
        """segment broj 2"""                    
        for I in range(ig71,ig81):#39-54
            x = (I)*DTH
            theta2[I] = -att + x
            """hpot2[I] =I""" 
            hpot1[I] = 1+(psizrac-1)+eps2*np.cos(theta2[I]+ att-fi2)

            for J in range(1,n+1):
                h[I,J] = 1+(psizrac-1)+eps2*np.cos(theta2[I] + att - fi2)       

        """segment broj 3 - drugi dio"""
        for I in range(ig81,ig91):#54-62
            x = (I)*DTH
            theta3[I] = - att + x
            """hpot2[I] =I""" 
            hpot1[I] = 1+(psizrac-1)+eps3*np.cos(theta3[I] + att - fi3)   
       
            for J in range(1,n+1): 
                h[I,J] =  1+(psizrac-1)+eps3*np.cos(theta3[I]  + att - fi3)         

        
        """svi segmenti"""  
        for I in range(m):
            x = (I)*DTH   
            kut[I]=x 
            theta[I] =  x - att
            
            
            for J in range(n):
                sirin[J]=J
            
        """FDM za stacionarno stanje"""     
        A1 = np.zeros([m,n]) #dodano
        A2 = np.zeros([m,n]) #dodano
        A3 = np.zeros([m,n]) #dodano
        A4 = np.zeros([m,n]) #dodano
        A5 = np.zeros([m,n]) #dodano
        A6 = np.zeros([m,n]) #dodano
    
        for J in range(1,n):
            for I in range(1,m):
                cc1 = h[I+1,J]-h[I-1,J]
                A1[I,J] = h[I,J]**(3) + 0.75*cc1*h[I,J]**(2)
                A2[I,J] = h[I,J]**(3) - 0.75*cc1*h[I,J]**(2)
                A3[I,J] = alfa*h[I,J]**(3)
                A4[I,J] = alfa*h[I,J]**(3)
                A5[I,J] = -1.5*DTH*cc1   
                A6[I,J] = 2*(1+alfa)*h[I,J]**(3)    
                

        n1 = 0
        sum2 = 0
        er1 = 1
        while (er1>Accuracy) and (n1<10**3):
            for J in range(1,n):
                for I in range(1,m):
                    if (switch1[I,J] != 1):
                        term = (A1[I,J]*p[I+1,J]+A2[I,J]*p[I-1,J]+A3[I,J]*p[I,J+1]+A4[I,J]*p[I,J-1]+A5[I,J])/A6[I,J];
                        """Gauss-Seidel over-relaxation"""
                        p[I,J] = p[I,J]+ORF*(term-p[I,J])
                        """first B.C's (no cavitation)"""
                        if (p[I,J] < 0):
                            p[I,J] = 0
    
            sum1 = sum(sum(p))
            p[:,0] = p[:,2]
            
            """estimate error"""
            er1 = abs(sum1-sum2)/sum1
            sum2 = sum1
            n1 = n1+1
            
        """calculating load carrying capacity (Trapezoidal Integration)
        integration in axial direction"""
        inty = np.zeros(m) #Zamjena?
        for I in range(m):
            for J in range(1,n):
                inty[I] = inty[I]+p[I,J]+p[I,J-1]
            inty[I] = inty[I]*0.5*DZ
            
        """axialw, tangew: axial and tangential component of load"""   
        axialw = 0
        tangew = 0
        
        """integration in circumferential direction"""
        for I in range(1,m):
            x = (I)*DTH;
            x2 = (I-1)*DTH;
            axialw = axialw-np.cos(x)*inty[I]-np.cos(x2)*inty[I-1]
            tangew = tangew+np.sin(x)*inty[I]+np.sin(x2)*inty[I-1]
        axialw = axialw*0.5*DTH
        tangew = tangew*0.5*DTH
        loadw = np.sqrt(axialw**2+tangew**2)
        attang = np.arctan(tangew/axialw)
        if (axialw > 0):
            attang1 = attang
        elif (axialw < 0):
            attang1 = -attang          
        """Gauss-Seidel under-relaxation"""
        att = att + URF*attang1
        er2 = abs(att-att1)/att
        att1 = att


    return[kut,hpot1,theta2,theta1,theta4,theta3,sirin,hpot,theta,p,axialw,tangew,loadw,att]   
