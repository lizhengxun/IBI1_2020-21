import matplotlib.pyplot as plt
import numpy as np
injections = {'USA':29862124, 'India':11285561, 'Brazil':11205972, 'Russia':436}
values = [29862124, 11285561, 11205972, 4360823, 4234924]
pro = []
sum = 0
for i in range(0,5):
	sum += values[i]
for j in range(0,5):
	a = float(values[j]/sum)
 	pro.append(a)
labels ='USA', 'India', 'Brazil', 'Russia','UK'
colors = 'green', 'yellow', 'blue', 'red', 'pink'
plt.pie(pro, labels=labels, colors=colors, autopct='%1.1f%%')
plt.axis('equal')
plt.show()
