
interface A {
	void callme();
	}
interface B {
	void callme();
	}
class C implements A,B {

	public void callme(){}
	
	public static void main(String args[]){
		C c  = new C();
		c.callme();
		A a;
		B b;
		a= c;
		a.callme();
		b=c;
		b.callme();
		}
	}
// Finish it java complete reference 237
