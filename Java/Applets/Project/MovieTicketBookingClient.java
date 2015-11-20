import java.awt.*;
import java.awt.event.*;
import java.applet.*;
import java.sql.*;
import java.applet.*;
import java.util.*;
/*
<html>

	<head>
	</head>
	
	<body> 
		<applet code="MovieTicketBookingClient.class" height=500 width=500> 
		</applet> 
	</body>
	
</html>
*/


public class MovieTicketBookingClient extends Applet implements ActionListener, FocusListener,ItemListener {
	
	Panel topPanel 		= new Panel(new BorderLayout());
	Panel centerPanel	= new Panel(new FlowLayout());
	Panel bottomPanel	= new Panel();//not used
	
	Panel buttonsPanel	= new Panel(new FlowLayout(FlowLayout.TRAILING));
	Label title			= new Label("Movie Ticket Booking System",Label.CENTER);
	
	Button homeButton	= new Button("Home");
	Button loginButton	= new Button("Login");
	Button signupButton	= new Button("Register");
	Button theatreButton	= new Button("Theatre Staff");
	
	Panel userInput		= new Panel(new GridLayout(4,1));
	Panel dummy			= new Panel(new BorderLayout());
	
	Panel phnoPanel		= new Panel(new GridLayout());
	Panel passwdPanel	= new Panel(new GridLayout());
	Panel namePanel		= new Panel(new GridLayout());
	Panel buttons		= new Panel(new GridLayout());
	
	Panel seatPanel		= new Panel(new GridLayout(2,1));

	TextField phno		= new TextField(/*"Phone no."*/"",20);
	TextField passwd	= new TextField(/*"Password"*/"",20);
	TextField name		= new TextField(/*"Name"*/"",20);

	Button clearButton	= new Button("Clear");
	Button submitButton	= new Button("Submit");
	
	Label introduction	= new Label(" This software helps you book your favorite movie ticket ",Label.CENTER);
	
	int registerState	= 1;
	int loginState		= 2;
	int theatreLogin	= 3;
	int theatreRegister	= 4;
	
	int state			= 0;
	
	int x,y;

	Choice rows		= new Choice();
	Choice cols		= new Choice();
	Choice location	= new Choice();
	Choice movieChoice=new Choice();
	Choice theatreChoice=new Choice();
	Choice showChoice=new Choice();
	
	TextField movieName = new TextField("",20);
	Choice cost	= new Choice();
	
	String currentUser;
	String currentTheatre;
	
	Button bookthese = new Button("Done");
	Seats seatsobj;
	public Connection con;
	public Statement st;
	public ResultSet rs;
	
	public void DBConnect()
	{
		try{
			Class.forName("com.mysql.jdbc.Driver");		
			con = DriverManager.getConnection("jdbc:mysql://localhost:3306/MovieTicket","root","saikiran");
			st = con.createStatement();
			System.out.println("hello world");
		}
		catch(Exception ex){
			System.out.println("Error"+ex);			
		}
	}
	 
