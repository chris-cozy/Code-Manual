#include <stdlib.h>
#include <stdio.h>
#include <string.h>

//Tokenizes the string
void token(char str[], char delim[]){
	char *ptr = strtok(str, delim);
	while(ptr != NULL)
	{
		printf("%s\n", ptr);
		ptr = strtok(NULL, delim);
	}
	return;
}

int main()
{
    char s[256];
    char delim[] = " ";
    strcpy(s, "one two three");

    token(s, delim);

    return 0;
}