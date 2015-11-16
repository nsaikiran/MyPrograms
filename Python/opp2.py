import os,user,posixpath as use,dis

class SearchEngine:
	#Sai=0
	def __init__(self,home):
		def Dot(List):
			return [files for files in List if files[0]!='.']

		def Separate(head,List,ext):
			for files in List:
				if use.isdir(use.join(head,files)):
					Folders.append(use.join(head,files))
				else:
					if use.splitext(files)==ext:
						Files.append(use.join(head,files))
			return Folders,Files
		
		self.list=Dot(os.listdir(home))

	def Find_Ext(self,ext):
		print self.list

SearchEngine.Find_Ext(SearchEngine(user.home),"t")
#print SearchEngine.Sai
z=SearchEngine("/home/RGUKT/Desktop/mine")
#print z.Sai

#shlex,dis
