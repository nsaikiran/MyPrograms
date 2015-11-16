// Grid Layout. We can design the container.
import java.awt.*;
import java.awt.event.*;

public class GridDemo extends Frame{
	public GridDemo () {
		super("Layout components using GridDemo");
		Panel p = new Panel ( new GridLayout(5,2,20,50));
		p.add(new Label("Name"));
		p.add(new TextField(5));
		
		p.add(new Label("Roll"));
		p.add(new TextField(5));
		
		p.add(new Label("class"));
		p.add(new TextField(5));
		
		p.add(new Label("marks"));
		p.add(new TextField(5));
		
		p.add(new Button("submit"));
		p.add(new Button("Clear"));
		
		add(p);
		
		setSize(400,400);//size of frame.
		
		setVisible(true);
		
		addWindowListener(new WindowAdapter() { public void windowClosing(WindowEvent e) { System.exit(0) ; } } );
		}
		
	public static void main(String args[]){
		GridDemo g= new GridDemo();
		}
	}
	
/*
We will create an action for Buttons in this program(submit and clear).
We will try to validiate and store them in a database. By extracting the data from fields.
*/
