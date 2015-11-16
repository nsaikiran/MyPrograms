import java.awt.*;
import java.applet.*;

/*
<html>
<body>
<applet code = "AppletDemo2.java" width = 200 height = 200 >
<param name="your name" value = "saivenkatesh">
<param name="your profession" value = "Wipro">
<param name="your age" value = 21>
</applet>
</body>

</html>
*/

public class AppletDemo2 extends Applet {
	String name ,profession;
	int age=2;
	public void start(){
		String str;
		name = getParameter("your name");
		if (name == null) 
			name = "not found ";
		str = getParameter("your profession");
		if (str!=null) 
			profession = str;
		else
			profession = "No job";
		str = getParameter("your age");
		try {
			age = Integer.parseInt(str);
		}
		catch (NumberFormatException e) {}

	}
	public void paint(Graphics g){
		g.drawString("your name "+name,20,10);
		g.drawString("your profession is "+profession,20,30);
		g.drawString("your age is "+age,20,50);
		}
	}

/*
URL url;
String str;
str = "Code base " + url.toString();
g.drawString(str,20,40);
url = getDocumentBase();
str = "Document Base : "+ url.toString();
g.drawString(str,20,40); 
*/
