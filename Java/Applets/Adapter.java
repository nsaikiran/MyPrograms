// Not working
import java.util.*;
import java.awt.*;
import java.awt.event.*;

class Demo extends MouseMotionAdapter {
	MouseMotionEvent m ;
	Demo(MouseMotionEvent m){
		this.m = m;
		}
	public void init(){
		addMouseMotionListener(new Demo(this));
		}
	public void paint(Graphics g){
		g.drawString("("+x+","+y")"x,y);
		}
	public void mouseMoved(MouseEvent e ) {
		m.x = e.getX();
		m.y = e.getY();
		m.repaint();
		}
	}
