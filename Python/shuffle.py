#Shuffle Program for seating arragement .....
#Author :: Saikiran638 .
import random as ran

def Shuffle(List):
	ran.shuffle(List)
	return List

def Fun(String,st,ed):
	return [String+str(x) for x in range(st,ed+1)]

List=[desks for Desks in [Fun('A',0,8),Fun('E',0,9),Fun('F',0,8)] for desks in Desks]

Boys=[ID for Lists in [Fun("N100",632,646),Fun("N100",681,693)] for ID in Lists]


for Sh in range(input("Enter Shuffle times ::: \n")):
	Boys=Shuffle(Boys)

print "\n\nID \t\t\t DESK\n"

for Sh in range(len(Boys)):
	print Boys[Sh],"\t\t",List[Sh]
print "\n\nA program by saikrian N ."
