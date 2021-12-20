#include <stdio.h>
#include <stdlib.h>

int hexTobin(char* hexdec)
{
 
    long int i = 0;
    int bin = 0b0;
    int char = 0b0;
 
    while (hexdec[i]) {
 
        switch (hexdec[i]) {
        case '0':
            char = 0b0000;
            break;
        case '1':
            char = 0b0001;
            break;
        case '2':
            char = 0b0010;
            break;
        case '3':
            char = 0b0011;
            break;
        case '4':
            char = 0b0100;
            break;
        case '5':
            char = 0b0101;
            break;
        case '6':
            char = 0b0110;
            break;
        case '7':
            char = 0b0111;
            break;
        case '8':
            char = 0b1000;
            break;
        case '9':
            char = 0b1001;
            break;
        case 'A':
        case 'a':
            char = 0b1010;
            break;
        case 'B':
        case 'b':
            char = 0b1011;
            break;
        case 'C':
        case 'c':
            char = 0b1100;
            break;
        case 'D':
        case 'd':
            char = 0b1101;
            break;
        case 'E':
        case 'e':
            char = 0b1110;
            break;
        case 'F':
        case 'f':
            char = 0b1111;
            break;
        default:
            printf("\nInvalid hexadecimal digit %c",
                   hexdec[i]);
        }
        bin = bin << 4;
        bin = bin | char;
        i++;
    }
    return bin;
}

int main()
{
    return 0;
}