#include <stdio.h>
#include <stdlib.h>

//This basic program prints a list of 5 random numbers
int main(){
    for(int i=0; i< 5; i++){
        printf("%d: %d\n", i, rand());
    }
}