	public void init()	{
		DBConnect();
		setLayout(new BorderLayout());
		
		seatsobj = new Seats();
		
		x=4;
		y=4;

		title.setFont(new Font("Serif",Font.BOLD,20));
		introduction.setFont(new Font("Serif",Font.PLAIN,15));
		
		//Add buttons to buttonPanel
		buttonsPanel.add(homeButton);
		buttonsPanel.add(loginButton);
		buttonsPanel.add(signupButton);
		buttonsPanel.add(theatreButton);
		
		//Fill topPanel
		topPanel.add(buttonsPanel,BorderLayout.NORTH);
		topPanel.add(title,BorderLayout.SOUTH);
		topPanel.setBackground(Color.white);
		
		
		namePanel.add(new Label("Name:",Label.LEFT));
		namePanel.add(name);
		
		phnoPanel.add(new Label("Phone No:",Label.LEFT));
		phnoPanel.add(phno);
		
		passwdPanel.add(new Label("Password:",Label.LEFT));
		passwd.setEchoChar('*');
		passwdPanel.add(passwd);
		
		buttons.add(clearButton);
		buttons.add(submitButton);
		
		//Add to input field
		userInput.add(namePanel);
		userInput.add(phnoPanel);
		userInput.add(passwdPanel);
		userInput.add(buttons);
		

		
		dummy.add(introduction,BorderLayout.NORTH);
		//dummy.add(userInput,BorderLayout.CENTER);
		

		centerPanel.add(dummy);
		//centerPanel.remove(userInput);	
		
		//Add action listener to these buttons
		homeButton.addActionListener(this);
		loginButton.addActionListener(this);	
		signupButton.addActionListener(this);
		theatreButton.addActionListener(this);
		
		bookthese.addActionListener(this);
		
		name.addFocusListener(this);
		passwd.addFocusListener(this);
		phno.addFocusListener(this);

		clearButton.addActionListener(this);
		submitButton.addActionListener(this);
		
		movieChoice.addItemListener(this);
		theatreChoice.addItemListener(this);
		showChoice.addItemListener(this);
		
		showChoice.add("Morning Show");
		showChoice.add("Matinee Show");
		showChoice.add("First Show");
		showChoice.add("Second Show");
		
		rows.add("4");
		rows.add("5");
		rows.add("6");
		cols.add("4");
		cols.add("5");
		cols.add("6");
		
		cost.add("50");
		cost.add("75");
		cost.add("150");

		location.add("Vijayawada");
		location.add("Nuzvid");
		
		rows.addItemListener(this);
		cols.addItemListener(this);

		add(topPanel,BorderLayout.NORTH);
		add(centerPanel,BorderLayout.CENTER);
		add(bottomPanel,BorderLayout.SOUTH);
		

		//userInput.setVisible(false);
		}
	
	public void itemStateChanged(ItemEvent event){
		
		if (event.getSource() == movieChoice){
			theatreChoice.removeAll();
			String movie = movieChoice.getSelectedItem();
			try {
				rs=st.executeQuery("select theatre from  movies where movie='"+movie+"'");
				String s;
				while(rs.next()){
					s=rs.getString("theatre");
					theatreChoice.add(s);
				}
				validate();
			}
			catch(Exception e){}
		}
		else if (event.getSource() == theatreChoice){
			showChoice.setVisible(true);
			validate();
		}
		
		else if (event.getSource() == showChoice){
			String movie = movieChoice.getSelectedItem();
			String theatre = theatreChoice.getSelectedItem();
			String show = showChoice.getSelectedItem();
			String showtable="";
			if (show.equals("Morning Show"))		showtable = "morningshow";
			else if ( show.equals("Matinee Show")) 	showtable = "matineeshow";
			else if ( show.equals("First Show"))	showtable = "firstshow";
			else if ( show.equals("Second Show"))	showtable = "secondshow";
			
			seatPanel.removeAll();
			
			try {
				rs=st.executeQuery("select rows,cols from theatre where name='"+theatre+"'");
				int r=0,c=0;
			//	System.out.println(rs.next());
				while (rs.next()){
					r =Integer.parseInt(rs.getString("rows"));
					c =Integer.parseInt(rs.getString("cols"));
				}
				System.out.println(r+" "+c);
				
				//seatPanel = new Panel(new GridLayout(2,1));
				
				Panel p = new Panel(new GridLayout(r,c));
				Button t;
				int sum=0;
				for (int i=0;i<r;++i)
					for (int j=0;j<c;++j){
						++sum;
						t=new Button( ((Integer)sum).toString());
						t.addActionListener(seatsobj);
						p.add(t);
						}
				try {
					rs=st.executeQuery("select seat from "+showtable+" where theatre='"+theatre+"'");
					while (rs.next()){
						//System.out.println(rs.getString("seat"));
						//Integer.parseInt(rs.getString("seat"))-1;
						((Button)p.getComponent(Integer.parseInt(rs.getString("seat"))-1)).setVisible(false);
					}
				}
				catch(Exception a){}
				System.out.println("success"+((Button)p.getComponent(12)).getActionCommand());
				seatPanel.add(p);
				seatPanel.add(bookthese);
				dummy.add(seatPanel,BorderLayout.SOUTH);
				validate();
				
			}
			catch ( Exception e){
			System.out.print("look out error");	
			}
			
		}
		/*
		if (e.getSource() == rows)
			x = Integer.parseInt(rows.getSelectedItem());
		else if (e.getSource() == cols)
			y = Integer.parseInt(cols.getSelectedItem());
		
		System.out.println("lkjasdflj");

		seatPanel.removeAll();
		dummy.remove(seatPanel);
		//dummy.removeAll();
		seatPanel.setLayout(new GridLayout(x,y));
		for (int i=0;i<x;++i)
			for (int j=0;j<y;++j)
				seatPanel.add(new Button( ((Integer)j).toString()) );
		dummy.add(seatPanel,BorderLayout.CENTER);
		seatPanel.validate();
		dummy.validate();*/
		}
	
