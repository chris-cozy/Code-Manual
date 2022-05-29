//Library for the shim

//Needed for shims
#define GNU_SOURCE

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <dlfcn.h>

//Replacement for rand function - can be whatever you like
int rand()
{
    //Calls the original rand function
    //Declaring a function pointer that looks like rand, then using dlsym to intialize it to point to the original rand function 
    //dlsym can get a pointer to a function in a library at runtime
        //Rather than specifying the library, this time we are using a special psuedohandle as the argument
        //RTLD_NEXT says: don't give me the first occurence, give me the next one.
        //We don't want the first because ours has become the first at runtime\
        //Adding -ldl to makefile makes sure dlsym will be linked with the shim
    int (*original_rand)(void) = dlsym(RTLD_NEXT, "rand");
    //Now will return a random number between 0 and 99
    return original_rand() % 100;
}

