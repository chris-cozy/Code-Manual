CC = gcc
CFLAGS = -Wall -g
BINS= test.out shim.so

all: $(BINS)

%.so: %.c
	$(CC) $(CFLAGS) -shared -fPIC -o $@ $^ -ldl

%.out: %.c
	$(CC) $(CFLAGS) -o $@ $^

clean:
	rm -f $(BINS)