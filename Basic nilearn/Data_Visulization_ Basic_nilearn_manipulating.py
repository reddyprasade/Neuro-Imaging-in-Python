import numpy as np
import matplotlib.pyplot as plt

# Let us use a Nifti file that is shipped with nilearn
from nilearn.datasets import MNI152_FILE_PATH

# Note that the variable MNI152_FILE_PATH is just a path to a Nifti file
print('Path to MNI152 template: %r' % MNI152_FILE_PATH) 


from nilearn import plotting
plotting.plot_img(MNI152_FILE_PATH)
plt.show()