	void theatreLoggedIn(){
		dummy.removeAll();
		introduction.setText("Type movie and choose ticket cost");
		//dummy.add(introduction);
		
		Panel p = new Panel(new GridLayout(4,1));
		p.add(introduction);
		Panel q = new Panel(new GridLayout(2,1));
		q.add(new Label("Movie Name",Label.CENTER));
		
		q.add(movieName);
		
		p.add(q);
		Panel r = new Panel(new GridLayout(2,1));
		
		r.add(new Label("Cost",Label.CENTER));
		r.add(cost);
		p.add(r);
		
		Button b= new Button("Update Info");
		b.addActionListener(this);
		p.add(b);
		dummy.add(p,BorderLayout.CENTER);
		validate();
	}
	
	public void actionPerformed(ActionEvent action){
		//String pressedButton = action.getActionCommand();
		if (action.getSource() == homeButton){
			state=0;
			clearFields();
			dummy.removeAll();
			introduction.setText("This software helps you book your favorite movie ticket.");
			dummy.add(introduction,BorderLayout.NORTH);
			loginButton.setVisible(true);
			signupButton.setVisible(true);
			theatreButton.setVisible(true);
			validate();
			}
		else if (action.getSource() == loginButton){
			state = loginState;
			clearFields();
			introduction.setText("Enter valid credentials to login");
			namePanel.setVisible(true);
			dummy.removeAll();
			dummy.add(introduction,BorderLayout.NORTH);
			dummy.add(userInput,BorderLayout.SOUTH);
			namePanel.setVisible(false);
			dummy.validate();
			validate();
			}
		else if (action.getSource() == signupButton){
			clearFields();
			state = registerState;
			introduction.setText("Enter valid credentials to register");
			
			dummy.removeAll();
			dummy.add(introduction,BorderLayout.NORTH);
			namePanel.setVisible(true);
			dummy.add(userInput,BorderLayout.SOUTH);
			
			validate();
			}
		else if (action.getSource() == theatreButton){
			//state = theatreState;
			clearFields();
			dummy.removeAll();
			Panel theatreButtons	= new Panel(new FlowLayout());
			Button theatreLogin		= new Button("Theatre Login");
			Button theatreRegister	= new Button("Theatre Register");
			
			theatreButtons.add(theatreRegister);
			theatreRegister.addActionListener(this);
			theatreLogin.addActionListener(this);
			theatreButtons.add(theatreLogin);
			
			dummy.add(theatreButtons);
			validate();
			//theatreLogIn();
			}
		else if (action.getActionCommand().equals("Theatre Login")){
			//System.out.println("You pressed t login");
			dummy.removeAll();
			clearFields();
			state = theatreLogin;
			introduction.setText("Theatre Login");
			dummy.add(introduction,BorderLayout.NORTH);
			dummy.add(userInput,BorderLayout.CENTER);
			namePanel.setVisible(false);
			/*
			introduction.setText("Type movie and choose ticket cost");
			//dummy.add(introduction);
			
			Panel p = new Panel(new GridLayout(4,1));
			p.add(introduction);
			Panel q = new Panel(new GridLayout(2,1));
			q.add(new Label("Movie Name",Label.CENTER));
			
			q.add(movieName);
			
			p.add(q);
			Panel r = new Panel(new GridLayout(2,1));
			
			r.add(new Label("Cost",Label.CENTER));
			r.add(cost);
			p.add(r);
			
			Button b= new Button("Update Info");
			b.addActionListener(this);
			p.add(b);
			dummy.add(p,BorderLayout.CENTER);*/
			validate();
		}
		else if (action.getSource() == bookthese) {
			//bookthese.setVisible(false);
			String movie = movieChoice.getSelectedItem();
			String theatre = theatreChoice.getSelectedItem();
			String show = showChoice.getSelectedItem();
			String showtable="";
			if (show.equals("Morning Show"))		showtable = "morningshow";
			else if ( show.equals("Matinee Show")) 	showtable = "matineeshow";
			else if ( show.equals("First Show"))	showtable = "firstshow";
			else if ( show.equals("Second Show"))	showtable = "secondshow";
			
			try{
				Enumeration e = seatsobj.vec.elements();
				int temp;
				String reservation=" ";
				
				while (e.hasMoreElements()){
					temp=((Integer)e.nextElement()).intValue();
					reservation+=temp;
					reservation+=",";
					st.executeUpdate("insert into "+showtable+" values('"+theatre+"',"+temp+")");
					//System.out.println(e.nextElement());
				}
				seatsobj.clear();
				dummy.removeAll();
				introduction.setText("You booked "+reservation+" seats ..");
				
				dummy.add(introduction,BorderLayout.NORTH);
				//dummy.add(bill,BorderLayout.CENTER);
			}
			catch(Exception e){System.out.println("unable to ");}
			
		}
		else if (action.getActionCommand().equals("Theatre Register")){
			//System.out.println("You pressed t register");
			clearFields();
			state= theatreRegister;
			dummy.removeAll();
			
			Panel p	= new Panel(new FlowLayout());
			Panel s = new Panel(new GridLayout(2,1));
			s.add(new Label("Location",Label.CENTER));
			s.add(location);
			p.add(s);
			
			Panel q= new Panel(new GridLayout(2,1));
			q.add(new Label("seats",Label.CENTER));
			
			Panel r= new Panel(new GridLayout());
			r.add(cols);
			r.add(rows);
			q.add(r);
			
			p.add(q);
			
			Panel t = new Panel(new GridLayout(0,1));
			dummy.add(t,BorderLayout.CENTER);
			introduction.setText("Register your theatre with us");
			t.add(introduction);
			t.add(p);
			t.add(userInput);
			//dummy.add(p);
			//dummy.add(userInput);
			validate();
			clearFields();
		}
		else if (action.getActionCommand().equals("Update Info")){
			System.out.println("you pressed update ifo");
			String m= movieName.getText();
			String c = cost.getSelectedItem();
			try {
				st.executeUpdate( "update movies set movie='"+m+"' where theatre='"+currentTheatre+"'" );
				st.executeUpdate( "update movies set cost="+c+"    where theatre='"+currentTheatre+"'" );
			}
			catch(Exception e ) {
				System.out.println("unable to set");
			}
			currentTheatre = "";
			dummy.removeAll();
			introduction.setText("Successfully Updated ..");
			dummy.add(introduction,BorderLayout.NORTH);
			validate();
			clearFields();
		}

		else if (action.getSource() == clearButton){
			System.out.println("clear pressed");
			clearFields();
			validate();
			}
		else if (action.getSource() == submitButton){
			// Process the input data to store.
			
			//introduction.setVisible(false);
			//userInput.setVisible(false);
			
			// if he is in register state.
			if (state==registerState){
				String namein	=name.getText();
				String phnoin	=phno.getText();
				String passwdin	=passwd.getText();
				
				if (namein.equals("") || phnoin.equals("") ||passwdin.equals("")){
					//System.out.println("+namein+");
					showStatus("Please fill all the fields");
					validate();
				}
				else{
					//System.out.println(MovieTicketBookingClient.checkPhone(phnoin));
					if (MovieTicketBookingClient.checkPhone(phnoin)){
						System.out.println("in");
						boolean allow=true;
						try{
							rs=st.executeQuery("select phno from users");
							String s;
							while (rs.next()){
								s = rs.getString("phno");
								if (s.equals(phnoin)) {
									allow=false;
									break;
								}
							}
						}
						catch(Exception e){
							
						}
						if (allow==true){
							try{
								st.executeUpdate( "insert into users values('"+phnoin+"','"+namein+"','"+passwdin+"')" );	
								dummy.remove(userInput);
								introduction.setText("Registration Successful");
								showStatus("Registration Successful");
								loginButton.setVisible(false);
								signupButton.setVisible(false);
								theatreButton.setVisible(false);
								clearFields();
								validate();
							}
							catch(Exception e){
								System.out.println("Error while inserting");
								}
							}
						else{
							showStatus("This phno already in use");
						}
					}
					else{
						showStatus("Error in fields");
					}
				}
			}
			else if (state==loginState){
				System.out.println("loginState");
				String phnoin	=phno.getText();
				String passwdin	=passwd.getText();
				if (MovieTicketBookingClient.checkPhone(phnoin)){
					try{
						rs=st.executeQuery("select phno from users");
						String s;
						boolean found=false;
						while (rs.next()){
							s = rs.getString("phno");
							System.out.println(s);
							if (s.equals(phnoin)) {
								found=true;
								System.out.println("phno equal");
								rs=st.executeQuery("select name,passwd from users where phno='"+phnoin+"'");
								rs.next();
								if (passwdin.equals(rs.getString("passwd"))){
									currentUser=rs.getString("name");
									showStatus(currentUser);
									//dummy.removeAll();
									bookTicket();
									break;
								}
								else{
									showStatus("Wrong Credentials");
									break;
								}
							}
						}
						if (found==false)
							showStatus("We don't recognize you.. please register");
					}
					catch(Exception e){
						
					}
				}
				else{
					showStatus("Wrong Credentials");
				}
			}
			else if(state == theatreRegister){
				String namein	=name.getText();
				String phnoin	=phno.getText();
				String passwdin	=passwd.getText();
				String locationin=location.getSelectedItem();
				int rowin		= Integer.parseInt(rows.getSelectedItem());
				int colin		= Integer.parseInt(cols.getSelectedItem());
				
				if (namein.equals("") || phnoin.equals("") ||passwdin.equals("")){
					//System.out.println("+namein+");
					showStatus("Please fill in all the fields");
					validate();
				}
				else{
					if (MovieTicketBookingClient.checkPhone(phnoin)){
						boolean allow=true;
						try{
							rs=st.executeQuery("select phno from theatre");
							String s;
							while (rs.next()){
								s = rs.getString("phno");
								if (s.equals(phnoin)) {
									allow=false;
									break;
								}
							}
						}
						catch(Exception e){}// careful in here
						if (allow==true){
							try{
								st.executeUpdate( "insert into theatre values('"+namein+"','"+phnoin+"','"+passwdin+"','"+locationin+"',"+rowin+","+colin+")" );	
								//insert empty row..
								st.executeUpdate( "insert into movies  values( '"+namein+"','"+" "+"',0)" );
							//	System.out.println("insert into movies  values(" '"+namein+",'" "',"0");
								dummy.removeAll();
								introduction.setText("Registration Successful");
								showStatus("Registration Successful");
								dummy.add(introduction);
								clearFields();
								validate();
							}
							catch(Exception e){
								System.out.println("Error while inserting");
								}
							}
						else{
							showStatus("This phno already in use");
						}
						}
					else{
						showStatus("Wrong Credentials(invalid phno)");
					}
				}		
			}
			else if (state == theatreLogin){
				System.out.println("theatre loginState");
				String phnoin	=phno.getText();
				String passwdin	=passwd.getText();
				if (MovieTicketBookingClient.checkPhone(phnoin)){
					try{
						rs=st.executeQuery("select phno from theatre");
						String s;
						boolean found=false;
						while (rs.next()){
							s = rs.getString("phno");
							System.out.println(s);
							if (s.equals(phnoin)) {
								found=true;
								System.out.println("phno equal");
								rs=st.executeQuery("select name,passwd from theatre where phno='"+phnoin+"'");
								rs.next();
								if (passwdin.equals(rs.getString("passwd"))){
									currentTheatre=rs.getString("name");
									showStatus(currentTheatre);
									theatreLoggedIn();
									break;
								}
								else{
									showStatus("Wrong Credentials");
									break;
								}
							}
						}
						if (found==false)
							showStatus("We don't recognize you.. please register");
					}
					catch(Exception e){
						
					}	
				}
				else{
					showStatus("Wrong Credentials");
				}
			}
			
			/*
			int rows =2,columns = 5;
			seatPanel.setLayout(new GridLayout(rows,columns));
			for (int i=0;i<rows;++i){
				for (int j=0;j<columns;++j){
					seatPanel.add(new Button( ((Integer)j).toString()) );
					}
				}

			dummy.add(seatPanel);
			dummy.validate();*/
			}
		//System.out.println(state);
		repaint();
		}
	void clearFields(){
		name.setText("");
		phno.setText("");
		passwd.setText("");
		movieName.setText("");
		validate();
	}
	static boolean checkPhone(String phno){
		int len = phno.length();
		if (len>10 || len <10)
			return false;
		else{
			for (int var=0;var<len;++var){
				if (('0' <= phno.charAt(var)) &&( phno.charAt(var)<= '9'));
				else return false;
			}
			return true;
		}
	}
	
