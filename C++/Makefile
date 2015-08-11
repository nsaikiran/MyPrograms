#									\
This Makefile is for compiling all C++ programs in this directory.	\
You have to mention the name of the file to build it.			\
Whenever a new C++ program is added in this directory. This Makefile	\
needs change.


COMPILER = g++
CFLAGS	 = -Wall

.PHONY	  : dummy clean

#									\
We can expect some file with the name 'dummy' in future. Then the whole	\
rule will depend on the modifying time of the file. If that is 		\
up-to-date then the receipe won't get executed. Hence it is better to	\
categerise that target as PHONY. As we know PHONY targets are not 	\
compared with filenames.

dummy 	  :
	printf "Please provide the filename to build\n"

namespaces : namespaces.cpp
	$(COMPILER) $(CFLAGS) $^ -o $@

namespaces2: namespaces2.cpp
	$(COMPILER) $(CFLAGS) $^ -o $@

clean	  :
	rm namespaces namespaces2

#									\
We can build an executable if it depends on only C/C++ file. without	\
even writing a Makefile. Realized after writing Makefile. Just execute	\
"make filename" where filename.c or filename.cpp should be there in 	\
current working directory.

	
