#record every number and sum up the total
U=29862124
I=11285561
B=11205972
R=4360823
K=4234924
Sum=U+I+B+R+K
#calculate every frequency
a=U/Sum
b=I/Sum
c=B/Sum
d=R/Sum
e=K/Sum
#get the dictionary
frequency={'USA':a,'India':b,'Brazil':c,'Russia':d,'UK':e}
print(frequency)
#draw the pie chart
import matplotlib.pyplot as plt
labels='USA','India','Brazil','Russia','UK'
sizes=[a,b,c,d,e]
explode=(0.1,0.1,0.1,0.1,0.1)
plt.pie(sizes,explode=explode,labels=labels,autopct='%1.1f%%',shadow=False,startangle=90)
plt.axis('equal')
plt.show()
