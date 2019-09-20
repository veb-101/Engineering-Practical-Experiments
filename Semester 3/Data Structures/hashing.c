#include <stdio.h>
#include <stdlib.h>

int a[10], j = 0, i = 0, c = 0, found = 0;

void insert(int x)
{
        j = (x + i) % 10;
        do
        {
                if (a[j] != 0)
                {
                        found = 1;
                        c++;
                        i++;
                        j = (x + i) % 10;
                }
                else
                {
                        found = 0;
                        i = 0;
                        a[j] = x;
                }
        } while (found == 1);
}

void main()
{
        int x, o, n, k;
        for (k = 0; k < 10; k++)
                a[k] = 0;
        do
        {
                printf("MENU\nEnter the option\n1. INSERT\n2. DISPLAY\n0. Exit\n");
                scanf("%d", &o);
                switch (o)
                {
                case 1:
                        printf("Enter the no. of element\n");
                        scanf("%d", &n);
                        for (k = 0; k < n; k++)
                        {
                                printf("Enter the element\n");
                                scanf("%d", &x);
                                insert(x);
                        }
                        break;

                case 2:
                        printf("Index\t\t||\t\tElement\n");
                        printf("________________||_____________________\n");
                        for (k = 0; k < 10; k++)
                        {
                                if (a[k] == 0)
                                        continue;
                                else
                                        printf("   %d\t\t||\t\t   %d\n", k, a[k]);
                        }
                        printf("No. of Collisions are: %d\n", c);
                        break;

                case 0:
                        exit(0);
                default:
                        printf("Wrong option\n");
                        break;
                }
        } while (o != 0);
}
