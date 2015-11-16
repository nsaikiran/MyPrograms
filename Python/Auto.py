#Program should be edited .....
import time,webbrowser,user,getpass,os,sys

def Fun(List,ele):
	for x in range(len(List)):
		if ele<=List[x]:
			return List[x]

def Open():
	webbrowser.open_new_tab(user.home+"/Auto.htm")
	webbrowser.open_new_tab(user.home+"/Auto.htm")

def Time():return int(time.ctime().split()[3][0:2])*60+int(time.ctime().split()[3][3:5])

def LogIn():
	Now=Time()
	
	if Now<961:
		List,w=[[510,540],[630,660],[810,840],[930,960]],0
		for w in range(len(List)):
			if Now in range(List[w][0],List[w][1]+1):
				Open()
				print "U logged in for Period ",w+1
				break
		List2=[510,630,810,960]

		time.sleep(Fun(List2,Now)-Now)
		LogIn()

	print Now
print "..::: Auto Log In :::..\n"

if 'Auto.htm' in os.listdir(user.home):
	LogIn()
else:
	string='<html><head><script>function login(){document.form1.action="http://10.1.60.7:8081/Stu_Attendance/";document.form1.submit();}</script></HEAD><BODY onLoad="login()"><form NAME="form1" id=form1 method="POST"><input type=hidden name="username" value='+'"'+raw_input("Enter ur user name ::: ")+'"'+'><input type=hidden name="password" value='+'"'+getpass.getpass()+'"'+'></form><p style="display:none;">Remember</p></body></html>'
	x=open(user.home+"/Auto.htm","w")
	x.write(string)
	x.close()
	LogIn()

print "\nReport a bug . Saikiran638\n"
