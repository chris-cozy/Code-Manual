#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <netdb.h>

#define PORTNUM 6001
#define QUEUE_LENGTH 5
#define BUFLEN 512

int main()
{
	int sockfd, connfd, port, clilen;
	struct sockaddr_in saddr, caddr;

	char buffer[BUFLEN];

	sockfd = socket(AF_INET, SOCK_STREAM, 0);
	if (sockfd < 0)
	{
		perror("Could not create socket.");
		exit(1);
	}

	memset(&saddr, 0, sizeof(struct sockaddr_in));
	port = PORTNUM;
	saddr.sin_family = AF_INET;
	saddr.sin_addr.s_addr = INADDR_ANY;
	saddr.sin_port = htons(port);

	if (bind(sockfd, 
		(struct sockaddr*)&saddr, 
		sizeof(saddr)) < 0) {
		perror("bind failed!");
		exit(1);
	} 

	listen(sockfd, QUEUE_LENGTH);

	clilen = sizeof(caddr);

	//accept a new client connection
	connfd = accept(sockfd,
				(struct sockaddr*)&caddr, 
				(socklen_t*)&clilen);

	if (connfd < 0)
	{
		perror("accept FAILED!");
		exit(1);
	}

	//zero out the buffer
	memset(buffer, 0, BUFLEN);

	int n = read(connfd, buffer, BUFLEN-1);

	if (n < 0) {
		perror("read FAILED.");
		exit(1);
	}

	printf("MSG: %s\n",buffer);

	n = write(connfd, "Hello Client!", 13);
	
	if (n < 0) {
		perror("write FAILED.");
		exit(1);
	}

	close(connfd);

	return 0;
}