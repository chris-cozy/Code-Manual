#include <stdio.h>
#include <pthread.h>
#include <stdlib.h>
#include <unistd.h>
#include <stdbool.h>

#define BIG 2000000000L

unsigned long counter = 0;

//do something CPU-bound
void count_to_big()
{
	printf("Counting rapidly...\n");
	for (long i=0; i < BIG; i++)
	{ counter++;}
	printf("Counting rapidly...done\n");
}

//do something
void do_something_really_slow()
{
	for (int i=0; i < 10; i++)
	{
		printf("Counting slowly...%d\n",i);
		sleep(1);
		
	}
}

void *tfunc(void *param)
{
	//pthread_setcancelstate(PTHREAD_CANCEL_DISABLE, NULL);
	do_something_really_slow();
	return NULL;
}

int main(int argc, char **argv)
{
	pthread_t t1, t2;
	pthread_create(&t1, NULL, tfunc, NULL);
	pthread_create(&t2, NULL, tfunc, NULL);
	count_to_big();

	pthread_cancel(t1);
	pthread_cancel(t2);

	pthread_join(t1, NULL);
	pthread_join(t2, NULL);

	printf("\nCounter=%lu\n",counter);
	return 0;
}
