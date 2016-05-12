
class A {
	A()	{ System.out.println("A");}
	}
class B extends A {
	B()	{ System.out.println("B");}
	B(int a){ System.out.println("B2");}
	}
class C extends B {
	// Observe the change in keeping and removing `super(2)`
	C()	{ super(2);System.out.println("C");}
	}

class Demo2 {
	public static void main(String args[]) {
		new C();
		}
	}
/* constructor's first statement would be a call to SUPER class constructor.
 * Even if we have placed it or not it will be there. If place that will
 * be called or java uses parameter less constructor of its super class.*/
