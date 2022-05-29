/*****************************************************************************
 Excerpt from "Linux Programmer's Guide - Chapter 6"
 (C)opyright 1994-1995, Scott Burkett

 Slightly modified by Jacob Sorber
 *****************************************************************************/

#include <stdio.h>
#include <stdlib.h>
#include <sys/stat.h>
#include <unistd.h>

#include <sys/stat.h>

//Temp file to recieve data from
#define FIFO_FILE "/tmp/myfifo"

int main(void) {
  FILE *fp;
  char readbuf[80];

  /* Create the FIFO if it does not exist */
  umask(0);
  mkfifo(FIFO_FILE, 0666);

  while (1) {
    fp = fopen(FIFO_FILE, "r");
    fgets(readbuf, 80, fp);
    printf("Received string: %s\n", readbuf);
    fclose(fp);
  }

  return (0);
}