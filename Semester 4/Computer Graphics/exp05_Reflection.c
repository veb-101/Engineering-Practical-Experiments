#include <graphics.h>
#include <stdio.h>
#include <conio.h>
#include <math.h>

void alongOrigin(int x1,int y1,int x2,int y2,int x3,int y3){
	int newx1,newx2,newx3,newy1,newy2, newy3;
	getch();
	printf("\nReflecting along origin");
	// along y-axis
	newx1 = 320 - (x1 - 320);
	newx2 = 320 - (x2 - 320);
	newx3 = 320 - (x3 - 320);
	// along x-axis
	newy1 = 240 - (y1- 240);
	newy2 = 240 - (y2- 240);
	newy3 = 240 - (y3- 240);
	line(newx1,newy1,newx2,newy2);
	line(newx2,newy2,newx3,newy3);
	line(newx3,newy3,newx1,newy1);
}

void main()
{
	int gm,gd=DETECT;
	int x1,x2,x3,y1,y2,y3, newx1,newx2,newx3,newy1,newy2, newy3;
	initgraph(&gd,&gm,"C:\\TURBOC3\\BGI");
	printf("\nEnter the coordinates of triangle(x>320):");
	scanf("%d%d%d%d%d%d",&x1,&y1,&x2,&y2,&x3,&y3);
	line(320, 0, 320, 480); //dividing screen vertically
	line(0, 240, 640, 240); //dividing screen horizontally
	line(x1,y1,x2,y2);
	line(x2,y2,x3,y3);
	line(x3,y3,x1,y1);
// middle of screen - (coordinates in right side - middle of screem)
// Y unchanged
	newx1 = 320 - (x1- 320);
	newx2 = 320 - (x2- 320);
	newx3 = 320 - (x3- 320);
	printf("Reflecting along y-axis");
	line(newx1,y1,newx2,y2);
	line(newx2,y2,newx3,y3);
	line(newx3,y3,newx1,y1);
	getch();
	printf("\nReflecting along x-axis" );
	newy1 = 240 - (y1- 240);
	newy2 = 240 - (y2- 240);
	newy3 = 240 - (y3- 240);
	line(x1,newy1,x2,newy2);
	line(x2,newy2,x3,newy3);
	line(x3,newy3,x1,newy1);
	alongOrigin(x1,y1,x2,y2,x3,y3);
    getch();
    closegraph();
}
