def ChangeMe(string,String):
	for ele in range(len(string)):
		if string[ele] in ["!","@","#","$","%","^","&","*","(",")"," ","}","{","[","]"]:
			String=String+"\\"+string[ele]
		else:
			String=String+string[ele]
	return String
		
print ChangeMe(list("jfkfkfkfk"),'')
