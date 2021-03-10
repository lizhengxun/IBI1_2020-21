a=061702
b=190784
c=100321
d=c-a
e=b-a
print ("d=",d)
print ("e=",e)
if d>e:
	print "d is greater"
else:
	print "e is greater"

X=True
Y=False
Z=(X and not Y) or (Y and not X)
W=(X !=Y)
print (Z)
print (W)
