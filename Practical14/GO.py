#try to use recursion to solve the problem
import re
#load an XML document and create a minidom object using the xml.dom
from xml.dom.minidom import parse
import xml.dom.minidom
import os
import matplotlib.pyplot as plt
import pandas as pd
os.chdir('/Users/xiaziyu')
go_obo=open('go_obo.xml','r')
#use dom because it can form a tree structure
DOMTree=xml.dom.minidom.parse('go_obo.xml')
collection=DOMTree.documentElement
#get the term from each sequence
terms=collection.getElementsByTagName('term')
DNAcounter=0
RNAcounter=0
Proteincounter=0
CHcounter=0
i=0
#create a list longer than 2000000
loc=[0]*5000000
#create a function which can found the childnode and parentnode
def find(j,term):
    is_a = []
    flag = False
    is_a = term.getElementsByTagName('is_a')
    if is_a == []:
        flag = False
    else:
        for a in is_a:
            parentid = a.childNodes[0].data
            s = re.findall(':(\d.*)$',parentid)
            digitid = int(s[0])
            fatherterm = terms[loc[digitid]]
            defstr = fatherterm.getElementsByTagName('defstr')[0]
            d = defstr.childNodes[0].data
            if re.search(j,d):
                flag = True
            elif find(j,fatherterm):
                flag = True
    return flag


for term in terms:
	termid=term.getElementsByTagName('id')[0].childNodes[0].data
	p=re.findall(':(\d.*)$',termid)
	q=int(p[0])
	loc[q]=i
	i=i+1
#use find function to count the number
#get the number of childnodes associated with DNA
for term in terms:
	if find('DNA',term):
		DNAcounter+=1

#get the number of childnodes associated with RNA
for term in terms:
	if find('RNA',term):
		RNAcounter+=1

#get the number of childnodes associated with protein
for term in terms:
	if find('protein',term):
		Proteincounter+=1

#I chose carbohydrate as the fourth macromolecule
#get the number of childnodes associated with CH
for term in terms:
	if find('carbohydrate',term):
		CHcounter+=1

print('The Number of ChildNodes Associated with DNA:',DNAcounter)
print('The Number of ChildNodes Associated with RNA:',RNAcounter)
print('The Number of ChildNodes Associated with Protein:',Proteincounter)
print('The Number of ChildNodes Associated with Carbohydrate:',CHcounter)

#draw a pie chart related to these four numbers
labels='DNA-associated\n'+str(DNAcounter),'RNA-associated\n'+str(RNAcounter),'Protein-associated\n'+str(Proteincounter),'Carbohydrate-associated\n'+str(CHcounter)
plt.pie([DNAcounter,RNAcounter,Proteincounter,CHcounter],explode=True,labels=labels,colors=('r','b','c','g'),autopct='%1.2f%%',pctdistance=0.7,shadow=True, labeldistance=1.3,startangle=0,radius=1.2,counterclock=True,wedgeprops=None,textprops=None,center=(0,0),frame=False)
plt.title('Numbers of ChildNodes of Associated with DNA,RNA,Protein and Carbohydrate in the Gene Ontology')
plt.axis('equal')
plt.show()
