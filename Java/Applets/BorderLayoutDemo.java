import java.awt.*;


public class BorderLayoutDemo extends Frame {
	public BorderLayoutDemo(String title) {
		super(title);
		add(new Button("NORTH"),BorderLayout.NORTH);
		add(new Button("SOUTH"),BorderLayout.SOUTH);
		add(new Button("EAST"),BorderLayout.EAST);
		add(new Button("WEST"),BorderLayout.WEST);
		add(new Button("CENTER"),BorderLayout.CENTER);
		setSize(400,270);
		setVisible(true);
		}

	public static void main(String args[]) {
		BorderLayoutDemo bl = new BorderLayoutDemo("DEMO"); 
		}
	}
