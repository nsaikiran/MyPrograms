
import java.util.Vector;
import java.util.Scanner;
class VectorDemo2{
	public static void main(String args[]){
		Scanner stdin = new Scanner(System.in);
		Vector<Integer> intList = new Vector<Integer>(2,4);
		
		intList.addElement(new Integer(1));
		intList.addElement(new Integer(2));
		intList.addElement(new Integer(3));

		System.out.println(intList.size());
		System.out.println(intList.capacity());
		//Use Enumeration to print all the elements	

		}
	
	}
