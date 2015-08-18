package MyPack;
import java.util.Scanner;

public class Details {
	static String[] details;
	public Details(String[] list){
		details = list;
		}
	public void show() {
		for (int var=0;var<details.length;++var) {
			System.out.println(details[var]);
			}
		}
	}
