/*
1.	We can't call a constructor from a method. 
	But we can call a method from Constructor (it is not recommended).
2.	We can call one constructor from another and
	the call should be the first one in calling constructor.
*/

import java.util.Scanner;

class Box {
	double width;
	double height;
	double length;

	Box(double l,double w,double h){
		width = w;
		height = h;
		length = l;
		}

	Box(double len){
		width = length = height = len;
		}

	double volume(){
		return width*height*length;
		}
	/*Method overloading section starts */
	void set(double len,double h){
		// length = breadth = len
		length = width = len;
		height = h;
		}

	void set(double len){
		width = length = height = len;
		}

	void set(double l,double w,double h){
		length = l;
		width = w;
		height = h;
		}
	
	public static void main(String args[]){
		//Constructor Overloading
		/*
		Box cube 	= new Box(4);
		Box box 	= new Box(5,3,2);
		System.out.println(cube.volume());
		System.out.println(box.volume());
		*/
		//Method overloading
		Box box = new Box(4);
		System.out.println(box.volume());
		box.set(5,3,2);
		System.out.println(box.volume());
		box.set(2,4);
		System.out.println(box.volume());
		}
	}

