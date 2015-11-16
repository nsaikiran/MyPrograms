import java.util.*;

class ColorFont extends Applet {

	public void init(){
		Color c	= new Color(230,220,0);
		setBackground(c);
		}
	public void paint(Graphics g) {
		String str = " ";
		String FontList[];
		GraphicsEnvironment ge	= GraphicsEnvironment.getlocalGraphicsEnvironment();
		FontList	= ge.getAvailableFontFamilyName();
		for ( int var =0 
		}
