a=1
b=1
print (a)
print (b)
#repeat
for i in range(0,11):
#store the second number value
	c=b
#caculate the third number
	b=a+b
#let a equal to the second number
	a=c
	print(b)
