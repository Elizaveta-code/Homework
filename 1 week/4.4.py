import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
fig = plt.figure(figsize = (20,60))
ax1 = fig.add_subplot(611)
ax2 = fig.add_subplot(612)
ax3 = fig.add_subplot(613)
ax4 = fig.add_subplot(614)
ax5 = fig.add_subplot(615)
ax6 = fig.add_subplot(616)
x1 = list(df['SepalLengthCm'])
x2 = list(df['SepalWidthCm'])
x3 = list(df['PetalLengthCm'])
x4 = list(df['PetalWidthCm'])

ax1.plot(x2, x1, color='red', marker='.', markersize=5, markeredgecolor='red', linestyle = 'None')
ax2.plot(x3, x1, color='green', marker='.', markersize=5, markeredgecolor='green', linestyle = 'None')
ax3.plot(x4, x1, color='blue', marker='.', markersize=5, markeredgecolor='blue', linestyle = 'None')
ax4.plot(x3, x2, color='palevioletred', marker='.', markersize=5, markeredgecolor='palevioletred', linestyle = 'None')
ax5.plot(x4, x2, color='mediumorchid', marker='.', markersize=5, markeredgecolor='mediumorchid', linestyle = 'None')
ax6.plot(x4, x3, color='black', marker='.', markersize=5, markeredgecolor='black', linestyle = 'None')

ax1.set_title('SepalLengthCm от SepalWidthCm')
ax2.set_title('SepalLengthCm от PetalLengthCm')
ax3.set_title('SepalLengthCm от PetalWidthCm')
ax4.set_title('SepalWidthCm от PetalLengthCm')
ax5.set_title('SepalWidthCm от PetalWidthCm')
ax6.set_title('PetalLengthCm от PetalWidthCm')

z6 = np.polyfit(x4, x3, 1)
p6 = np.poly1d(z6)
print(p6)
x = [0, 2.6]
y = np.interp(x, x4, x3)
ax6.scatter(x4, x3, marker='x')
ax6.errorbar(x4, x3, yerr=0.2, xerr = 0.1, color = 'k', linestyle = 'None')
ax6.plot(x, y, color='red')


ax1.grid()
ax2.grid()
ax3.grid()
ax4.grid()
ax5.grid()
ax6.grid()

plt.show()