import java.awt.*;
import java.applet.*;

/*
<html> <body> <applet code=FlowLayoutDemo.java height=400 width = 400 ></applet> </body></html>
*/

public class FlowLayoutDemo extends Applet {
	LayoutManager flowlayout;
	Button [] Buttons;
	public FlowLayoutDemo(){
		int i;
		flowlayout = new FlowLayout();
		setLayout(flowlayout);
		Buttons = new Button[6];
		for (i=0;i<6;++i){
			Buttons[i] = new Button();
			Buttons[i].setLabel("Button"+(i+1) );
			add(Buttons[i]);	
			}
		}
	}
