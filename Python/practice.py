#Code for even numbers ..
for w in [even for even in range(0,input("Limit :")) if even%2==0]:
	print "%d is a even number ."%w
print "-"*8
for w in [odd for odd in range(0,input("Limit :")) if odd%2!=0 ]:
	print "%d is a odd number ."%w
print "-"*8
#Code for Prime numbers ....

Primes,Index=[ele for ele in range(1,input("Limit :")) for Ele in range(1,ele) if ele%Ele==0 ],0
while Index!=len(Primes):
	if Primes.count(Primes[Index])==1:
		print "%d is a prime number ."%Primes[Index]
		Index=Index+1
	else:
		Index=Index+Primes.count(Primes[Index])
