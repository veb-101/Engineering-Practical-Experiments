#include<stdio.h>
#include<conio.h>
#include<graphics.h>
#include<math.h>

// try points (100, 200), (150 , 150), (160, 150), (200, 200)
// For clarification watch
// https://www.youtube.com/watch?v=J0fSfx8a8dY 

void bezier(int x[4], int y[4]){
    int i;
    double t, xt, yt;

    line(x[0], y[0], x[1], y[1]);
    line(x[1], y[1], x[2], y[2]);
    line(x[2], y[2], x[3], y[3]);
    
    // 4 control points
    // order = 3
    // 0, 1, 2, 3
    // similar to (a-b)^3
    // bezier eqn = P0*(1-t)^3 + P1*3t(1-t)^2 + P2*3t^2*(1-t) + P3*t^3
    // generated using bernstein's eqn. and plugged in bezier eqn.
    // Pi = (xi, yi)
    for (t = 0.0; t < 1.0; t += 0.00005)
    {
        xt = pow(1 - t, 3) * x[0] + 3 * t * pow(1 - t, 2) * x[1] +
                    3 * pow(t, 2) * (1 - t) * x[2] + pow(t, 3) * x[3];

        yt = pow(1 - t, 3) * y[0] + 3 * t * pow(1 - t, 2) * y[1] +
                    3 * pow(t, 2) * (1 - t) * y[2] + pow(t, 3) * y[3];

        putpixel(xt, yt, WHITE);
    }
}

void main(){
    int gd=DETECT, gm;
    int x[4], y[4];
    int i;
    initgraph(&gd, &gm, "C:\\TURBOC3\\BGI");
    printf("Enter the x-coordinates and y-coordinates of 4 control points: ");
    for(i=0; i<4; i++)
        scanf("%d%d", &x[i], &y[i]);
    
    bezier(x, y);
    getch();
    closegraph();
} 