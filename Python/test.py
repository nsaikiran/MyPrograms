import time,random,user,os,posixpath as use

if '.Score' not in os.listdir(user.home):
	f=open(use.join(user.home,'.Score'),'w')
	f.close()

def Time(sec,char,Tchar):
	H=(sec/60)/60
	M=(sec-(H*60*60))/60
	S=sec-(H*60*60)-(M*60)
	print 'Elapsed time ::',H,'hour',M,'min',S,'sec'
	CPS=(char/sec)
	Acu=(char/Tchar)*100.0
	print 'Characters per second :: %.3f '%(CPS)
	print 'Accuracy  :: %.3f '%(Acu)
	print str(H)+' '+str(M)+' '+str(S)+' '+str(CPS)+' '+str(Acu)+'\n'
	f=open(use.join(user.home,'.Score'),'a')
	f.write(str(H)+' '+str(M)+' '+str(S)+' '+str(CPS)+' '+str(Acu)+'\n')
	f.close()

Time(120,269.0,370.0)
