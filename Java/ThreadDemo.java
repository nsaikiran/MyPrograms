
class Timer implements Runnable {
	int limit;	//Seconds
	Timer(int sec) {
		limit 	= sec;
		}

	void run(){
		try 	{
			System.out.println("Timer started");
			for ( int sec = 0; sec < limit; ++sec)
				System.out.println(sec);
			System.out.println("Timer stopped");
			}
		catch (InterruptedException exception) {
			exception.printStackTrace();
			}
		}
	
	}

class ThreadDemo {
	public static void main(String args[]){
		Timer stopwatch = new Timer(60); //Timer for a minute
		Thread clock 	= new Thread(stopwatch);
		clock.run();
		}
