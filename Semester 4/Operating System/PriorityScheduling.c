#include<stdio.h>

int main()
{
    int burst_time[20],process_id[20],wait_time[20],turn_around_time[20],priority[20],i,j,n,total=0,pos,temp;
    float avg_waiting_time,avg_turn_around_time;
    printf("Enter Total Number of Process: ");
    scanf("%d",&n);
 
    printf("\nEnter Burst Time and Priority\n");
    for(i=0;i<n;i++)
    {
        printf("\nProcess [%d]-->\n",i+1);
        printf("Burst Time: ");
        scanf("%d",&burst_time[i]);
        printf("Priority: ");
        scanf("%d",&priority[i]);
        process_id[i]=i+1;           //contains process number
    }
 
    //sorting burst time, priority and process number in ascending order using selection sort
    for(i=0;i<n;i++)
    {
        pos=i;
        for(j=i+1;j<n;j++)
        {
            if(priority[j]<priority[pos])
                pos=j;
        }
 
        temp=priority[i];
        priority[i]=priority[pos];
        priority[pos]=temp;
 
        temp=burst_time[i];
        burst_time[i]=burst_time[pos];
        burst_time[pos]=temp;
 
        temp=process_id[i];
        process_id[i]=process_id[pos];
        process_id[pos]=temp;
    }
 
    wait_time[0]=0;    //waiting time for first process is zero
 
    //calculate waiting time
    for(i=1;i<n;i++)
    {
        wait_time[i]=0;
        for(j=0;j<i;j++)
            wait_time[i]+=burst_time[j];
 
        total+=wait_time[i];
    }
 
    avg_waiting_time=total/n;      //average waiting time
    total=0;
 
    printf("\nProcess\t    Burst Time    \tWaiting Time\tTurnaround Time");
    for(i=0;i<n;i++)
    {
        turn_around_time[i]=burst_time[i]+wait_time[i];     //calculate turnaround time
        total+=turn_around_time[i];
        printf("\nP[%d]\t\t    %d\t\t         %d\t\t\t\t%d\n",process_id[i],burst_time[i],wait_time[i],turn_around_time[i]);
    }
 
    avg_turn_around_time=total/n;     //average turnaround time
    printf("\n\nAverage Waiting Time = %.2f ms",avg_waiting_time);
    printf("\nAverage Turnaround Time = %.2f ms\n",avg_turn_around_time);
    printf("Done");
 
    return 0;
}