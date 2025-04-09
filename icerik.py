from pylab import *
import matplotlib.pyplot as plt


x = [2, -3, -1.5, 3]
y = [3, 1, -2.5, -2]
color = ['m', 'g', 'r', 'b']
fig = plt.figure()
ax = fig.add_subplot(111)
scatter(x, y, s=100, marker='o', c=color)
a = []
b = []
a.append(x[0])
b.append(y[0])
a.append(x[3])
b.append(y[3])
for i in range(len(x)):

    if len(x) > 2:
        plt.plot(a[i:i + 2], b[i:i + 2], 'ro-')

    plt.plot(x[i:i + 2], y[i:i + 2], 'ro-')

left, right = ax.get_xlim()
low, high = ax.get_ylim()
arrow(left, 0, right - left, 0, length_includes_head=True, head_width=0.15)
arrow(0, low, 0, high - low, length_includes_head=True, head_width=0.15)
xpoints = ypoints = ax.get_xlim()
ax.plot(xpoints, ypoints, linestyle='-', color='k', lw=3, scalex=False, scaley=False)
grid()
show()
