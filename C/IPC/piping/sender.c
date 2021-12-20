/*****************************************************************************
 Excerpt from "Linux Programmer's Guide - Chapter 6"
 (C)opyright 1994-1995, Scott Burkett

 Slightly modified by Jacob Sorber
 *****************************************************************************/

#include <stdio.h>
#include <stdlib.h>

//Temp file to send data through
#define FIFO_FILE "/tmp/myfifo"

int main(int argc, char *argv[]) {
  FILE *fp;

  if (argc != 2) {
    printf("USAGE: %s [string]\n", argv[0]);
    exit(1);
  }

  if ((fp = fopen(FIFO_FILE, "w")) == NULL) {
    perror("fopen");
    exit(1);
  }

//This example writes the second argument to the file
  fputs(argv[1], fp);

  fclose(fp);
  return (0);
}
