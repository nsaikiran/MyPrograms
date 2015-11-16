import java.lang.System;
import java.util.Scanner;

class UseMe{
	UseMe(){
		Scanner stdin = new Scanner(System.in);
		int a=stdin.nextInt();
		System.out.print(a);
		}
	public static void main(String args[]){
		System.out.println("Hello");
		UseMe a = new UseMe();
		System.out.println(a);
		}
	}
