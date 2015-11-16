import java.awt.*;
import java.awt.event.*;
import java.applet.*;



/*
<html>
<head></head>

<body> <applet code = TextFieldDemo.java width = 400 height = 600 > </applet> </body>
</html>

*/


public class TextFieldDemo extends Applet implements TextListener,ActionListener,FocusListener {
	Label l;
	Button b;
	TextField tf;
	
	public void init() {
		tf = new TextField ("Text");
		l = new Label("Make selection");
		b= new Button("submit");
		
		b.addFocusListener(this);
		tf.addFocusListener(this);
		tf.addTextListener(this);
		
		tf.addActionListener(this);
		tf.selectAll();
		setLayout( new BorderLayout());
		add(l,BorderLayout.NORTH);
		add(tf,BorderLayout.CENTER);
		add(b,BorderLayout.SOUTH);
		}
		
	public void textValueChanged(TextEvent e) {
		l.setText( "This is boss" );
		}
		
	public void focusGained(FocusEvent e ) {
		if (e.getSource() == tf)
			l.setText("Foucus is on text");
		else if (e.getSource() == b)
			l.setText("Focus is on button");
		}
		
	public void focusLost(FocusEvent e ) {
		l.setText("Focus is not on window");
		}
		
	public void actionPerformed(ActionEvent e ) {
		l.setText("ActionEvent");
		}
	}
