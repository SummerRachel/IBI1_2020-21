n=84
r=1.2
i=1
n1=n
#n1 stands for the people who are infectors
n2=0
#n2 stands for the people who are infected with diease in this round
m=n
#m stands for the total number of the infected people
for i in range(1,6):
 n2=n1*r
 n1=n1+n2
 m=m+n2
 i=i+1

print"r is",str(r),"the total number is ",str(m)
