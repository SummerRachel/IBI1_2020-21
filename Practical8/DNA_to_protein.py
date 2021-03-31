#import DNA sequence
seq='ATGCGACTACGATCGAGGGCC'
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
protein=''
#use for loop to do this task
for i in range(0,len(seq),3):
	recent=seq[i:i+3]
#stop coding if we meet X/O/U
	if recent=='X'or recent=='O'or recent=='U':
		break
	else:protein+=gene_code[recent]

print(protein)
