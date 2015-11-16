import java.awt.*;
import java.awt.event.*;
import java.util.*;
import java.applet.*;

/*
<html>

<body>
<applet code = "ButtonDemo.class" height =200 width = 200 ></applet>
</body>

</html>
*/

public class ButtonDemo extends Applet implements ActionListener {
	Button red,blue,green;
	public void init() {
		red = new Button("Red");
		blue= new Button("Blue");
		green=new Button("Green");
		
		add(red);
		add(blue);
		add(green);
		
		red.addActionListener(this);
		blue.addActionListener(this);
		green.addActionListener(this);
		}
	public void actionPerformed(ActionEvent e ) {
		String str = e.getActionCommand();
		if (str.equals("Red")) {
			setBackground(Color.red);
			}
		else if (str.equals("Blue"))
			setBackground(Color.blue);
		else
			setBackground(Color.green);
		repaint();
		}
	}
