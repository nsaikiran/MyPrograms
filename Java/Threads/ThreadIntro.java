
class MyThread extends Thread {
	int id;
	MyThread(int num) {
		id = num;
		}
	public void run() {
		try {
			System.out.println("I'm Thread : "+id );
			for ( int var=0;var<10;++var){
				System.out.println(id +":"+ var);
				Thread.sleep(2000);//wait for a second
				}
			}
		catch ( InterruptedException exception) {
			exception.printStackTrace();
			}
		}
	}

class Tester {
	public static void main(String args[]){
		MyThread t1 = new MyThread(1);
		MyThread t2 = new MyThread(2);
		t1.run();
		t2.run();
		System.out.println("Done");
		}
	}
