#include <graphics.h>
#include <stdio.h>


void translation(int x1, int y1, int x2, int y2, int x3, int y3){
    int x, y, newx1, newy1, newx2, newy2, newx3, newy3;
    printf("Enter translation co-ordinates (x, y): ");
    scanf("%d%d",&x,&y);
    newx1=x1+x;
    newy1=y1+y;
    newx2=x2+x;
    newy2=y2+y;
    newx3=x3+x;
    newy3=y3+y;
    printf("After translation:\n");
    line(newx1, newy1, newx2, newy2);
    line(newx2, newy2, newx3, newy3);
    line(newx3, newy3, newx1, newy1);

}

void main()
{
	int gm,gd=DETECT;
	int x1,x2,x3,y1,y2,y3,choice;
	initgraph(&gd,&gm,"C:\\TURBOC3\\BGI");
	printf("\nEnter the coordinates of triangle(x1, y1), (x2, y2), (x3, y3):");
	// setcolor(20);
	scanf("%d%d%d%d%d%d",&x1,&y1,&x2,&y2,&x3,&y3);
    line(x1,y1,x2,y2);
	line(x2,y2,x3,y3);
	line(x3,y3,x1,y1);
    translation(x1, y1, x2, y2, x3, y3);
    getch();
	closegraph();
}
