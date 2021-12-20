#include <sys/types.h>
#include <sys/mman.h>
#include <err.h>
#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/wait.h>

#define BLOCKSIZE 4096

int main(void)
{
        char *sharedblock;

        char *mystring = "Hi, I'm Jacob.";

        //map a block of 4K that will be shared between
        //child and
        //parent after fork()
        sharedblock = (char*)mmap(NULL, BLOCKSIZE,
                PROT_READ|PROT_WRITE, MAP_ANON|MAP_SHARED,
                -1, 0);

        if (sharedblock == MAP_FAILED)
                errx(1, "mmap error");

        //copy some text into the shared block.
        strcpy(sharedblock, mystring);

        //allocate some non-shared memory on the heap.
        int * testptr = malloc(sizeof(int));
        *testptr = 43;

        if (fork() == 0)
        {
                //child
                printf("shared: %s\n",sharedblock);
                printf("private: %s\n",mystring);

                mystring = "Foo!";
                *testptr = 11;
                printf("the int is %d (%p)\n",*testptr, testptr);
                strcpy(sharedblock, mystring);
        } else {
                //parent
                wait(NULL);
                printf("the int is %d (%p)\n",*testptr, testptr);
                printf("parent shared: %s\n",sharedblock);
                printf("parent private: %s\n",mystring);
                munmap(sharedblock, 4096);
        }

        return 0;
}
