/*


<html>
<body>
<APPLET code=AppletDemo.java width=20 height=20>
</APPLET>
</body>
</html>

*/


import java.awt.*;
import java.applet.*;

public class AppletDemo extends Applet{
	public void paint(Graphics g){
		g.drawString("This is my first Applet program",20,20);
		showStatus("New status of Applet");
		//URL url ;
		}

	public void start(){
		System.out.println("Started :) ");
		}

	public void stop(){
		System.out.println("Stopped :( ");
		}

	public void destroy(){
		System.out.println("Destroyed .. :( ");	
		}

	public void init(){
		setBackground(Color.orange);
		setForeground(Color.white);
		}
	}

