#Three lines to make our compiler able to draw:
import sys
import matplotlib
matplotlib.use('Agg')

# ******* Following only demos n log (n)
# ******* Other growth rates also need to coded

import matplotlib.pyplot as plt
import numpy as np


# Define n values
n = np.arange(1, 51)  # from 1 to 50: default step is 1

# Compute n * log(n) using natural log
y = n * np.log(n)

# Plot
plt.figure(figsize=(8,5))

# May need to update following to add info
plt.plot(n, y, marker='o', linestyle='-', color='blue')

# Labels and title
# *****Need to add code here
plt.grid(True)

plt.show()

#Two  lines to make our compiler able to draw:
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()
