#include <stdlib.h>
#include <stdio.h>
#include <string.h>

//Takes in two arguments: n is the number to be converted to binary, s is the desired bit length
//Converts the integer to binary format, and returns the value
//If a negative integer is given, returns the 2's compliment.
int decToBinary(int n, int s)
{
	int comp = 0;
	if (n < 0){
		n = -n;
		comp = 1;
	}
	
    // array to store binary number
    int binaryNum[s];
	int fin = 0b0;
    // counter for binary array
    int i = 0;
    while (n > 0) {
        // storing remainder in binary array
        binaryNum[i] = n % 2;
        n = n / 2;
        i++;
    }
	while(i < s){
		binaryNum[i] = 0;
		i++;
	}

    // printing binary array in reverse order
    for (int j = i - 1; j >= 0; j--){
		fin = fin << 1;
		if(comp == 1){
			int temp = binaryNum[j];
			if(temp == 0){
				fin = fin | 1;
			}else if(temp ==1){
				fin = fin | 0;
			}
		}else{
			fin = fin | binaryNum[j];
		}
	}
	if (comp == 1){
		fin = fin + 1;
		//printf("fin: %d\n", fin); //fin test
	}
	return fin;
}

int main(){
    //Take in ints from the cmd line, convert them o binary and output them to file


    int test1, test2, test3;
    test1 = rand() % 50;
    test2 = rand() % 50;
    test3 = rand() % 50;

    printf("%d in binary is: %d\n", test1, decToBinary(test1));
    printf("%d in binary is: %d\n", test2, decToBinary(test2));
    printf("%d in binary is: %d\n", test3, decToBinary(test3));

    //Use the cmd: xxd -b -c *output.dat file* to view binary breakdown

    return 0;
}