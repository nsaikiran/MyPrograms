/*
Author	: saikiran638
Description	: WrapperClasses Demo.
*/

import java.util.*;

public class WrapperClassDemo {
	public static float simpleInterest( Float p,Float r,Integer t){
		float principle	= p.floatValue();
		float rate  	= r.floatValue();
		int time	= t.intValue();
		float interest	= ( principle * rate * time) / 100.0f;
		return interest;
		}

	public static void main(String args[]) {
		Scanner stdin 	= new Scanner(System.in);
		System.out.println("Priciple Amount >> ");
		float p		= stdin.nextFloat();
		System.out.println("Time >>");
		int t 		= stdin.nextInt();
		System.out.println("Rate >>");
		float r		= stdin.nextFloat();
		Integer time	= new Integer(t);
		Float rate	= new Float(r);
		Float principle	= new Float(p);
		System.out.println("Interest = "+ simpleInterest(principle,rate,time));
		}
	}
