
class SuperClass {
	int a,b;
	SuperClass(int a,int b){
		this.a	= a;
		this.b	= b;
		}
	}
class SubClass extends SuperClass {
	int c;
	SubClass(int a,int b){
		super(a,b);
		c	= 3;
		}
	}

class Demo {
	public static void main(String args[]) {
		SuperClass sub	= new SubClass(1,2);
		System.out.println( sub.a );
		/*
		 * 1. Accessing `sub.c` will be illegal here as superclass variable is referencing the subclass object.
		 * superclass may not have any idea about member that are added by subclass.
		 * 2. But in first line of creating an object. variable `c` will also be initialized but can't be accessed
		 * for the above reason.
		 * */
		//System.out.println( sub.c ); // raises compile-time error
		}
	}
