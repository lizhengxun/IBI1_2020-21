#the initial number is 84 
n=84
#input r rate
r=1.1
j=0
#5 round of injection
while j<=4:
	n=n+n*r
	j+=1
print("r rate is: "+str(r)+" the total number of individuals infected after 5 generations is "+str(n))
