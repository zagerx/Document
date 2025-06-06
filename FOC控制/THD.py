import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用黑体显示中文
plt.rcParams['axes.unicode_minus'] = False  # 正确显示负号


# 理想正弦波（50Hz基波）
t = np.linspace(0, 0.02, 1000)
ideal = 10 * np.sin(2*np.pi*50*t)

# 实际波形（含5/7/11次谐波）
actual = ideal + \
         0.8 * np.sin(2*np.pi*250*t) + \
         0.5 * np.sin(2*np.pi*350*t) + \
         0.3 * np.sin(2*np.pi*550*t)

# 计算THD
V1_rms = 10 / np.sqrt(2)  # 基波有效值
V5_rms = 0.8 / np.sqrt(2)
V7_rms = 0.5 / np.sqrt(2)
V11_rms = 0.3 / np.sqrt(2)

THD = np.sqrt(V5_rms**2 + V7_rms**2 + V11_rms**2) / V1_rms * 100

# 绘图
plt.figure(figsize=(10,6))
plt.plot(t, ideal, 'b--', label='理想电流')
plt.plot(t, actual, 'r-', label=f'实际电流 (THD={THD:.1f}%)')
plt.xlabel('时间(s)')
plt.ylabel('电流(A)')
plt.title('电流波形与谐波失真分析')
plt.legend()
plt.grid(True)
plt.tight_layout()  # 自动调整布局
plt.show()
