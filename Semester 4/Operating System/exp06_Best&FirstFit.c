#include <stdio.h>

void selectionSort(int mem[])
{
    int i, j, temp, pos;
    for (i = 0; i < 5; i++)
    {
        pos = i;
        for (j = i + 1; j < 5; j++)
        {
            if (mem[j] < mem[pos])
                pos = j;
        }
        if (i != pos)
        {
            temp = mem[i];
            mem[i] = mem[pos];
            mem[pos] = temp;
        }
    }
}

void memManage(int mem[], int allo[], int pro[], int num)
{
    int i, j;
    for (i = 0; i < num; i++) // run for number of processes
    {
        for (j = 0; j < 5; j++) // traverse through all the memmory space for each process
        {
            if (allo[j] == -1 && mem[j] >= pro[i])
            {
                printf("\nMemory size: %d  allocated to process: %d", mem[j], pro[i]);
                allo[j] = 1;
                break;
            }
        }
    }
}

int main()
{
    int mem[5], i, j, pro[5], allo[5], num, firstArray[5], firstAllo[5];
    printf("\nEnter memmory size(5):\n");
    for (i = 0; i < 5; i++)
    {
        allo[i] = -1;
        firstAllo[i] = -1;
        printf("Memory %d size: ", i + 1);
        scanf("%d", &mem[i]);
        firstArray[i] = mem[i];
    }

    printf("\nEnter number of processes: ");
    scanf("%d", &num);
    printf("\nEnter proces size:\n");
    for (i = 0; i < num; i++)
    {
        printf("Process %d size: ", i + 1);
        scanf("%d", &pro[i]);
    }
    selectionSort(mem);

    for (i = 0; i < 5; i++)
        printf("%d ", mem[i]);
    printf("\nFor best fit...");
    memManage(mem, allo, pro, num);
    printf("\nFor first fit...");
    memManage(firstArray, firstAllo, pro, num);
    printf("\nEnding Program...");
}
