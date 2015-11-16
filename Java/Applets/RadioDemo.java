import java.awt.*;
import java.awt.event.*;
import java.util.*;
import java.applet.*;

/*

<html>
<head> </head>

<body>
<applet code = RadioDemo.java width = 400 height = 400 > </applet>
</body>

</html>

*/

public class RadioDemo extends Applet implements ItemListener {
	Checkbox red,green,blue;
	CheckboxGroup cbg;
	
	public void init() {
		/*
		Creating group of checkbox.
		*/
		cbg = new CheckboxGroup();
		red = new Checkbox("red",cbg,false);
		blue = new Checkbox("blue",cbg,false);
		green = new Checkbox("green",cbg,false);
		
		add(red);
		add(green);
		add(blue);
		
		red.addItemListener(this);
		green.addItemListener(this);
		blue.addItemListener(this);
		}
		
	public void itemStateChanged( ItemEvent e ) {
		String str = (String) e.getItem();
		if (str.equals ( "red") )
			setBackground(Color.red);
		else if (str.equals( "blue" ) )
			setBackground(Color.blue);
		else
			setBackground(Color.green);
		
		repaint();
		}
	
	}