	void bookTicket(){
		dummy.removeAll();
		movieChoice.removeAll();
		theatreChoice.removeAll();
		introduction.setText("Welcome  "+currentUser);
		dummy.add(introduction,BorderLayout.NORTH);
		
		Panel p = new Panel(new GridLayout(2,1));
		
		Panel q = new Panel(new GridLayout(2,1));
		Panel r = new Panel(new FlowLayout());
		r.add(new Label("Choose Movie",Label.CENTER));
		r.add(new Label("Choose Theatre",Label.CENTER));
		r.add(new Label("Choose Show",Label.CENTER));
		
		Panel s =new Panel(new FlowLayout());
		s.add(movieChoice);
		s.add(theatreChoice);
		s.add(showChoice);
		
		showChoice.setVisible(false);
		q.add(r);
		q.add(s);
		p.add(q);
		
		try{
			rs=st.executeQuery("select movie from movies where movie!=' '");
			String temp;
			while (rs.next()){
				temp = rs.getString("movie");
				movieChoice.add(temp);
				}
			}
		catch(Exception e){}	
		dummy.add(p,BorderLayout.CENTER);
		
		validate();
	}
	void theatreLogIn() {
	
		dummy.removeAll();
		Panel choicePanel = new Panel(new FlowLayout());
		
		choicePanel.add(rows);
		choicePanel.add(cols);
		dummy.add(choicePanel,BorderLayout.NORTH);
		dummy.validate();
		//choicePanel.add

		}
	
	public void focusGained(FocusEvent fe){
		if 	(fe.getSource() == name)
			showStatus("Enter your fullname");
		else if (fe.getSource() == passwd)
			showStatus("Enter your password here");
		else if (fe.getSource() == phno)
			showStatus("Enter your mobile phone no");
		}
	
	public void focusLost(FocusEvent fe){
		showStatus("TicketBooking");
	}
	//public void paint(Graphics g) {
		//showStatus("Hello! Guest");
		//}
	}

class Seats implements ActionListener {
	Vector<Integer> vec=new Vector<Integer>();
	public void actionPerformed(ActionEvent e){
		((Button)e.getSource()).setBackground(Color.blue);
		vec.add(Integer.parseInt(e.getActionCommand()));
	}
	public void clear(){
		vec= new Vector<Integer>();
	}
}
