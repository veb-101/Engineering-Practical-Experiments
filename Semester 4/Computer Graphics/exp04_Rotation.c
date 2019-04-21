#include <graphics.h>
#include <stdlib.h>
#include <stdio.h>
#include <conio.h>
#include <math.h>

int roundno(float num){
    return num < 0 ? num - 0.5 : num + 0.5;
}

void rotation(int x1, int y1, int x2, int y2, int x3,int y3){
    int newx1, newy1, newx2, newy2, newx3, newy3, r;
    float t, sine, cose;
    printf("\nEnter the angle for rotation: ");
    scanf("%d",&r);
    t=3.14*r/180;
    // shifting to  a reference point
    x1 -= 100;
    y1 -= 100;
    x2 -= 100;
    y2 -= 100;
    x3 -= 100;
    y3 -= 100;
    sine = sin(t);
    cose = cos(t);
    newx1 = roundno((x1*cose) - (y1*sine));
    newy1 = roundno((x1*sine) + (y1*cose));
    newx2 = roundno((x2*cose) - (y2*sine));
    newy2 = roundno((x2*sine) + (y2*cose));
    newx3 = roundno((x3*cose) - (y3*sine));
    newy3 = roundno((x3*sine) + (y3*cose));
    // cause anticlockwise spin
    // newx1 -= 100;
    // newy1 -= 100;
    // newx2 -= 100;
    // newy2 -= 100;
    // newx3 -= 100;
    // newy3 -= 100;
    line(newx1,newy1,newx2,newy2);
    line(newx2,newy2,newx3,newy3);
    line(newx3,newy3,newx1,newy1);
    delay(50);
}

void main()
{
	int gm,gd=DETECT;
	int x1,x2,x3,y1,y2,y3,choice;
	initgraph(&gd,&gm,"C:\\TURBOC3\\BGI");
	printf("\nEnter the coordinates of triangle(x1, y1), (x2, y2), (x3, y3):");
	scanf("%d%d%d%d%d%d",&x1,&y1,&x2,&y2,&x3,&y3);
    line(x1,y1,x2,y2);
	line(x2,y2,x3,y3);
	line(x3,y3,x1,y1);
    rotation(x1, y1, x2, y2, x3, y3);
    getch();
	closegraph();
}
