"""
Usually in python we can have class variables and instance variables. We can access class variables from instances aswell
but to modify the values we need to use class name to modify class variables otherwise a new instance variable is created 
for that particular object.
We can dynamically add attributes to an object.
"""
class Student:
	"""
	This is a class of student objects
	"""
	count = 0 # Class variable
	def __init__(self,name,roll):
		self.name = name
		self.roll = roll
		Student.count= Student.count + 1
	def classMethod(obj,count):
		obj.count = count

sai = Student("sai",1)
kiran = Student("kiran",2)
print Student.count
print sai.count
print Student.__dict__
print sai.__dict__
sai.count = 9
print sai.__dict__

print Student.count
Student.count = 10
print Student.count
Student.classMethod(sai,638)
print Student.count
#sai.classMethod(9)
