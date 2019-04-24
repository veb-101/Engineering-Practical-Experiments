#include <stdio.h>
#include <dirent.h>
#include <stdlib.h>
void main()
{
  char dirname[10];
  DIR *p;
  struct dirent *d;
  printf("Enter directory name: ");
  scanf("%s", dirname);
  p = opendir(dirname);
  if (p == NULL)
  {
    perror("Cannot find directory");
    exit(-1);
  }
  while (d = readdir(p))
    printf("%s\n", d->d_name);
}

/*
Program execution:
1) create a directory in the same folder as the program file
2) In the newly created directory, create any new file.

$ gcc exp04_lc.c -o exp4lc
$ ./exp4lc

*/
