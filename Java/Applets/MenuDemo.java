/*
Menus can be used only in Frame, not in applets.
Menu()
Menu(String label)
	add(MenuItem m) //particular menuitem
	add(String label) // item adding
	deleteShortCut(MenuShortcut m) 
	getItemCount()
	getItem(int index)
	removeAll()
MenuBar()
	add(Menu m)
	remove(int index)

MenuItem()
MenuItem(String label)
MenuItem(String label,MenuShortcut s)
MenuShortcut()
STEPS TO ADD A MENU IN MENUBAR
setMenuBar()
Menu fmenu = new Menu("menu")
MenuItem n = new MenuItem("File");
n.addActionListener()
*/

import java.awt.*;
import java.awt.event.*;

public class MenuDemo extends Frame implements ActionListener {
	Label l;
	public void mDemo(){
		setTitle("MenuDemo");
		setSize(250,150);
		setVisible(true);
		
		MenuBar mb = new MenuBar();
		setMenuBar(mb);
		
		MenuShortcut n = new MenuShortcut(KeyEvent.VK_N);
		MenuShortcut x = new MenuShortcut(KeyEvent.VK_X);
		MenuShortcut o = new MenuShortcut(KeyEvent.VK_O);
		
		Menu file = new Menu ("file");
		Menu edit = new Menu ("edit");
		
		MenuItem nLabel = new MenuItem("New",n);
		MenuItem oLabel = new MenuItem("Open",o);
		MenuItem xLabel = new MenuItem("Exit",x); 
		
		file.addSeparator();
		file.add(nLabel);
		file.addSeparator();
		file.add(oLabel);
		file.addSeparator();
		file.add(xLabel);
		file.addSeparator();
		
		
		nLabel.addActionListener(this);
		oLabel.addActionListener(this);
		xLabel.addActionListener(this);
		
		MenuItem nLabel1 = new MenuItem("Cut");
		MenuItem oLabel1 = new MenuItem("Copy");
		MenuItem xLabel1 = new MenuItem("Paste"); 
		
		edit.addSeparator();
		edit.add(nLabel1);
		edit.addSeparator();
		edit.add(oLabel1);
		edit.addSeparator();
		edit.add(xLabel1);
		
		nLabel1.addActionListener(this);
		oLabel1.addActionListener(this);
		xLabel1.addActionListener(this);
		
		mb.add(file);
		mb.add(edit);
		
		addWindowListener(new WindowAdapter() { public void windowClosing(WindowEvent e) { System.exit(0) ; } } );
		
		l = new Label();
		l.setText("None");
		add(l);
		}
		
	public void actionPerformed(ActionEvent e){
		String action = e.getActionCommand();
		if ( action.equals("New") )
				l.setText("New");
		else if ( action.equals ("Open"))
				l.setText("Open");
		else if ( action.equals ("Exit"))
				l.setText("Exit");
		else if ( action.equals ("Cut"))
				l.setText("Cut");
		else if ( action.equals ("Copy"))
				l.setText("Copy");
		else if ( action.equals ("Paste"))
				l.setText("Paste");
		repaint();
		}
	
	public static void main(String args[]) {
		MenuDemo m = new MenuDemo();
		m.mDemo();
		}
	}
