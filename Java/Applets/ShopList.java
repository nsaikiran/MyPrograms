import java.awt.*;
import java.applet.*;
import java.awt.event.*;

/*

<html>
<head></head>

<body> <applet code = ShopList.java height = 500 width = 400> </applet> </body>

</html>

*/


public class ShopList extends Applet implements ActionListener {
	List original,copy;
	
	public void init() {
		original = new List(5,false);// displays 5 elements with scrollbar for extra elements.
		copy = new List(10,false);
		populateList();
		
		add(original);
		add(copy);
		
		Button b1= new Button(">>>");
		add(b1);
		Button b2= new Button("clear");
		add(b2);
		
		b1.addActionListener(this);
		b2.addActionListener(this);
		}
		
	public void populateList() {
		original.add("Biscuts");
		original.add("Chocolates");
		original.add("vegetables");
		original.add("Books");
		original.add("Grossaries");
		original.add("Dresses");
		original.add("Shampoos");
		original.add("Soaps");
		}
		
	public void actionPerformed(ActionEvent e) {
		String str = e.getActionCommand();
		if (str.equals(">>>") && original.getSelectedIndex() >= 0 ) {
			copy.add(original.getSelectedItem());
			original.remove(original.getSelectedItem());
			}
		else if (str.equals("clear")) {
			original.removeAll();
			copy.removeAll();
			populateList();
			}
		repaint();
		}
	}
