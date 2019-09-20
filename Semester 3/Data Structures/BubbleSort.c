#include <stdio.h>
int main()
{
    int data[100],i,n,j,temp;
    printf("Enter the number of elements to be sorted: ");
    scanf("%d",&n);
    printf("Enter Elements:\n" );
    for(i=0;i<n;++i)
        scanf("%d",&data[i]);

    for(i=1;i<n;i++){
        for(j=0;j<n-i;j++){
            if(data[j] > data[j+1]){
                temp = data[j];
                data[j] = data[j+1];
                data[j+1] = temp;
            }
        }
    }
    for(i=0;i<n;++i)
         printf("%d  ",data[i]);
    return 0;
}
