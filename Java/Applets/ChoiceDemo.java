
import java.applet.*;
import java.awt.*;
import java.awt.event.*;

/*

<html>
<head></head>

<body>
<applet code = ChoiceDemo.java width = 400 height = 400 > </applet>
</body>
</html>

*/

public class ChoiceDemo extends Applet implements ItemListener {
	String CurrentCols=" ";// current selected
	Choice theoptions;

	public void init () {
		theoptions = new Choice(); // create choice list
		theoptions.add("none");//add
		theoptions.add("red");
		theoptions.add("green");
		theoptions.add("blue");
		
		theoptions.addItemListener(this);
		add(theoptions);
		}
		
	public void itemStateChanged ( ItemEvent e ) {
		CurrentCols = theoptions.getSelectedItem();
		repaint();// repaint will call paint
		}
	public void paint( Graphics g ) {
		if ( CurrentCols.equals( "red" ) )
			setBackground(Color.red);
		else if ( CurrentCols.equals("green") ) 
			setBackground(Color.green);
		else if ( CurrentCols.equals("blue") )
			setBackground(Color.blue);
		else 
			setBackground(Color.white);
		}	
	}
