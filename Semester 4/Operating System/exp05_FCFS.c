#include<stdio.h>
int main()
{
 int n,i,burst_time[50],wait_time[10],turnaround_time[10],t=0;
 float avgw=0,avgt=0;
 printf("Enter No. of process::");
 scanf("%d",&n);
 for(i=0;i<n;i++)
 {
  printf("Burst Time of %d process::",i+1);
  scanf("%d",&burst_time[i]);
 }
 for(i=0;i<n;i++)
 {
  wait_time[i]=t;
  t=t+burst_time[i];
  turnaround_time[i]=burst_time[i]+wait_time[i];
  avgw+= wait_time[i];
  avgt+= turnaround_time[i];
 }
 printf("Process|  Burst Time  |  Waiting time  |  TurnAround Time\n");
 for(i=0;i<n;i++)
 {
  printf("%d\t\t%d\t\t%d\t\t%d\n",i+1,burst_time[i],wait_time[i],turnaround_time[i]);
 }
 printf("Avg Waiting time:: %.3f\n",avgw/n);
 printf("Avg TurnAround time::%.3f\n",avgt/n);
 return 0;
}
