# This make file is to compile the Java programs in this directory.	|
# It has to be edited as soon as a new program added.			|

.PHONY : clean 

MyPack : Details.java
	javac -d . $^

Usepack.class : Usepack.java
	javac $^
clean : 
	rm *.class
