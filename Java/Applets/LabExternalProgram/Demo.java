import java.awt.*;
import java.awt.event.*;
import java.applet.*;



/*
<html>
	<body>
		<applet code=Demo.java height=500 width=500> </applet>
	</body>
</html>
*/


public class Demo extends Applet implements MouseMotionListener {

	boolean laugh = false;
	public void init() {
		addMouseMotionListener(this);
		repaint();
		}
	public void paint(Graphics g){
	
		g.setColor(Color.red);//cap filling color
		int a[] = {121,150,175},b[]={110,70,110};//cap
		g.fillPolygon(a,b,3);
		g.setColor(Color.black);
		g.drawOval(100,100,100,100);//main
		g.drawOval(90,130,10,20); // left ear
		g.drawOval(200,130,10,20);//right ear
		
		g.drawOval(165,130,15,10);//right eye
		g.fillOval(170,132,5,5);//right eye ball
		
		g.drawOval(121,130,15,10);//left eye
		g.fillOval(126,132,5,5);//left eye ball
		
		g.setColor(Color.green);
		g.fillOval(140,140,20,15);//nose
		//g.drawLine(100,100,200,200);
		
		g.setColor(Color.black);
		//g.drawArc(300,300,50,10,180,180);
		if (laugh) {
			g.setColor(Color.white);
			//g.fillArc(120,170,60,15,180,180);//mouth
			//g.fillArc(120,170,60,15,180,180);//mouth
			g.fillOval(170,132,5,5);//right eye ball
			g.fillOval(126,132,5,5);//left eye ball
			g.fillArc(125,170,50,10,180,180);
			}
		else {
			g.drawArc(125,170,50,10,180,180);//mouth
			//g.drawArc(120,170,60,15,180,180);//mouth
			}
		g.setColor(Color.red);
		
		//int a[] = {0,10,20},b[]={30,0,30};
		//int a[] = {121,135,165},b[]={125,110,125};
		/*int a[] = {121,140,165},b[]={110,70,110};
		g.fillPolygon(a,b,3);*/
		//g.fillOval(350,150,40,40);
		}
		
	public void mouseMoved(MouseEvent me){
		int x,y;
		x=me.getX();
		y=me.getY();
		if (( x>=140 && x<=160) && ( y>=140 && y<=160) )
			laugh = true;
		else laugh =false;
		repaint();
		}
	public void mouseDragged(MouseEvent md) {
	
		} 
	}
