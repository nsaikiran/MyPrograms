import java.awt.*;
import java.awt.event.*;

// No events are used in this program.

public class FlowLayoutDemo extends Frame {
	FlowLayoutDemo(){
		/* 	Didn't find any difference between FlowLayout.LEFT and FLowLayout.LEADING
		 *	and FlowLayout.RIGHT and FlowLayout.TRAILING	
		 */	
		setLayout(new FlowLayout(FlowLayout.LEFT));
		Button b = new Button("b1");
		Button b2= new Button("b2");
		Button b3= new Button("b3");
		add(b);
		add(b2);
		add(b3);
		
		setVisible(true);		//Use this for a frame
		setSize(400,500);		//size of the frame
		setTitle("Practice Programs");	//set Title
		addWindowListener( new WindowAdapter() { public void windowClosing(WindowEvent event) { System.exit(0);}} );
		}
	public static void main(String args[]) {
		new FlowLayoutDemo();
		}
	}
