import numpy as np
import sys                                          #for path to external scripts
sys.path.insert(0, '/sdcard/Documents/CoordGeo')        #path to my scripts
#sys.path.insert(0, 'solutions/1/1/3/codes/CoordGeo')        #path to my scripts
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import math
#from line.funcs import *
#from triangle.funcs import *
#from conics.funcs import circ_gen
#import subprocess
#import shlex


def line_gen(A,B):
  len =10
  dim = A.shape[0]
  x_AB = np.zeros((dim,len))
  lam_1 = np.linspace(0,1,len)
  for i in range(len):
    temp1 = A + lam_1[i]*(B-A)
    x_AB[:,i]= temp1.T
  return x_AB
np.set_printoptions(precision=2)

A= np.array([0,-5])
B= np.array([-2,-4])
C= np.array([-5,-4])

#Mat = np.array([[1,1,1],[A[0],B[0],C[0]],[A[1],B[1],C[1]]])

#rank = np.linalg.matrix_rank(Mat)

#if (rank<=2):
 #print("Hence proved that points A,B,C in a triangle are collinear")
#else:
# print("The given points are not collinear")

#getting the equation of line AB
#omat = np.array([[0,1],[-1,0]])
#m = B-A   #direction vector
#n = omat@m    #normal vector
#c = n@A
#eqn = f"{n}x = {c}"
#print("The equation of line AB is",eqn)

#getting the equation of line BC
#omat = np.array([[0,1],[-1,0]])
#m = C-B   #direction vector
#n = omat@m    #normal vector
#c = n@B
#eqn = f"{n}x = {c}"
#print("The equation of line BC is",eqn)

#getting the equation of line CA
omat = np.array([[0,1],[-1,0]])
m = A-C   #direction vector
n = omat@m    #normal vector
c = n@C
eqn = f"{n}x = {c}"
print("The equation of line CA is",eqn)

#Generating all lines
#x_AB = line_gen(A,B)
#x_BC = line_gen(B,C)
x_CA = line_gen(C,A)

#Plotting all lines
#plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
#plt.plot(x_BC[0,:],x_BC[1,:],label='$BC$')
plt.plot(x_CA[0,:],x_CA[1,:],label='$CA$')

#Labeling the coordinates
A = A.reshape(-1,1)
#B = B.reshape(-1,1)
C = C.reshape(-1,1)
#tri_coords = np.block([[A, B, C]])
#tri_coords = np.block([[A, B]])
#tri_coords = np.block([[B, C]])
tri_coords = np.block([[C, A]])
plt.scatter(tri_coords[0, :], tri_coords[1, :])
#vert_labels = ['A', 'B','C']
#vert_labels = ['A', 'B']
#vert_labels = ['B', 'C']
vert_labels = ['C', 'A']
for i, txt in enumerate(vert_labels):
    offset = 10 if txt == 'C' else -10
    plt.annotate(txt,
                 (tri_coords[0, i], tri_coords[1, i]),
                 textcoords="offset points",
                 xytext=(0, offset),
                 ha='center')

plt.xlabel('$X-axis$')
plt.ylabel('$Y-axis$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')

#if using termux
plt.savefig('/sdcard/Documents/figs/CA')
plt.show()
