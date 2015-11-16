
import java.util.*;
import java.awt.*;
import java.applet.*;
import java.awt.event.*;

/*
<html>

<body>
<applet code = AnonyDemo.java width=300 height=300>
</applet>
</body>

</html>

*/
public class AnonyDemo extends Applet {
	public void init() {
		addKeyListener(new KeyAdapter() {
			public void keyPressed(KeyEvent e ) {
				showStatus("Pressed");
				}
			public void keyReleased(KeyEvent e) {
				showStatus("Released");
				}
			} );
		}
	}
