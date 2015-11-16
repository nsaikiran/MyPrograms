interface A{
	void A1();
	void A2();
	}
interface B extends A{
	void B1();
	void B2();
	}
interface C{
	void C1();
	void C2();
	}

class InterfaceDemo implements B,C{
	public void A1(){
		System.out.println("It's A1");
		}
	public void A2(){
		System.out.println("It's A2");
		}
	public void B1(){
	System.out.println("It's B1");
		}
	public void B2(){	System.out.println("It's B2");
		}
	public void C1(){	System.out.println("It's C1");
		}
	public void C2(){	System.out.println("It's C2");
		}
	public static void main(String args[]){
		InterfaceDemo demo = new InterfaceDemo();
		demo.A1();
		demo.A2();
		demo.B1();
		demo.B2();
		demo.C1();
		demo.C2();
		}
	}
