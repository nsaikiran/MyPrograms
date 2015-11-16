import java.awt.*;
import java.awt.event.*;
import java.util.*;
import java.applet.*;

/*
<html>

<body>
<applet code = "CheckBoxDemo.class" height =200 width = 200 ></applet>
</body>

</html>
*/

public class CheckBoxDemo extends Applet implements ActionListener {
	Button submit;
	Checkbox 	name1,
				name2,
				name3;
				
	public void init() {
		name1 = new Checkbox("Sai Kiran",null,false);
		name2 = new Checkbox("Naresh",null,false);
		name3 = new Checkbox("Bobby",null,false);
		
		submit = new Button("submit");
		
		add(name1);
		add(name2);
		add(name3);
		
		add(submit);
		submit.addActionListener(this);
		}
		
	public void paint(Graphics g) {
		if (name1.getState())
			g.drawString("Sai Kiran",50,100);
		if (name2.getState())
			g.drawString("Naresh",50,120);
		if (name3.getState()) 
			g.drawString("Bobby",50,140);
		}
		
	public void actionPerformed(ActionEvent e ) {
		String str = e.getActionCommand();
		if (str.equals("submit")) {
			repaint();
			}
		}
	}
