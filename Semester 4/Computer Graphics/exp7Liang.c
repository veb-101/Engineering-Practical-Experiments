#include <stdio.h>
#include <conio.h>
#include <graphics.h>
#include <math.h>

float compareMin(float a, float b){
    if (a < b){
        return a;
    }
    return b;
}

float compareMax(float a, float b){
    if (a < b){
        return b;
    }
    return a;
}

int main()
{
    int gd = DETECT, gm;
    int x1, x2, y1, y2, xmin, xmax, ymin, ymax, i;
    int dx, dy, x1new, x2new, y1new, y2new;
    float t[4], p[4], q[4], tmin, tmax;
    initgraph(&gd, &gm, "C:\\TURBOC3\\BGI");
    printf("Enter coordinates of a line (x1, y1) (x2, y2): ");
    scanf("%d%d%d%d", &x1, &y1, &x2, &y2);
    printf("Enter viewport coordinates(xmin,ymin) (xmax, ymax): ");
    scanf("%d%d%d%d", &xmin, &ymin, &xmax, &ymax);
    line(x1, y1, x2, y2);              //Line to be clipped
    rectangle(xmin, ymin, xmax, ymax); // viewport
    getch();
    dx = x2 - x1;
    dy = y2 - y1;
    tmin = 0.0;
    tmax = 1.0;
    p[0] = -dx;
    p[1] = dx;
    p[2] = -dy;
    p[3] = dy;
    q[0] = x1 - xmin;
    q[1] = xmax - x1;
    q[2] = y1 - ymin;
    q[3] = ymax - y1;

    for(i = 0; i < 4; i++)
	t[i] = q[i] / p[i];

    for (i = 0; i < 4; i++){
        if (p[i] == 0.0 && q[i] < 0.0){
            cleardevice();
            printf("\nLine lies completely outside");
            rectangle(xmin, ymin, xmax, ymax);
            getch();
            return 0;
        }
        else if (p[i] < 0.0)
            tmin = compareMax(tmin, t[i]);
        else if (p[i] > 0.0)
            tmax = compareMin(tmax, t[i]);
    }

    if (tmin > tmax){
        cleardevice();
        printf("\nLine lies completely outside");
        rectangle(xmin, ymin, xmax, ymax);
        getch();
        return 0;
    }
    else if (tmin != 0.0 && tmax != 1.0){
        x1new = (int)(x1 + (tmin * dx));
        y1new = (int)(y1 + (tmin * dy));
        x2new = (int)(x1 + (tmax * dx));
        y2new = (int)(y1 + (tmax * dy));
        cleardevice();
        printf("Line after clipping");
        rectangle(xmin, ymin, xmax, ymax);
        line(x1new, y1new, x2new, y2new);
    }
    else if (tmin == 0.0 && tmax != 1.0){
        x2new = (int)(x1 + (tmax * dx));
        y2new = (int)(y1 + (tmax * dy));
        cleardevice();
        printf("Line partially inside");
        rectangle(xmin, ymin, xmax, ymax);
        line(x1, y1, x2new, y2new);
    }
    else if (tmin != 0.0 && tmax == 1.0){
        x1new = (int)(x1 + (tmin * dx));
        y1new = (int)(y1 + (tmin * dy));
        cleardevice();
        printf("Line partially inside");
        rectangle(xmin, ymin, xmax, ymax);
        line(x1new, y1new, x2, y2);
    }
    else{
        cleardevice();
        printf("Line Already inside");
        rectangle(xmin, ymin, xmax, ymax);
        line(x1, y1, x2, y2);
    }

    getch();
    closegraph();
    return 0;
}