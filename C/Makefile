# \
	This is my introductory Makefile 			\
	This file shows basic usage of make 			\
	This make file is for all C programs in this directory	\
	Ref : make.pdf 						\



#\
	Don't use first character of target line as tab or .RECIPEPREFIX	\
	If you add tab or .RECIPEPREFIX at the begining of any line other than recipe 	\
	the line will be considered as receipe other than a line specifying target and dependencies	\
DEFAULT =  gcc $^ -o $@

.PHONY : fake clean

fake :
	printf "Please specify the program name\n"

pointers: pointers.c
	# Comments written in recipe are passed on to the shell 
	gcc $^ -o $@

buffering : buffering.c	
	gcc $^ -o $@

signal : signal.c
	gcc $^ -o $@

stdin : stdin.c
	gcc $^ -o $@

clean :
	rm pointers buffering
