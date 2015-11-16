import calendar.Year;
import java.util.Scanner;

class Day{
	public static Scanner stdin = new Scanner(System.in);
	private static int dd,mm,yyyy,days[];

	private static void nextDay(){
		int dd=Day.dd,mm=Day.mm,yyyy=Day.yyyy;
		if ( dd == days[mm] ) {
			if ( mm == 12 ) {
				yyyy++;
				dd = 1;
				mm=1;
				}
			else {
				mm++;
				dd = 1;
				}
			}
		else 
			dd++;
		System.out.println(dd+"-"+mm+"-"+yyyy);
		}

	private static void prevDay(){
		int dd=Day.dd,mm=Day.mm,yyyy=Day.yyyy;
		if ( dd == 1) {
			if (mm==1){
				mm = 12;
				yyyy--;
				dd=days[mm];
				}
			else {
				mm--;
				dd = days[mm];
				}
			}
		else dd--;
			System.out.println(dd+"-"+mm+"-"+yyyy);
		}

	public static void main(String args[]) {
		dd 	= stdin.nextInt();
		mm 	= stdin.nextInt();
		yyyy	= stdin.nextInt();
		days	= Year.monthDays(yyyy);
		prevDay();
		nextDay();
		}
	}
