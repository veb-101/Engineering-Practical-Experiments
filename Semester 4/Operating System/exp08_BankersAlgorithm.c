// credits: https://www.geeksforgeeks.org/operating-system-bankers-algorithm/
// Banker's Algorithm
#include <stdio.h>
int main()
{
    // P0, P1, P2, P3, P4 are the Process names here
    int n, m, i, j, k;
    n = 5;                         // Number of processes P0, P1, P2, P3, P4
    m = 3;                         // Number of resources A, B, C
    int alloc[5][3] = {{0, 1, 0},  // P0    // Allocation Matrix
                       {2, 0, 0},  // P1
                       {3, 0, 2},  // P2
                       {2, 1, 1},  // P3
                       {0, 0, 2}}; // P4

    int max[5][3] = {{7, 5, 3},  // P0    // MAX Matrix
                     {3, 2, 2},  // P1
                     {9, 0, 2},  // P2
                     {2, 2, 2},  // P3
                     {4, 3, 3}}; // P4

    int avail[3] = {3, 3, 2}; // Available Resources
    int need[n][m];
    int y = 0;
    int flag = 0;
    int f[n], ans[n], ind = 0;

    // n: number of processes
    // m: no. of resources for each process

    // to indicate is the process has been finished and added to the safe sequence
    // f = {0, 0, 0, 0, 0}
    for (k = 0; k < n; k++)
    {
        f[k] = 0;
    }

    // calculating need matrix
    for (i = 0; i < n; i++)
    {
        for (j = 0; j < m; j++)
            need[i][j] = max[i][j] - alloc[i][j];
    }

    // for (i = 0; i < n; i++)
    // {
    //     for (j = 0; j < m; j++)
    //         printf("%d ", need[i][j]);
    //     printf("\n");
    // }

    // main loop

    for (k = 0; k < n; k++)
    {
        for (i = 0; i < n; i++)
        { // 0, 1
            if (f[i] == 0)
            {
                int flag = 0;
                // printf("i: %d\n", i);
                for (j = 0; j < m; j++)
                {
                    // printf("j: %d\n", j);
                    if (need[i][j] > avail[j])
                    {
                        flag = 1;
                        break;
                    }
                    // printf("\n\n\\\");
                }

                if (flag == 0)
                {
                    // printf("In here..\n");
                    ans[ind++] = i;
                    for (y = 0; y < m; y++)
                        avail[y] += alloc[i][y];
                    f[i] = 1;
                }
            }
        }
    }

    printf("Following is the SAFE Sequence\n");
    for (i = 0; i < n - 1; i++)
        printf(" P%d ->", ans[i]);
    printf(" P%d", ans[n - 1]);

    return (0);
}
