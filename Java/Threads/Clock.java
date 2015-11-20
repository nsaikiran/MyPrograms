import java.util.*;

class Time extends Thread {
	public void run() {
		try {
			for (int i=0;i<60;++i){
				System.out.println(new Date());
				Time.sleep(1000);
				}
			}
		catch(InterruptedException e ){
			e.printStackTrace();
			}
		}
	public static void main(String args[]) {
		new Time().start();
		}
	}
