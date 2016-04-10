CC = g++
OBJS = hello.o helloWrap.o

hello.so: $(OBJS)
	$(CC) -fPIC -Wall -shared -o hello.so $(OBJS)

hello.o: hello.cpp
	$(CC) -fPIC -Wall -c -o hello.o hello.cpp

helloWrap.o: helloWrap.cpp
	$(CC) -fPIC -Wall -c -o helloWrap.o helloWrap.cpp
