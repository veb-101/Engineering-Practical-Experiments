#include<graphics.h>
#include<stdio.h>
#include<conio.h>

void Circle(int xc, int yc, int r){
    int x=0, y=r, p = 1-r;
    do
    {

        //   (-x, y).....|......(x, y)
        // (-y, x).......|..........(y, x)
        // -----------(xc,yc)-----------------------
        // (-y, -x)......|.........(y, -x)
        //   (-x, -y)....|......(x, -y)

        putpixel(xc+x, yc+y, WHITE);
        putpixel(xc+x, yc-y, WHITE);
        putpixel(xc-x, yc-y, WHITE);
        putpixel(xc-x, yc+y, WHITE);
        delay(20);
        putpixel(xc+y, yc+x, WHITE);
        putpixel(xc+y, yc-x, WHITE);
        putpixel(xc-y, yc-x, WHITE);
        putpixel(xc-y, yc+x, WHITE);

        if (p<0){
            p += (2*x + 3);
        }
        else{
            p = p + 2*x - 2*y + 5;
            y -= 1;
        }
        x += 1;
        delay(20);
    } while (x<y);

}

void main(){
    int gd=DETECT, gm;
    int xc, yc, r;
    initgraph(&gd, &gm, "C:\\TURBOC3\\BGI");
    printf("Enter radius of the circle: ");
    scanf("%d", &r);
    printf("Enter center co-ordinates of circle: ");
    scanf("%d%d", &xc, &yc);
    Circle(xc, yc, r);
    getch();
    closegraph();
}
