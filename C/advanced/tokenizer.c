#include <stdlib.h>
#include <stdio.h>
#include <string.h>

//Tokenizes the string
/*
	strtok() - destroys the string that its parsing
	Keeps a pointer to a position that it's at to 'save progress'
	Can only tokenize one message at a time, 
	so if you call it in one thread for msg1 then call it in another thread for msg2 before msg1 is finished, 
	the next time the first thread calls strtok it will return the next token from msg2
*/
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