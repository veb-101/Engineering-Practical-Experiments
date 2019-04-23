#include <stdio.h>

int main()
{
    int burst_time[20], process[20], wait_time[20], turnaround_time[20], i, j, n, total = 0, pos, temp;
    float avg_wait_time = 0, avg_turnaround_time = 0;
    printf("Enter number of process:");
    scanf("%d", &n);

    printf("\nEnter Burst Time:\n");
    for (i = 0; i < n; i++)
    {
        printf("p%d:", i + 1);
        scanf("%d", &burst_time[i]);
        process[i] = i + 1; //contains process number
    }
    //sorting burst time in ascending order using selection sort
    for (i = 0; i < n; i++)
    {
        pos = i;
        for (j = i + 1; j < n; j++)
        {
            if (burst_time[j] < burst_time[pos])
                pos = j;
        }

        temp = burst_time[i];
        burst_time[i] = burst_time[pos];
        burst_time[pos] = temp;

        temp = process[i];
        process[i] = process[pos];
        process[pos] = temp;
    }

    for (i = 0; i < n; i++)
    {
        wait_time[i] = total;
        total = total + burst_time[i];
        turnaround_time[i] = burst_time[i] + wait_time[i];
        avg_wait_time += wait_time[i];
        avg_turnaround_time += turnaround_time[i];
    }
    printf("Process|  Burst Time  |  Waiting time  |  TurnAround Time\n");
    for (i = 0; i < n; i++)
    {
        printf("%d\t\t\t%d\t\t\t%d\t\t\t%d\n", process[i], burst_time[i], wait_time[i], turnaround_time[i]);
    }
    printf("Avg Waiting time:: %.3f\n", avg_wait_time / n);
    printf("Avg TurnAround time:: %.3f\n", avg_turnaround_time / n);
}

/*
Program execution:
$ gcc exp05_SJF.c -o expsjf
$ ./expsjf
*/