// bubble sort using C and inline assembly
#include <stdio.h>
#include <conio.h>

void main()
{
    int array[10], n, i, j, a, b;

    printf("Enter array size: ");
    scanf("%d", &n);

    for (i = 0; i < n; i++)
    {
        printf("\nEnter array element %d: ", i + 1);
        scanf("%d", &array[i]);
    }

    printf("\nBefore Sorting Array: ");
    for (i = 0; i < n; i++)
        printf("%d ", array[i]);

    for (i = 0; i < n - 1; i++)
    {
        for (j = 0; j < n - i - 1; j++)
        {
            a = array[j];
            b = array[j + 1];

            asm mov ax, a;
            asm mov bx, b;
            asm cmp ax, bx;
            asm jg l1;
            asm jmp l2;

        l1:
            _asm {
                xchg ax, bx;
                mov a, ax;
                mov b, bx;
            }
            array[j] = a;
            array[j + 1] = b;
        l2:
            printf("");
        }
    }

    printf("\nSorted Array: ");
    for (i = 0; i < n; i++)
        printf("%d ", array[i]);
    printf("\nEnd");
    getch();
}

// // https://github.com/mish24/Assembly-step-by-step/blob/master/Bubble-sort.asm
