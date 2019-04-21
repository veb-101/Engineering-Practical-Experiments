#include <graphics.h>
#include <stdio.h>


void scaling(int x1, int y1, int x2, int y2, int x3, int y3){
    int x, y;
    int newx1, newy1, newx2, newy2, newx3, newy3;
    printf("Enter scaling co-ordinates (x, y): ");
    scanf("%d%d",&x,&y);
    // (- x1) (-y1) to shift back to starting co-ordinate
    newx1 = (x1*x) - x1;
    newy1 = (y1*y) - y1;
    newx2 = (x2*x) - x1;
    newy2 = (y2*y) - y1;
    newx3 = (x3*x) - x1;
    newy3 = (y3*y) - y1;
    cleardevice();
    printf("Line after scaling");
    line(newx1, newy1,newx2, newy2);
    line(newx2, newy2,newx3, newy3);
    line(newx3, newy3, newx1, newy1);
}

void main()
{
	int gm,gd=DETECT;
	int x1,x2,x3,y1,y2,y3,choice;
	initgraph(&gd,&gm,"C:\\TURBOC3\\BGI");
	printf("\nEnter the coordinates of triangle:");
	setcolor(20);
	scanf("%d%d%d%d%d%d",&x1,&y1,&x2,&y2,&x3,&y3);
    line(x1,y1,x2,y2);
	line(x2,y2,x3,y3);
	line(x3,y3,x1,y1);
    scaling(x1, y1, x2, y2, x3, y3);
    getch();
	closegraph();
}
