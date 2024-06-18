import matplotlib.pyplot as plt
import numpy as np

y=np.array([35, 25, 25, 15])
mylabel=["Apples", "Bananas", "Cherries", "Dates"]
myexplode=[0.2, 0, 0, 0]

plt.pie(y, labels=mylabel, startangle=90, explode=myexplode)
plt.legend(loc='lower right', bbox_to_anchor=(1.3, 0.7))
plt.show()
