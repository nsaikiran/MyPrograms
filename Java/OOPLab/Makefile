.PHONY : clean dummy

COMPILER = javac
OPT	 = -d .

dummy :
	echo "Please specify program "
VectorDemo.class : Vector.java
	$(COMPILER) $^
Demo.class: Demo.java
	$(COMPILER) $^

clean : 
	rm *.class
