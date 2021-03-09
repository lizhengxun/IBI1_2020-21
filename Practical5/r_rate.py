#the initial number is 84 and r rate is 1.2
n=84
r=1.2
j=0
#5 round of injection
while j<=4:
	n=n+n*1.2
	j+=1
print("if r rate is 1.2, and initial number is 84, the total number of individuals infected after 5 generations is",n)
