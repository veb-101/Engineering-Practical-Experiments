#include <ctype.h>
#include <stdio.h>
#define SIZE 50
char s[SIZE];
int top = -1;

void push(char elem)
{
    s[++top] = elem;
}

char pop()
{
    return (s[top--]);
}

int pr(char elem)
{
    int ret;
    switch (elem)
    {
    case '#':
        ret = 0;
        break;
    case '(':
        ret = 1;
        break;
    case '+':
    case '-':
        ret = 2;
        break;
    case '*':
    case '/':
        ret = 3;
        break;
    }
    return ret;
}

int main()
{
    char infix[50], postfix[50], ch, elem;
    int i = 0, k = 0;
    printf("\n\nEnter Infix Expression : ");
    scanf("%s", infix);
    push('#');
    while ((ch = infix[i++]) != '\0')
    {
        if (ch == '(')
            push(ch);
        else if (isalnum(ch))
            postfix[k++] = ch;
        else if (ch == ')')
        {
            while (s[top] != '(')
                postfix[k++] = pop();
            elem = pop();
        }
        else
        {
            while (pr(s[top]) >= pr(ch))
                postfix[k++] = pop();
            push(ch);
        }
    }
    while (s[top] != '#')
        postfix[k++] = pop();
    postfix[k] = '\0';
    printf("\nPostfix Expression =  %s\n", postfix);
    return 0;
}
