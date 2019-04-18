#include<stdio.h>
#include<conio.h>
#include<graphics.h>

void x_shearing(int x1,int y1,int x2,int y2,int x3,int y3,int x4,int y4){
    int x_shear;
    printf("\nEnter x shear: ");
    scanf("%d",&x_shear);
    line(x1 + (x_shear * y1),y1,x2,y2);
    line(x2,y2,x3,y3);
    line(x3,y3,x4 + (x_shear * y4),y4);
    line(x4 + (x_shear * y4),y4,x1 + (x_shear * y1),y1);
    delay(100);
}

void y_shearing(int x1,int y1,int x2,int y2,int x3,int y3,int x4,int y4){
    int y_shear;
    printf("\nEnter y shear: ");
    scanf("%d" ,&y_shear);
    line(x1,y1,x2,y2);
    line(x2,y2,x3,y3 + (y_shear*x3));
    line(x3,y3 + (y_shear*x3),x4,y4 + (y_shear*x4));
    line(x4,y4 + (y_shear*x4),x1,y1);
    delay(20);
}

void main(){
int gd=DETECT,gm;
int x_shear, y_shear, choice, x1, y1, x2, y2, x3, y3, x4, y4;
clrscr();
initgraph(&gd,&gm,"C:\\TURBOC3\\BGI");
printf("\nEnter the coordinates of rectangle(4 points)");
scanf("%d%d%d%d%d%d%d%d",&x1,&y1,&x2,&y2,&x3,&y3,&x4,&y4);
line(x1,y1,x2,y2);
line(x2,y2,x3,y3);
line(x3,y3,x4,y4);
line(x4,y4,x1,y1);
printf("\nEnter choice: ");
scanf("%d", &choice);
switch (choice) {
    case 1:
        x_shearing(x1, y1, x2, y2, x3, y3, x4, y4);
        break;
    case 2:
        y_shearing(x1, y1, x2, y2, x3, y3, x4, y4);
        break;
}

getch();
closegraph();
}
