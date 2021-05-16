import matplotlib.pyplot as plt
import numpy as np
# create two lists
gene_lengths=[9410, 394141, 4442, 105338, 19149, 76779, 126550, 36296, 842, 159]
exon_counts=[51, 1142, 42, 216, 25, 650, 32533, 57, 1, 523]
# calculate and sort average length
L = []
for i in range(0,10):
    a = gene_lengths[i]/exon_counts[i]
    L.append(a)
length = sorted(L)
print(length)
# make a boxplot
plt.boxplot(length,
	    vert=True,
            whis=1.5,
            patch_artist = True,
	    meanline = False,
            showbox = True,
            showcaps = True,
            showfliers = True,
            notch = False,
              )
plt.show()
