import java.awt.*;


public class FrameDemo extends Frame {
	public FrameDemo(String title) {
		super(title);
		}
	
	public static void main(String args[]) {
		FrameDemo fd = new FrameDemo ( "FrameTitle" );
		fd.setSize(200,300);
		fd.setVisible(true);
		}
	}
