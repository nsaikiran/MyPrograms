
package calendar;

public class Year{
	private static int days[] = {0,31,28,31,30,31,30,31,31,30,31,30,31};
	public static boolean isleap(int year){
		return (year%4 == 0 && (year%100 !=0 || year%400==0));
		}
	public static int[] monthDays(int year){
		if ( isleap(year) )
			days[2] = 29;	//If leap.
		return days;
		}
	}
