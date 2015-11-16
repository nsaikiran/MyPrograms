import curses,time,random,posixpath as use,user,os

Logo="""
________________________
   |      __          __  \\
   | \ / |__| | |\ | |__
   |  |  |    | | \| |__|
   |          __  __
   |  | |\/| |_  |__|
   |  | |  | |__ |  \\ 2.0

"""
if '.Score' not in os.listdir(user.home):
	f=open(use.join(user.home,'.Score'),'w')
	f.close()

def Menu(Window,maxx,maxy):
	try:
		Window.erase()
		Window.refresh()
		Window.addstr(1,((maxx-1)/2)-9,"MAIN MENU",curses.A_STANDOUT)
		Window.addstr(3,2,"1 : Start Tutotial",curses.A_BOLD)
		Window.addstr(4,2,"2 : Score Card ",curses.A_BOLD)
		Window.addstr(5,2,"3 : Exit ",curses.A_BOLD)
		y,x=7,2
		Str="** At instant press 'ctrl + c ' to getback to main menu !"
		for w in range(len(Str)):
			if w==maxx-3:y,x=y+1,0
			Window.addstr(y,x,Str[w],curses.A_BOLD)
			x+=1
		y,x=y+1,2
		Str="** Try not to change the size of command line !"
		for w in range(len(Str)):
			if w==maxx-3:y,x=y+1,0
			Window.addstr(y,x,Str[w],curses.A_BOLD)
			x+=1
		Window.addstr(maxy-1,(((maxx-1)/2)-12),"(c) N.Sai Kiran",curses.A_STANDOUT)
		char=Window.getch()
		if chr(char)=='1':
			Typing(Window,maxx,maxy)
		elif chr(char)=='2':
			Score(Window)
			curses.endwin()
			quit()
		elif chr(char)=='3':
			curses.endwin()
			quit()
		else:
			Menu(Window,maxx,maxy)
	except KeyboardInterrupt:Menu(Window,maxx,maxy)

def Score(Window):
	Window.erase()
	Window.refresh()
	f=open(use.join(user.home,'.Score'),'r')
	z=f.readlines()
	z.reverse()
	f.close()

	def Print(Window,maxx,maxy,List,index):
		try:
			Window.erase()
			Window.refresh()
			Window.addstr(1,((maxx-1)/2)-6,'SCORE',curses.A_STANDOUT)
			[H,M,S,C,A,W]=List[index].split()
			y,x=2,0
			Str="** p :previous & n: next !"
			for w in range(len(Str)):
				if w==maxx-3:y,x=y+1,0
				Window.addstr(y,x,Str[w],curses.A_BOLD)
				x+=1
			Str='ElapsedTime : '+H+' Hour ,'+M+' Min ,'+S+' Sec .'
			Window.addstr(4,0,'RECENT('+str(index+1)+')',curses.A_UNDERLINE)
			y,x=5,0
			for w in range(len(Str)):
				if w==maxx-1:y,x=y+1,0
				Window.addstr(y,x,Str[w],curses.A_BOLD)
				x+=1
			Str='Characters Per Second : '+C
			x,y=0,y+1
			for w in range(len(Str)):
				if w==maxx-1:y,x=y+1,0
				Window.addstr(y,x,Str[w],curses.A_BOLD)
				x+=1
			Str='Accuracy :'+A+' %'
			x,y=0,y+1
			for w in range(len(Str)):
				if w==maxx-1:y,x=y+1,0
				Window.addstr(y,x,Str[w],curses.A_BOLD)
				x+=1
			Str='Words Per Minute : '+W
			x,y=0,y+1
			for w in range(len(Str)):
				if w==maxx-1:y,x=y+1,0
				Window.addstr(y,x,Str[w],curses.A_BOLD)
				x+=1
			#Window.move(maxy-1,maxx-1)
			Window.addstr(maxy-1,(((maxx-1)/2)-9),"TypingTimer",curses.A_STANDOUT)
			ch=Window.getch()
			if chr(ch)=='n':
				if index<len(List)-1:Print(Window,maxx,maxy,List,index+1)
				else:Print(Window,maxx,maxy,List,index)
			elif chr(ch)=='p':
				if index>0:Print(Window,maxx,maxy,List,index-1)
				else:Print(Window,maxx,maxy,List,index)
			else:
				Print(Window,maxx,maxy,List,index)
		except KeyboardInterrupt:
			Menu(Window,maxx,maxy)
	if not z:
		Window.addstr(2,2,'No History !!',curses.A_UNDERLINE)
		Window.getch()
	else:
		Print(Window,maxx,maxy,z,0)
	#Window.getch()
	Menu(Window,maxx,maxy)

def Check(ele,List):
	c=0
	for e in List:
		if ele==e:c=c+1
	if c==6:return True
	else:return False

