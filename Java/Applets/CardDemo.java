/*
innerclass
inheritance
polymorphism
exception handling
applet basics
2 programs : 
*/

import java.awt.*;
import java.awt.event.*;

public class CardDemo extends Frame implements ActionListener {
	Panel CardP;
	Panel p1,p2,p3;
	Panel buttonp;
	Button b1,b2,b3;
	CardLayout clay;
	
	public CardDemo() {
		CardP = new Panel();
		clay = new CardLayout();
		CardP.setLayout(clay);
		p1 = new Panel();
		p1.setBackground(Color.red);
		p2= new Panel();
		p2.setBackground(Color.green);
		p3 = new Panel();
		p3.setBackground(Color.blue);		

		b1 = new Button("red");
		b2 = new Button("blue");
		b3 = new Button("green");
		
		b1.addActionListener(this);
		b2.addActionListener(this);
		b3.addActionListener(this);
		
		buttonp = new Panel();
		buttonp.add(b1);
		buttonp.add(b2);
		buttonp.add(b3);
		
		CardP.add(p1,"b1");
		CardP.add(p2,"b2");
		CardP.add(p3,"b3");
		
		setLayout(new BorderLayout());
		add(buttonp,BorderLayout.SOUTH);
		add(CardP,BorderLayout.CENTER);
		setVisible(true);
		setSize(300,400);
		setTitle("Deomo");

		addWindowListener(new WindowAdapter() { public void windowClosing(WindowEvent e) { System.exit(0) ; } } );
		}
		
	public void actionPerformed(ActionEvent e) {
		if (e.getSource() == b1 )
			clay.show(CardP,"b1");
		if (e.getSource() == b2)
			clay.show(CardP,"b2");
		if (e.getSource() == b3 )
			clay.show(CardP,"b3");
		}
		
	public static void main(String args[]) {
		CardDemo c= new CardDemo();
		}
	}
