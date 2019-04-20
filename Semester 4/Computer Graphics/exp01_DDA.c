#include<graphics.h>
#include<stdio.h>
#include<conio.h>
#include<math.h>
void main(){
    int gd=DETECT, gm, i;
    float x1, y1, x2, y2, x, y, step, dx, dy;
    initgraph(&gd, &gm, "C:\\TURBOC3\\BGI");
    clrscr();
    printf("Enter (x1, y1), (x2, y2) for the line:");
    scanf("%f%f%f%f\n",&x1, &y1, &x2, &y2);
    dx = (int)(x2 - x1);
    dy = (int)(y2 - y1);
    if (dx >= dy)
        step = dx;
    else
        step = dy;

    dx /= step;
    dy /= step;
    x = x1;
    y = y1;
    i = 1;
    while(i<=step){
        putpixel(x, y, WHITE);
        x += dx;
        y += dy;
        i += 1;
        delay(20);
    }
    getch();
    closegraph();

}
