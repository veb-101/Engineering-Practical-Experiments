#include<graphics.h>
#include<stdio.h>
#include<conio.h>
#include<math.h>

int bresenLine(int x1, int y1, int x2, int y2){
    int x, y, step, dx, dy, i, p;
    dx = abs(x2 - x1);
    dy = abs(y2 - y1);
    if(dx >= dy)
        step = dx;
    else
        step = dy;
    x = x1;
    y = y1;
    if (step == dx){ // m <  1
        p = (2 * dy) - dx;
        putpixel(x, y, WHITE);
        for(i=x1;i<=x2; i++){
            if(p<0){
                putpixel(x, y, WHITE);
                x += 1;
                p += (2 * dy);
            }
            else{
                putpixel(x, y, WHITE);
                x += 1;
                y += 1;
                p += ((2*dy) - (2*dx));
            }
        }
    }
    else{  // m > 1
        p = (2 * dx) - dy;
        putpixel(x, y, WHITE);
        for(i=x1;i<y2;i++){
            if(p<0){
                putpixel(x, y, WHITE);
                y += 1;
                p += (2 * dx);
                delay(20);
            }
            else{
                putpixel(x, y, WHITE);
                x += 1;
                y += 1;
                p += ((2*dx) - (2*dy));
                delay(20);
            }
        }
    }
    getch();
    return 0;
}


void main(){
    int gd=DETECT, gm;
    int x1, x2, y1, y2;
    initgraph(&gd, &gm, "C:\\TURBOC3\\BGI");
    printf("Enter co-ordinates (x1, y1), (x2, y2):");
    scanf("%d%d%d%d\n", &x1, &y1, &x2, &y2);
    bresenLine(x1, y1, x2, y2);
    getch();
    closegraph();
}
