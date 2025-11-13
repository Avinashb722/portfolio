CC=gcc
CFLAGS=-Wall -Wextra -std=c99
TARGET=robot
SOURCES=line_following_robot.c

all: $(TARGET)

$(TARGET): $(SOURCES)
	$(CC) $(CFLAGS) -o $(TARGET) $(SOURCES)

clean:
	rm -f $(TARGET) *.o

.PHONY: all clean