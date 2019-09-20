#include<stdio.h>
int main()
{
	int a[100],n,temp,i,j;
	printf("Enter number of terms(should be less than 10): ");
	scanf("%d",&n);
	printf("Enter elements: ");
	for(i=0;i<n;i++)
	{
		scanf("%d",&a[i]);
	}
	for(i=1;i<n;i++)
	{
		temp = a[i];
		j=i-1;
		for(j=i-1; j>=0 && a[j] > temp;j--)
            a[j+1] = a[j];
        a[j+1] = temp;
	}
	printf("In ascending order: ");
	for(i=0; i<n; i++)
		printf("%d\t",a[i]);
    printf("\n");
    return 0;

}
