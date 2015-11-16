import java.util.*;
import java.applet.*;
import java.awt.*;
import java.awt.event.*;
/*
<html> 
<head>
</head>

 <body>
 <applet code = "MouseAction.java" width =300 height =300 ></applet>
</body>
 </html>
*/
public class MouseAction extends Applet implements MouseMotionListener {
	int x,y;
	public void init() {
		addMouseMotionListener(this);
		}
	public void paint(Graphics g) {
		g.drawString("(" + x + "," + y + ")",x,y);
		}
	public void mouseMoved(MouseEvent e) {
		x = e.getX();
		y = e.getY();
		repaint();
		}
	public void mouseDragged(MouseEvent e ) {
		}
	}
