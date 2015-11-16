import java.util.*;
import java.applet.*;
import java.awt.*;

/*

<html>
<body>
<APPLET code=FMDemo.class width=20 height=20>
</APPLET>
</body>
</html>

*/
public class FMDemo extends Applet {
	public void init() {
		Color c = new Color(255,255,0);
		setBackground(c);
		}
	public void paint(Graphics g){
		int fontsize = 20;
		g.setFont(new Font("TIMESROMAN",Font.PLAIN,fontsize));
		FontMetrics fm = g.getFontMetrics();
		String s = "It's my applet";
		int sw= fm.stringWidth(s);
		int w = 300;
		int h = 300;
		int x = (w-sw)/2;
		int baseLine = (fm.getAscent()+fm.getDescent());

		int ascent = fm.getAscent();
		int descent = fm.getDescent();
		int fontHeight = ascent+descent;
		int front = ascent + descent;
		g.setColor(Color.pink);
		g.fillRect(x,baseLine-ascent,sw,fontHeight);
		g.setColor(Color.black);
		g.drawLine(x,baseLine-ascent,x+sw,baseLine+descent);
		g.setColor(Color.blue);
		g.drawLine(x,baseLine-ascent,x+sw,baseLine+descent);
		g.setColor(Color.green);
		g.drawString(s,x,baseLine);
		}
	}
