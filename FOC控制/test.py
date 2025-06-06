import matplotlib.pyplot as plt
import numpy as np

# 创建图形和坐标轴
fig, ax = plt.subplots()

# 绘制矢量
vectors = [
    (1, 0, "V1"),
    (0.5, 0.866, "V2"),
    (-0.5, 0.866, "V3"),
    (-1, 0, "V4"),
    (-0.5, -0.866, "V5"),
    (0.5, -0.866, "V6")
]

for x, y, label in vectors:
    ax.quiver(0, 0, x, y, angles='xy', scale_units='xy', scale=1, color='blue')
    ax.text(x, y, label, fontsize=12)

# 绘制最大内切圆
circle = plt.Circle((0, 0), 0.577, fill=False, color='red', label='最大内切圆')
ax.add_patch(circle)

# 设置坐标轴范围和比例
ax.set_xlim(-1.2, 1.2)
ax.set_ylim(-1.2, 1.2)
ax.set_aspect('equal')

# 添加标题
ax.set_title('电压空间矢量六边形')

# 显示图形
plt.grid(True)
plt.show()