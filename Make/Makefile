#										\
This is a simple makefile that demonstrate the usage of the GNU make.		\
In this we are going to 'make' a text file from other two text files.		\
Here finaldoc.txt is our target that depends on doc1.txt and doc2.txt		\
If any of the pre-requisites are modified the target ( finaldoc.txt ) has to be	\
modified.									\
										\
Here we have used some automatic variables ( $^= first pre-requisite,$@ = target\
$^ = list of all pre-requisites. )



finaldoc.txt : doc1.txt doc2.txt
	cat $^ > $@

# The target that are 'not' up-to-date are called PHONY targets. We can use	\
Them explicitely . More about make and its usage is available in C in a Nutshell\
and make.pdf


.PHONY : view

view:
	less finaldoc.txt
	
