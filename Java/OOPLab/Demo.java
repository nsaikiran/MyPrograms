/*
Author: saikiran638
Description: 
	This program demonstrate operations on String objects
	No object has been created for user-defined classes.
*/

class StringDemo{
	private static String str1,str2;
	public static void set( String str1,String str2 ) {
		//String object is created in String Constant Pool
		StringDemo.str1 = str1;
		// String object is created
		StringDemo.str2 = new String(str2);
		}
	public static void show() {
		System.out.println( str1 == str2 );
		System.out.println( str1.equals(str2) );
		System.out.println( str2.length() );
		System.out.println( str1.concat(str2) );
		System.out.println( str1.compareTo(str2) );
		System.out.println( str2.charAt(0) );
		System.out.println( str1.startsWith( "sai" ));
		System.out.println( str2.endsWith( "638" ) );
		System.out.println( str1.indexOf( "kiran" ) );

		set("saikiran638","SAIKIRAN638");

		System.out.println( str1.equals( str2 ) );
		System.out.println( str1.equalsIgnoreCase( str2 ) );
		System.out.println( str1.compareTo( str2 ) );
		System.out.println( str2.compareToIgnoreCase ( str1 ) );
		System.out.println( str2.toLowerCase() );
		System.out.println( str1.toUpperCase() );
		System.out.println( str1.substring(0,8) );
		
		// Split using a delimeter
		String[] strs = str1.split( "i" );
		for ( int index = 0 ; index < strs.length ; ++index )
			System.out.println( strs[index] );
		
		// Changing contents of a string
		char[] chars = new char[ str1.length() ];
	 	str1.getChars(0,str1.length(), chars, 0 );
		System.out.println (chars);
		chars[8] ='1';
		chars[9] ='2';
		chars[10] = '3';
		
		set ( new String( chars ) , "saikiran" );
		System.out.println( str1 );
		
		//Trim the string
		set("  saikiran638  ","saikiran");

		System.out.println( str1.trim() );
	
		}
	}

public class Demo {
	public static void main( String args[] ) {
		StringDemo.set ( "saikiran638","saikiran638" );
		StringDemo.show();
		}
	}
