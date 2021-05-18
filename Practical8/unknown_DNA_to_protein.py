import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import re
os.chdir('/Users/xiaziyu')
#import DNA sequence
#read the origin file and create a new file
file_origin=open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa','r')
#input a new file name
name=input('Please input the filename(Remember to include ".fa" in the name):')
file=open(name,'w')
#create a storage for coding
gene_code={'TTT':'F','TTC':'F','TTA':'L','TTG':'L',
 'CTT':'L','CTC':'L','CTA':'L','CTG':'L',
 'ATT':'I','ATC':'I','ATA':'J','ATG':'M',
 'GTT':'V','GTC':'V','GTA':'V','GTG':'V',
    'TCT':'S','TCC':'S','TCA':'S','TCG':'S',
    'CCT':'P','CCC':'P','CCA':'P','CCG':'P',
 'ACT':'T','ACC':'T','ACA':'T','ACG':'T',
 'GCT':'A','GCC':'A','GCA':'A','GCG':'A',
 'TAT':'Y','TAC':'Y','TAA':'Y','TAG':'U',
 'CAT':'H','CAC':'H','CAA':'Q','CAG':'Z',
 'AAT':'N','AAC':'B','AAA':'K','AAG':'K',
 'GAT':'D','GAC':'D','GAA':'E','GAG':'E',
 'TGT':'C','TGC':'C','TGA':'X','TGG':'W',
 'CGT':'R','CGC':'R','CGA':'R','CGG':'R',
 'AGT':'S','AGC':'S','AGA':'A','AGG':'R',
 'GGT':'G','GGC':'G','GGA':'G','GGG':'G'}
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
		protein=''
#use for loop to do this task
		for i in range(0,len(b),3):
        		recent=b[i:i+3]
#stop coding if we meet X/O/U
			if recent=='X'or recent=='O'or recent=='U':
				break
			else:
				protein+=gene_code[recent]

		for d in a:
#write the gene name
			file.write(d)
			file.write('\t')
#write the length of gene
			file.write(str(len(protein)))
			file.write('\t')
			file.write(protein)
			file.write('\t')

file_origin.close()
