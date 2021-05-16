import matplotlib.pyplot as plt
import numpy as np
# make a dictionary to store the data
injections = {'USA':29862124, 'India':11285561, 'Brazil':11205972, 'Russia':436}
# print the dictionary
print(injections)
values = [29862124, 11285561, 11205972, 4360823, 4234924]
# calculate the percentage
pro = []
sum = 0
for i in range(0,5):
	sum += values[i]
for j in range(0,5):
	a = float(values[j]/sum)
	pro.append(a)
# make a pie chart
labels ='USA', 'India', 'Brazil', 'Russia','UK'
colors = 'green', 'yellow', 'blue', 'red', 'pink'
plt.pie(pro, labels=labels, colors=colors, autopct='%1.1f%%',startangle=90)
plt.axis('equal')
plt.title('Coronavirus Infection Rates across Countries')
plt.show()
