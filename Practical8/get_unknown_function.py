import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import re
os.chdir('/Users/xiaziyu')
#read the origin file and create a new file
file_origin=open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa','r')
file=open('unknown_function.fa','w')
#create a file_read to read
file_read=file_origin.read()
#create a split to cut the file_read
split=re.split('>',file_read)
for i in split:
	if'unknown function' in i:
#get the name of the gene
		a=re.findall(r'gene:(.+?)\s',i)
#get the DNA sequence of the gene
		DNAseq=re.sub(r'.+]','',i)
		b=re.sub(r'\n','',DNAseq)
		for d in a:
#write the gene name
			file.write(d)
			file.write('\t\t\t')
#write the length of gene
			file.write(str(len(b)))
			file.write(DNAseq)

file_origin.close()
file.close()
file=open('unknown_function.fa')
print(file.read())
file.close()
