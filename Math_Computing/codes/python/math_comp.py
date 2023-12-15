import sys                                          #for path to external scripts
sys.path.insert(0, '/sdcard/Documents/CoordGeo')        #path to my scripts
import numpy as np
import numpy.linalg as LA
import scipy.linalg as SA
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import pandas as pd
import math as m

#local imports
from line.funcs import *
from triangle.funcs import *
from conics.funcs import circ_gen

#if using termux
import subprocess
import shlex
#end if

A = np.array([0,0]).reshape(-1,1)
B = np.array([5,0]).reshape(-1,1) 
P = (A+B)/2             # Mid-point of AB
r = LA.norm(A-B)         #length of AD and BE
theta1=m.pi/6           # angle BAD and angle ABE30 degrees
theta2=m.pi/3          #angle EPA and and angle DPB 60 degrees
D = A + np.array([r*m.cos(theta1),r*m.sin(theta1)]).reshape(-1,1)
E = B + np.array([-r*m.cos(theta1),r*m.sin(theta1)]).reshape(-1,1)
D = P + np.array([r*m.cos(theta2),r*m.sin(theta2)]).reshape(-1,1)
E = P + np.array([-r*m.cos(theta2),r*m.sin(theta2)]).reshape(-1,1)
print(P,"\n",D,"\n",E,"\n")
print(r,"\n")

x1 = LA.norm(A-D)    #length of AD
x2 = LA.norm(B-E)    #length of BE
print(x1,"\n",x2,"\n")
print("1.By the definition of AAS congruency rule if any two pair of angles and one pair of corresponding sides are equal then the two triangles are said to be congruent \n\n")


if(x1==x2):
    print("2.AD equals BE")
else:
    print("2.AD not equals to BE")


#Generating all lines
x_AB = line_gen(A,B)
x_AD = line_gen(A,D)
x_BE = line_gen(B,E)
x_PD = line_gen(P,D)
x_PE = line_gen(P,E)

#Plotting all lines
plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
plt.plot(x_AD[0,:],x_AD[1,:],label='$AD$')
plt.plot(x_BE[0,:],x_BE[1,:],label='$BE$')
plt.plot(x_PD[0,:],x_PD[1,:],label='$PD$')
plt.plot(x_PE[0,:],x_PE[1,:],label='$PE$')

#Labeling the coordinates
tri_coords = np.block([[A,B,P,D,E]])
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = ['A','B','P','D','E']
for i, txt in enumerate(vert_labels):
    plt.annotate(txt, # this is the text
                 (tri_coords[0,i], tri_coords[1,i]), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 
                 ha='center') # horizontal alignment can be left, right or center
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')

#if using termux
plt.savefig('/sdcard/Documents/figs/fig_mat_comp.png')
#subprocess.run(shlex.split("termux-open ./figs/tri_sss.pdf"))
#else
plt.show()
