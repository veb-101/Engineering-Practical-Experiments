#include<iostream.h>
#include<conio.h>

void main() {
    int num, shift, end_result;
    clrscr();
    cout << "Enter a number: ";
    cin >> num;
    cout << "\nEnter number of bits to shift: ";
    cin >> shift;

    asm mov ax, num
    asm mov cx, shift
    asm shl ax, cl
    asm mov end_result, ax
    cout << "\nLEFT SHIFT: Before: "<<num << " After: "<<end_result<<"\n";

    asm mov ax, num
    asm mov cx, shift
    asm shr ax, cl
    asm mov end_result, ax
    cout << "RIGHT SHIFT: Before: "<<num << ", After: "<<end_result;

    getch();
}
