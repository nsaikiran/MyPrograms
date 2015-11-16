package MyPack;

import java.lang.System;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.BufferedReader;

public class MyInputReader{
	BufferedReader stdin=new BufferedReader(new InputStreamReader(System.in));
	public static void main(String args[]){
		System.out.println("Hello");
		}
	public char ch() throws IOException {
		return (char)stdin.read();
		}
	public String str() throws IOException {
		return stdin.readLine();
		}
	public int Int() throws IOException {
		return Integer.parseInt(stdin.readLine());
		}
	protected void finalize(){
		System.out.println("Deleting object");
		}
	}
