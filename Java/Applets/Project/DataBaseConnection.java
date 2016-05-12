import java.sql.*;

public class DataBaseConnection {
	public Connection con;
	public Statement st;
	public ResultSet rs;

	public DataBaseConnection(){
		try {
			Class.forName("com.mysql.jdbc.Driver");
			con = DriverManager.getConnection("jdbc:mysql://localhost:3306/MovieTicket","root","saikiran");
			st = con.createStatement();
			System.out.println("success");
			}
		catch(Exception e){
			System.out.println("error");
			}
		}
	public static void main(String args[]){ new DataBaseConnection();}
	}
