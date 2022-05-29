#include <stdio.h>
#include <pthread.h>
#include <stdlib.h>
#include <stdbool.h>
#include <assert.h>
#include <stdint.h>

#define BIG 100000000L

uint64_t sum=0;
pthread_mutex_t thelock = PTHREAD_MUTEX_INITIALIZER;


void count_to_big() {
	for (int i=0; i < BIG; i++) {
		pthread_mutex_lock(&thelock);
		sum += i;
		pthread_mutex_unlock(&thelock);
	}
}

void * threadfunc(void *arg) {
	count_to_big();
	return NULL;
}

int main(int argc, char **argv)
{
	pthread_t t1, t2;
	pthread_create(&t1, NULL, threadfunc,NULL);
	pthread_create(&t2, NULL, threadfunc,NULL);
	

	pthread_join(t1, NULL);
	pthread_join(t2, NULL);
	
	printf("The result is %lu\n", sum);
	return 0;
}
