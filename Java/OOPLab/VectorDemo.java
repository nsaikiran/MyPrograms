/*
Author:	saikiran638
Description:
	Vector is a part of Generic Types in Java much like C++'s STL.
	Here in this program we are not specifying type of Vector,
	Type will be determined by type inference.
	So, we may get a note or warning from the compiler.
*/
import java.util.*;

class VectorDemo{
	public static void main(String args[]) {
		Vector vec = new Vector(4,8);
		//No. of elements that are there in Vector
		System.out.println("size:"+vec.size());
		//No. of elements + No. of empty blocks
		System.out.println("capacity:"+vec.capacity());
		//Add an object
		vec.addElement(new Integer(3));
		//Add another object
		vec.addElement(new String("saikiran638"));
		//Add another object
		vec.addElement(new Float(2.356));
		vec.addElement(new Boolean(true));
		vec.addElement(new Character('F'));
		//Print first object
		System.out.println("First element:"+vec.firstElement());
		//Print last object
		System.out.println("Last element:"+vec.lastElement());

		Enumeration vEnum = vec.elements();
		System.out.println("\nElements in vector:");
		while(vEnum.hasMoreElements())
			System.out.print(vEnum.nextElement() + " ");
		System.out.println();

		System.out.println("size of vector:"+ vec.size() );
		System.out.println("capacity of vector:"+ vec.capacity() );
		}
	}
