#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "libs/listgen.h"
#include "libs/listfun.h"

int  main()
{
avyuh *A,*B,*D,*E,*P,*vert;
double r; //lengths of a side 
int m =2,n=2,o=1; //(mxn) matrices
double CMA,BMD,DBC,BCA; //angles 
double AD, BE, BP, AP, EB, DA;
double theta;

//load matrix from file
vert = loadList("vertices.dat",m,n);

printList(vert);
//Triangle vertices
A = Listcol(vert,0);
B = Listcol(vert,1);


//printing the lists
//printList(vert);
printList(A);
printList(B);

P= Listsec(A,B,1);
printList(P);

r = Listnorm(Listsub(A,B));
 
theta = 60;
D = Mat(A, r, theta*(M_PI/180),1);
printf("\nD\n");
printList(D);


E = Mat( B,r, theta*(M_PI/180), -1);
printf("\nE\n");
printList(E);

BP = Listnorm(Listsub(B,P));
AP = Listnorm(Listsub(A,P));
EB = Listnorm(Listsub(E,B));
DA = Listnorm(Listsub(D,A));

AD = Listnorm(Listsub(A,D));
BE = Listnorm(Listsub(B,E));

//printf("For proving △ DAP ≅ △ EBP \n");
 if ((BP == AP) && (EB == DA)) {
        printf("△ DAP ≅ △ EBP (congruent By SAS Congruency)\n");
    } else {
        printf("△ DAP ≇ △ EBP (is NOT congruent)\n");
    };

if(AD == BE)
	printf("\n AD is equal to BE\n");
else
	        printf("\n AD is not equal to BE\n");


return 0;

}
