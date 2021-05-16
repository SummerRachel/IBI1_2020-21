#gather the gene information
gene_lengths=[9410,394141,4442,105338,19149,76779,126550,36296,842,15981]
exon_counts=[51,1142,42,216,25,650,32533,57,1,523]
import numpy as np
import matplotlib.pyplot as plt
# use two sets of information into two arrays
a=np.array(gene_lengths)
b=np.array(exon_counts)
#get a new array which represents average exon length
c=a/b
print(sorted(c))
#print the boxplot
plt.boxplot(c,vert=True,whis=1.5,patch_artist=True,meanline=False, showbox=True, showcaps= True, showfliers=True, notch = False)
plt.show()
