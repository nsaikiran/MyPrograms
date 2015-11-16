import java.awt.*;
import java.awt.event.*;

public class ScrollbarDemo extends Frame implements AdjustmentListener{
	int x,y;
	Label l;
	Scrollbar hs,vs;
	
	public ScrollbarDemo(){
		hs = new Scrollbar(Scrollbar.HORIZONTAL);
		vs = new Scrollbar(Scrollbar.VERTICAL);
		
		x=100;
		y=100;
		
		l = new Label("Default");
		hs.setMaximum(400);
		vs.setMaximum(400);
		
		setTitle("Title");
		setLayout(new BorderLayout());
		add(l,BorderLayout.NORTH);
		add(hs,BorderLayout.SOUTH);
		add(vs,BorderLayout.EAST);
		
		hs.addAdjustmentListener(this);
		vs.addAdjustmentListener(this);
		
		hs.setValue(x);
		vs.setValue(y);
		
		l.setText("HScroll = "+hs.getValue()+"VScroll = "+vs.getValue() );
		setSize(400,500);
		
		setVisible(true);
		
		addWindowListener(new WindowAdapter() { public void windowClosing(WindowEvent e) { System.exit(0) ; } } );
		}
		
	public void adjustmentValueChanged(AdjustmentEvent e){
		x = hs.getValue();
		y=vs.getValue();
		
		l.setText("HScroll = "+hs.getValue()+"VScroll = "+vs.getValue() );
		repaint();
		}
	
	public void paint(Graphics g){
		g.drawOval(50,100,x,y);
		}
	
	public static void main(String args[]) {
		ScrollbarDemo d = new ScrollbarDemo();
		}
	}
	
