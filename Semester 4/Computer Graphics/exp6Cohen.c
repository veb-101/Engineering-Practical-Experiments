// taken from https://www.askforprogram.in/2013/04/cohen-sutherland-line-clipping-algorithm-c-code.html


#include<stdio.h>
#include<conio.h>
#include<graphics.h>

void main()
{
    int gd = DETECT, gm;
    float i, xmax, ymax, xmin, ymin, x1, y1, x2, y2, m;
    float start[4], end[4], code[4];
    clrscr();
    initgraph(&gd, &gm, "C:\\TURBOC3\\BGI");
    printf("\nPlease enter the bottom left and top right co-ordinate of viewport: ");
    scanf("%f%f%f%f", &xmin, &ymin, &xmax, &ymax);
    printf("\nPlease enter the co-ordinates for starting point of line: ");
    scanf("%f%f%f%f", &x1, &y1, &x2, &y2);
    
    for (i = 0; i < 4; i++){
        start[i] = 0;
        end[i] = 0;
    }
    // LRBT 
    m = (y2 - y1) / (x2 - x1);
    if (x1 < xmin)
        start[0] = 1;
    if (x1 > xmax)
        start[1] = 1;
    if (y1 > ymax)
        start[2] = 1;
    if (y1 < ymin)
        start[3] = 1;
    if (x2 < xmin)
        end[0] = 1;
    if (x2 > xmax)
        end[1] = 1;
    if (y2 > ymax)
        end[2] = 1;
    if (y2 < ymin)
        end[3] = 1;

    for (i = 0; i < 4; i++)
        code[i] = start[i] && end[i];

    if ((code[0] == 0) && (code[1] == 0) && (code[2] == 0) && (code[3] == 0))
    {
        if ((start[0] == 0) && (start[1] == 0) && (start[2] == 0) && (start[3] == 0) && (end[0] == 0) && (end[1] == 0) && (end[2] == 0) && (end[3] == 0))
        {
            cleardevice();
            printf("\nThe line is totally visible and not a clipping candidate");
            rectangle(xmin, ymin, xmax, ymax);
            line(x1, y1, x2, y2);
            getch();
        }
        else
        {
            cleardevice();
            printf("\nLine is partially visible");
            rectangle(xmin, ymin, xmax, ymax);
            line(x1, y1, x2, y2);
            getch();

            // top and bottom intercept points
            // // y = ymin -- top 
            if ((start[2] == 0) && (start[3] == 1))
            {
                x1 = x1 + (ymin - y1) / m;
                y1 = ymin;
            }
            if ((end[2] == 0) && (end[3] == 1))
            {
                x2 = x2 + (ymin - y2) / m;
                y2 = ymin;
            }
            // // y = ymax -- bottom
            if ((start[2] == 1) && (start[3] == 0))
            {
                x1 = x1 + (ymax - y1) / m;
                y1 = ymax;
            }
            if ((end[2] == 1) && (end[3] == 0))
            {
                x2 = x2 + (ymax - y2) / m;
                y2 = ymax;
            }
            
            // left and right intercept points
            // // x = xmin -- left
            if ((start[1] == 0) && (start[0] == 1))
            {
                y1 = y1 + m * (xmin - x1);
                x1 = xmin;
            }
            if ((end[1] == 0) && (end[0] == 1))
            {
                y2 = y2 + m * (xmin - x2);
                x2 = xmin;
            }

            // // x = xmin -- right
            if ((start[1] == 1) && (start[0] == 0))
            {
                y1 = y1 + m * (xmax - x1);
                x1 = xmax;
            }
            if ((end[1] == 1) && (end[0] == 0))
            {
                y2 = y2 + m * (xmax - x2);
                x2 = xmax;
            }


            clrscr();
            cleardevice();
            printf("\nAfter clippling:");
            rectangle(xmin, ymin, xmax, ymax);
            line(x1, y1, x2, y2);
            getch();
        }
    }
    else
    {
        clrscr();
        cleardevice();
        printf("\nLine is invisible");
        rectangle(xmin, ymin, xmax, ymax);
    }
    getch();
    closegraph();
}