import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
os.chdir("/Users/xiaziyu")
#import the .csv file works
covid_data=pd.read_csv("full_data.csv")
#show all columns and every second row between(and including)0 and 10
covid_data.iloc[0:11:2,:]
#use a Boolean to show 'total_cases' for all rows 'afghanistan'
L=[]
for i in range (0,7996):
	if covid_data.loc[i,"location"]=="Afghanistan":
		flag=True
		L.append(flag)
	else:
		flag=False
		L.append(flag)
print(covid_data.loc[L,"total_cases"])
#find the world rows
world=[]
for i in range(0,7996):
	if covid_data.loc[i,'location']=='World':
		flag=True
		world.append(flag)
	else:
		flag=False
		world.append(flag)
#get new_cases of world and new_deaths of world
world_date=covid_data.loc[world,'date']
world_data=covid_data.loc[world,'new_cases']
world_death=covid_data.loc[world,'new_deaths']
#calculate the mean and median
np.mean(world_data)
np.median(world_data)
#create a boxplot of new cases worldwide
plt.plot(world_date,world_data,'b+')
plt.plot(world_date,world_death,'r+')
plt.show()
#plot both new cases and new deaths worldwide
China=[]
for i in range (0,7996):
        if covid_data.loc[i,"location"]=="China":
                flag=True
                L.append(flag)
        else:
             	flag=False
                L.append(flag)
China_total=covid_data.loc[China,"total_cases"]
China_new=covid_data.loc[China,"new_cases"]
China_date=covid_data.loc[China,"date"]
plt.plot(China_date,China_total,'b+')
plt.plot(China_date,China_new,'r+')
plt.show()
