import java.util.*;
import java.awt.*;
import java.applet.*;


/*
<html>
<head></>
<body>
<APPLET code=ColorFont.class width=20 height=20>
</APPLET>
</body>
</html>

*/

public class ColorFont extends Applet {

	public void init(){
		Color c	= new Color(230,220,0);
		setBackground(c);
		}
	public void paint(Graphics g) {
		String str = " ";
		String FontList[];
		GraphicsEnvironment ge	= GraphicsEnvironment.getLocalGraphicsEnvironment();
		FontList	= ge.getAvailableFontFamilyNames();
		for ( int i = 0; i < FontList.length;++i){
			g.drawString("Fonts Available Are ",5,30);
			str += FontList[i]+",";
			g.drawString(str,5,50);
			}
		Color c = new Color(255,50,50);
		g.setColor(c);
		g.drawString("Hello !",5,180);
		Font currF = new Font("TIMESROMAN",Font.PLAIN,20);
		g.setFont(currF);
		g.drawString("It is Me",5,200);
		currF = new Font("TIMESROMAN",Font.ITALIC,40);
		g.setFont(currF);
		g.drawString("Got it",5,240);
		}
	}
