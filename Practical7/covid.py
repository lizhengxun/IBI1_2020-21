import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
os.chdir("/Users/lizhengxun/Documents/GitHub/IBI1_2020-21/Practical7")
# import the file
a = covid_data = pd.read_csv("full_data.csv")
#  show all columns, and every second row between (and including) 0 and 10
b = covid_data.iloc[0:11:2,:]
print(b)
# extract the data from column "location"
location = covid_data.iloc[:,1]
# using a Boolean to show “total cases” for all rows corresponding to Afghanistan.
my_rows = []
for i in range(len(location)):
    if location[i] == "Afghanistan":
        c = True
    else:
        c = False
    my_rows.append(c)
d = covid_data.iloc[my_rows,[1,4]]
print(d)
# extract the fata of dates,new deaths and new cases of worldwide
world_new_cases = []
world_new_deaths = []
world_date =[]
rows2 = []
for j in range(len(location)):
    if location[j] == "World":
        c = True
    else:
        c = False
    rows2.append(c)
world_new_cases = covid_data.iloc[rows2,2]
world_new_deaths = covid_data.iloc[rows2,3]
world_date = covid_data.iloc[rows2,0]
# calculate the mean and median of new cases
new_cases_mean = np.mean(world_new_cases)
new_cases_median = np.median(world_new_cases)
print("the mean of new cases is: " + str(new_cases_mean ))
print("the median of new cases is: " + str(new_cases_median ))
# create a boxplot of new cases of worldwide
plt.title('Worldwide new cases')
plt.ylabel('number')
plt.boxplot(world_new_cases,
            vert=True,
            whis=1.5,
            patch_artist=True,
            meanline=False,
            showmeans=True,
            showbox=True,
            showcaps=True,
            showfliers=False,
            notch=False,
            )
plt.show()
# plot both new cases and new deaths
plt.title('Worldwide new cases and deaths')
plt.plot(world_date, world_new_cases, 'ro')
plt.plot(world_date, world_new_deaths, 'b+')
plt.xlabel('date')
plt.ylabel('number')
plt.xticks(world_date.iloc[0:len(world_date):4],rotation=-90)
plt.show()

# the code to answer my question
# extract the new cases in China and UK
china_new_cases = []
uk_new_cases = []
rows3 = []
rows4 = []
for k in range(len(location)):
    if location[k] == "China":
        c = True
    else:
        c = False
    rows3.append(c)
china_new_cases = covid_data.iloc[rows3,2]
for q in range(len(location)):
    if location[q] == "United Kingdom":
        c = True
    else:
        c = False
    rows4.append(c)
uk_new_cases = covid_data.iloc[rows4,2]
# make plot to compare new cases between China and UK
plt.title('New cases and deaths in China and UK')
plt.ylabel('number')
plt.xlabel('date')
plt.plot(world_date, china_new_cases, 'ro')
plt.plot(world_date, uk_new_cases, 'b+')
plt.xticks(world_date.iloc[0:len(world_date):4],rotation=-90)
plt.show()


