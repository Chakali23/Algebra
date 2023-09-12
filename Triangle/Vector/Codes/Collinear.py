import numpy as np 
import matplotlib.pyplot as plt 
from numpy import linalg as LA 
import math

A = np.array(([0, -5])) 
B = np.array(([-2, -4]))
C = np.array(([-5, -4]))

def line_gen(A,B):
   len =2
   dim = A.shape[0]
   x_AB = np.zeros((dim,len))
   lam_1 = np.linspace(0,1,len)
   for i in range(len):
     temp1 = A + lam_1[i]*(B-A)
     x_AB[:,i]= temp1.T
   return x_AB

Mat = np.array([[1,1,1],[A[0],B[0],C[0]],[A[1],B[1],C[1]]])

rank = np.linalg.matrix_rank(Mat)

if (rank<=2):
 print("Hence proved that points A,B,C in a triangle are collinear")
else:
 print("The given points are not collinear")

#Generating all lines
x_AB = line_gen(A,B)
x_BC = line_gen(B,C)
x_CA = line_gen(C,A)

#Plotting all lines
plt.plot(x_AB[0,:],x_AB[1,:],label='AB')
plt.plot(x_BC[0,:],x_BC[1,:],label='BC')
plt.plot(x_CA[0,:],x_CA[1,:],label='CA')

plt.text(-5, -3.8, 'A')
plt.text(-2, -3.8, 'B')
plt.text(0, -5.2, 'C')

#Labeling the coordinates
tri_coords = np.vstack((A,B,C)).T
plt.scatter(tri_coords[0,:], tri_coords[1,:])

plt.xlabel('$X-Axis$')
plt.ylabel('$Y-axis$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')
plt.title('Triangle ABC',size=10)
#if using termux
plt.savefig('/sdcard/Documents/figs/Collinear')
plt.show()
