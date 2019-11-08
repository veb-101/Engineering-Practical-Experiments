// factorial of a number using C and inline assembly
#include <stdio.h>
#include <conio.h>

void main()
{
    int number, i, fact = 1;

    clrscr();
    printf("Enter number: ");
    scanf("%d", &number);

    asm mov ax, fact; // initialize 1 in ax

    asm mov cx, number; // mov number in counter

t1:             // loop
    asm mul cx; // multiply ax with content of cx => ax = ax * cx
    asm dec cx; // decrement counter value
    asm jnz t1; // loop back if number not zero

    asm mov number, ax; // mov content of ax in number
    printf("Factorial is = %d", number);
    getch();
}