#include<iostream.h>
#include<conio.h>

void main() {
    int a, b, c;
    clrscr();
    cout << "Enter two numbers: \n";
    cin >>a>>b;
    asm mov ax, a
    asm mov cx, b
    asm add ax, cx
    asm mov c, ax
    cout<<"Result: " <<c;
    getch();
}
