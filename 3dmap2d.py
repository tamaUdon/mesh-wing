import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 1. ３次元曲面の定義
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)
x = 10 * np.outer(np.cos(u), np.sin(v))
y = 10 * np.outer(np.sin(u), np.sin(v))
z = 10 * np.outer(np.ones(np.size(u)), np.cos(v))  # これは単なる球を示す

# 2. その表面に模様を描画
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z, color='c', alpha=0.6)

# 模様を追加 (例としてz軸に沿ったストライプ模様を追加)
for i in range(2, 9, 2):
    ax.plot(x[i, :], y[i, :], z[i, :], color='r', lw=2)

plt.show()

# 3. ３次元の模様をユークリッド平面に写像
fig, ax = plt.subplots()
ax.scatter(x, y, color='c', alpha=0.6)

# 模様を追加 (同じストライプ模様)
for i in range(2, 9, 2):
    ax.plot(x[i, :], y[i, :], color='r', lw=2)

plt.show()