def Typing(Window,maxx,maxy):
	Passages=["Preschool education is important because it can give a child the edge in a competitive world and education climate.citation needed While children who do not receive the fundamentals during their preschool years will be taught the alphabet, counting, shapes and colors and designs when they begin their formal education they will be behind the children who already possess that knowledge.","In India, compulsory education spans over twelve years, out of which children receive elementary education for 8 years. Elementary schooling consists of five years of primary schooling and 3 years of upper primary schooling. Various states in the republic of India provide 12 years of compulsory school education based on national curriculum framework designed by the National Council of Educational Research and Training.","Higher education, also called tertiary, third stage, or post secondary education, is the non-compulsory educational level that follows the completion of a school providing a secondary education, such as a high school or secondary school. Tertiary education is normally taken to include undergraduate and postgraduate education, as well as vocational education and training. Colleges and universities are the main institutions that provide tertiary education. Collectively, these are sometimes known as tertiary institutions. Tertiary education generally results in the receipt of certificates, diplomas, or academic degrees.","University education includes teaching, research, and social services activities, and it includes both the undergraduate level ,sometimes referred to as tertiary education and the graduate ,or postgraduate, level sometimes referred to as graduate school. Universities are generally composed of several colleges. In the United States, universities can be private and independent, like Yale University, they can be public and State governed, like the Pennsylvania State System of Higher Education, or they can be independent but State funded, like the University of Virginia.","With the boom of information from availability of knowledge through means of internet and other modern low cost information exchange mechanisms people are beginning to take an attitude of Lifelong learning. To make knowledge and self improvement a lifelong focus as opposed to the more traditional view that knowledge and in particular value creating trade skills are to be learned just exclusively in youth.","The first large established university is thought to be Nalanda established in 427 A.D in India. At its peak, the university attracted scholars and students from as far away as Tibet, China, Greece, and Persia. The first university establishments in the western world are thought to be University of Bologna ,founded in 1088, and later Oxford university ,founded around 1096.","The Renaissance in Europe ushered in a new age of scientific and intellectual inquiry and appreciation of ancient Greek and Roman civilizations. Around 1450, Johannes Gutenberg developed a printing press, which allowed works of literature to spread more quickly. The European Age of Empires saw European ideas of education in philosophy, religion, arts and sciences spread out across the globe. Missionaries and scholars also brought back new ideas from other civilisations as with the Jesuit China missions who played a significant role in the transmission of knowledge, science, and culture between China and the West, translating Western works like Euclids Elements for Chinese scholars and the thoughts of Confucius for Western audiences. The Enlightenment saw the emergence of a more secular educational outlook in the West.","Adult learning, or adult education, is the practice of training and developing skills in adults. It is also sometimes referred to as andragogy ,the art and science of helping adults learn.Adult education has become common in many countries. It takes on many forms, ranging from formal class-based learning to self-directed learning and e-learning. A number of career specific courses such as veterinary assisting, medical billing and coding, real estate license, bookkeeping and many more are now available to students through the Internet.","Sugars are found in the tissues of most plants but are only present in sufficient concentrations for efficient extraction in sugarcane and sugar beet. Sugarcane is a giant grass and has been cultivated in tropical climates in the Far East since ancient times. A great expansion in its production took place in the 18th century with the setting up of sugar plantations in the West Indies and Americas","Similar to the Collaboration of the week, but on a smaller scale, you might want to adopt an article. This would involve doing the research, writing, and picture-taking (if possible) for either a non-existent article or a stub. Of course, everyone else can still edit an adopted article, and you can work on other things too, but the idea is to find a focus for a while, to try and build up the number of quality articles the Project has produced.","A computer is a general purpose device that can be programmed to carry out a finite set of arithmetic or logical operations. Since a sequence of operations can be readily changed, the computer can solve more than one kind of problem.","Conventionally, a computer consists of at least one processing element, typically a central processing unit (CPU) and some form of memory. The processing element carries out arithmetic and logic operations, and a sequencing and control unit that can change the order of operations based on stored information. Peripheral devices allow information to be retrieved from an external source, and the result of operations saved and retrieved.","I saw many servants carrying bags tied to the end of a stick. These bags containedlittle pebbles. With these bags they now and then flapped the mouths and ears of those who stood nearthem.Itwasastrangepractice.I learned later that these people were so preoccupied with intense thinking that they could neither speak nor listen to others without beingroused.","I learned later that thesepeople were so preoccupied with intense thinking that they could neither speak nor listen to others without being roused. The flapper was also employed to prevent a person wrapped up in meditation from falling off a precipice, or bouncing his head against every post.","I was led into the presence of the king. He did not notice us, as he was deep in thought trying to solve a problem. After an hour, and a gentle flap, he spoke some words. I answered as well as I could, in all the languages that I knew. When it was found that I could neither understand nor be understood, I was led to another room and given dinner.","After dinner, a person came, bringing with him pens, ink, paper and a few books, to teach me their language. I learnt that the word in their language for a flying or floating island is Laputa. ","The kings men thought I was badly clad and ordered a tailor to come and take my measurements. He measured my height and waist and then made some complicated calculations. The result of this was a set of illfitting clothes, because the tailor had made a mistake while calculating ","My knowledge of mathematics helped me in picking up their language, which depended much upon science, and on music. If they were to praise the beauty of a woman or an animal, they described it by circles, parallelograms and other geometrical terms.","These people never enjoyed a minutes peace of mind. They feared that the earth, by continuous exposure to the sun, would at last be wholly swallowed up. They were so alarmed by their thoughts that they could not sleep at night. The flying island was circular.","Its movement depended totally on a huge loadstone, which was six yards in length and three yards in thickness. It was placed around a steel axle so exactly that the weakest hand could turn it. By means of this loadstone, the island was made to rise and fall and move from place to place. The king had his own methods of overcoming the revolt of any of the towns in his kingdom. He would keep his island hovering over the town so that the people received no sun or rain, and as a result became afflicted by diseases."]
	Text=Passages[random.choice(range(0,len(Passages)-1))]
	try:
		Window.erase()
		Window.refresh()
		Window.addstr(1,((maxx-1)/2)-10,"Typing Tutorials",curses.A_STANDOUT)
		#time.sleep(2)
		y,x=5,1
		for words in range(len(Text)):
			if y==maxy-2:break
			if x==maxx-1:
				x,y=1,y+1
			Window.addstr(y,x,Text[words],curses.A_BOLD)
			x=x+1
		y,x,t=5,1,0
		Window.addstr(maxy-1,(((maxx-1)/2)-9),"TypingTimer",curses.A_STANDOUT)
		#curses.init_pair(1,curses.BLACK,curses.WHITE)
		Base=time.ctime()
		Time1=int(Base[11:13])*60*60+int(Base[14:16])*60+int(Base[17:19])
		LIST=[]
		for words in range(len(Text)):
			if y==maxy-2:break
			if x==maxx-1:
				x,y=1,y+1
			#Window.addstr(maxy-3,maxx-4,str(Text[words]))
			Window.addstr(2,maxx-7,"Status",curses.A_BOLD)
			Window.addstr(3,maxx-7,str(t)+'/'+str(words),curses.A_BOLD)
			Window.move(y,x)
			char=Window.getch()
			LIST.append(char)
			#Window.addstr(maxy-3,maxx-4,chr(char)+' '+Text[words],curses.A_STANDOUT) imp
			#,curses.color_pair(2))#A_STANDOUT)#A_STANDOUT : bgcolor ,A_UNDERLINE
			#Window.addstr(14,5,"   ",curses.A_STANDOUT)
			if chr(char)==Text[words]:
				t=t+1
			else:
				Window.addstr(y,x,Text[words],curses.A_UNDERLINE)
			x=x+1
		term=0
		for sai in range(len(LIST)):
			if Check(LIST[sai],LIST[sai+1:sai+7]):
				term=1
				break

		if term:Menu(Window,maxx,maxy)
		else:
			#Window.addstr(maxy-1,4,str(words)+' '+str(t))
			#Window.getch()
			Base=time.ctime()
			Time2=int(Base[11:13])*60*60+int(Base[14:16])*60+int(Base[17:19])
			sec=Time2-Time1
			Tchar=float(words)
			Char=float(t)
			H=(sec/60)/60
			M=(sec-(H*60*60))/60
			S=sec-(H*60*60)-(M*60)
			#print 'Elapsed time ::',H,'hour',M,'min',S,'sec'
			CPS=(Tchar/float(sec))
			Acu=(Char/Tchar)*100.0
			WPM=float(len(Text.split()))/((float(H)*60.0)+float(M)+(float(S)/60.0))
			#print 'Characters per second :: %.3f '%(CPS)
			#print 'Accuracy  :: %.3f '%(Acu)
			#print str(H)+' '+str(M)+' '+str(S)+' '+str(CPS)+' '+str(Acu)+'\n'
			f=open(use.join(user.home,'.Score'),'a')
			f.write(str(H)+' '+str(M)+' '+str(S)+' '+str(CPS)+' '+str(Acu)+' '+str(WPM)+'\n')
			f.close()
			Score(Window)
			#f=open("tr.txt",'w')
			#f.write(str(t))
			#f.close()

	except (KeyboardInterrupt,ZeroDivisionError):
		Menu(Window,maxx,maxy)
		Window.getch()
	curses.endwin()

print "\033[1;"+str(random.choice([31,32,33,34,35,36,38,39]))+"m"+Logo+"\033[1;m"
time.sleep(2)
try:
	Window=curses.initscr()
	#curses.start_color()
	(maxy,maxx)=Window.getmaxyx()
	if maxy-1<=20 or maxx-1<=30:
			curses.endwin()
			print 'Try to maximize!'
			quit(1)
	Menu(Window,maxx,maxy)
except ImportError:
	print "\nSome modules unavailable !!!\n"
