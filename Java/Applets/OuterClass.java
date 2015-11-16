import java.util.*;
import java.awt.*;
import java.awt.event.*;
import java.applet.*;
/*
<html>

<body>
<applet code = OuterClass.java width = 300 height = 300 > </applet>
</body>
</html>
*/

public class OuterClass extends Applet {
	public void init(){
		addKeyListener(new InnerClass());
		}
	
	class InnerClass extends KeyAdapter {
		public void keyPressed(KeyEvent e ) {
			showStatus( "Key pressed");
			}
		public void keyReleased(KeyEvent e ){
			showStatus("keyReleased");
			}
		}
		
	}
