for w in range(1,20003):
	c=0
	for r in range(1,w+1):
		if w%r==0:
			c=c+1
	if c==2:
		print w,
