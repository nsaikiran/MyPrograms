import java.net.*;
import java.awt.*;
import java.applet.*;

/*
<html>
<body>
<applet code = "MediaTrackerDemo.java" width = 2000 height = 2000>
</applet>
</body>
</html>
*/

public class MediaTrackerDemo extends Applet implements Runnable {

	Image[] imgarr = null;
	MediaTracker m = null;
	int current = 0;
	Thread t = null;
	
	public void init() {
		m = new MediaTracker(this);
		imgarr = new Image[2];
		imgarr[0] = getImage( getDocumentBase(),"1.jpg" );
		m.addImage(imgarr[0],0);
		imgarr[1] = getImage( getDocumentBase(), "2.jpeg");
		m.addImage(imgarr[1],1);
		t = new Thread(this);
		t.start();
		}
	
	public void paint(Graphics g) {
		g.setColor(Color.white);
		g.fillRect(0,0,400,400);
		g.setColor(Color.black);
		if ( m.checkAll() ) { // Check whether all items are loaded.
			g.drawImage( imgarr[ current++ ] ,0,0,this);
			if ( current >= imgarr.length)
				current = 0;
			}
		else {
			g.drawString("Images loading",20,20);
			}
		}
	
	public void run() {
		try {
			m.waitForAll();
			for (;;){
				repaint();
				Thread.sleep(2000);
				}
			}
		catch(InterruptedException e) {}
		}
	}
