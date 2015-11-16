
/*
Author: saikiran638
Description: To demonstrate instance,static variables and functions
*/

class Car {
	//class variable
	private static int count = 0;
	//instance variable
	private int serial;
	Car(){
		//one car is created
		Car.count++;
		//set serial number
		serial	= Car.count;
		}
	int serial(){
		return serial;
		}
	static int count(){
		return count;
		}
	static void reset(int c){
		count 	= c;
		}
	}

class Manufacturer {
	String name;
	// Max 10 cars
	private static Car cars[] = new Car[10];
	Manufacturer(String name){
		this.name = name;
		}
	void manufacture(){
		cars[0]	= new Car();
		cars[1]	= new Car();
		System.out.println("Cars manufactured : "+Car.count());
		cars[2]	= new Car();
		}
	static void statistics(){
		// Here cars.length = 10. But we didn't fill all of them
		for (int var = 0; var < cars.length;++var)
			if ( cars[var] != null )
				System.out.println(cars[var].serial());
		}
	}
/*Driver class*/
class Demo {
	public static void main(String[] args){
		Manufacturer company;
		if ( args.length != 0 )
			company = new Manufacturer(args[0]);
		else	company = new Manufacturer("TATA");
		company.manufacture();
		company.statistics();
		}
	}
