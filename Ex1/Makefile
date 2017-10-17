# This is a Makefile, it tells the `make` utility what to do.  If this is
# unfamiliar, check out http://makefiletutorial.com/

# These are variables: they are valid on my computer, but they may not be valid
# on yours.
#
# You can:
# - Change the makefile after you download it
# - specify makefile commands when asking `make` to run a "target" (like
#   "runstreams").  For example, if your file downloading utility is `foo`,
#   calling `make stream.c WGET=foo` should work.
#
CC = cc
CFLAGS = -O10
N = 2000000
RM = rm -f
WGET = wget

# recipe for downloading the stream benchmark (stream.c is the target)
stream.c:
	$(WGET) https://www.cs.virginia.edu/stream/FTP/Code/stream.c $<

# recipe for running the stream benchmark (the "target" isn't actually the
# creation of a file, it's just to perform a task.  When this is the case, it
# is a ".PHONY" target, which we specify below)
runstream: stream.c
	$(CC) $(CFLAGS) -DSTREAM_ARRAY_SIZE=$(N) -DOFFSET=43 -o stream stream.c
	./stream

# recipe for cleaning up the directory
clean:
	$(RM) stream stream.c

.PHONY: runstream clean

