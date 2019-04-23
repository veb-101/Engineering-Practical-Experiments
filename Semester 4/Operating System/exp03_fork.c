#include <sys/types.h>
#include <stdio.h>

// https://www.geeksforgeeks.org/fork-system-call/
void main()
{
    int pid = fork();
    printf("PID: %d\n", pid);
    if (pid == 0)
    {
        printf("This is child process.\n");
        printf("Child pid: %d", getpid());
        execvp("\nbin/ls", NULL);
        // http://www.csl.mtu.edu/cs4411.ck/www/NOTES/process/fork/exec.html
    }
    else
    {
        wait();
        printf("\nThis is parent.");
        printf("\nParent PID: %d", getpid());
        printf("\nChild PID: %d\n", pid);
    }
}

/*
Program execution steps:

$ gcc exp03_fork.c -o exp3
<<ignore warnings>>
$ ./exp3
*/