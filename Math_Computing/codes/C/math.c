//Code biy G V V Sharma
//October 27, 2023
//matrix operations using arrays
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "libs/matfun.h"
//printing the matrix

double radians(double deg)
{
  double rad;
  rad = deg*(M_PI / 180);
  return rad;
}

int  main()
{

FILE *fp; //file pointer
double **A,**B;//declaring matrices names
double **P;//declare P midpoint
double AD,BE,BP,AP,EB,DA;//direction vectors
double r; //Length of AD and BE
int m = 2, n = 2, o = 1;
double **vert;

double angle = radians(60);
// creating Matrix MAT and loading MATRIX from file
vert = createMat(m,n);
vert = loadMat("Mat.dat",m,n);

//Extracting vertices
A = Matcol(vert,m,0);
B = Matcol(vert,m,1);

//mid-point
P = Matsec(A,B,m,o);

//printMat(A,2,1);  
//printMat(B,2,1);  
//printMat(P,2,1);  

r = Matnorm(Matsub(A,B,m,n),m);
//printf("r = %lf\n",r);

double **D = createMat(m,o);
D = Mat_2(A,r,angle);
//printf("D\n");
//printMat(D,2,1);

double **E = createMat(m,o);
E = Mat_1(B,r,angle);
//printf("E\n");
//printMat(E,2,1);

BP = Matnorm(Matsub(B,P,m,o),m);
AP = Matnorm(Matsub(A,P,m,o),m);
EB = Matnorm(Matsub(E,B,m,o),m);
DA = Matnorm(Matsub(D,A,m,o),m);
//printf("For proving △ DAP ≅ △ EBP \n");
 if ((BP == AP) && (EB == DA)) {
        printf("△ DAP ≅ △ EBP (congruent By SAS Congruency)\n");
    } else {
        printf("△ DAP ≇ △ EBP (is NOT congruent)\n");
    };

//length of AD, BE
AD = Matnorm(Matsub(A,D,m,o),m);
BE = Matnorm(Matsub(B,E,m,o),m);
printf("\nAD = %lf\n",AD);
printf("\nBE = %lf\n",BE);

if(AD == BE)
	printf("\n AD is equal to BE\n");
else
	        printf("\n AD is not equal to BE\n");


return 0;
}
