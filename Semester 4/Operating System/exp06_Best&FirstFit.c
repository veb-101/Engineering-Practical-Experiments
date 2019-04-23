#include <stdio.h>

void insertionSort(int arr[])
{
   int i, key, j;
   for (i = 1; i < 5; i++)
   {
       key = arr[i];
       j = i-1;
       while (j >= 0 && arr[j] > key)
       {
           arr[j+1] = arr[j];
           j = j-1;
       }
       arr[j+1] = key;
   }
}
void memManage(int mem[], int allo[], int pro[], int num){
    int i, j;
    for(i=0;i<num;i++){
        for(j=0;j<5;j++){
            if(allo[j] == -1 && mem[j] >= pro[i]){
                printf("\n%d size allocated to %d", mem[j],pro[i]);
                allo[j] = 1;
                break;
            }
        }
    }
}

int main(){
    int mem[5], i, j, pro[5], allo[5], num, firstArray[5], firstAllo[5];
    printf("\nEnter memmory size(5):\n");
    for(i=0;i<5;i++){
        allo[i] = -1;
        firstAllo[i] = -1;
        scanf("%d", &mem[i]);
        firstArray[i] = mem[i];
    }

    printf("\nEnter number of processes: ");
    scanf("%d", &num);
    printf("\nEnter proces size:\n");
    for(i=0;i<num;i++)
        scanf("%d", &pro[i]);

    printf("For best fit...");
    insertionSort(mem);
    memManage(mem, allo, pro, num);
    printf("\nFor first fit...");
    memManage(firstArray, firstAllo, pro, num);
    printf("\nEnding Program...");

}
