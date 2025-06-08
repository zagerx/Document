import numpy as np
import matplotlib.pyplot as plt

def plot_s_curve(jerk_max=1.0, accel_max=1.0, vel_max=1.0, total_time=7.0):
    """
    绘制七段S型曲线
    参数:
        jerk_max: 最大加加速度
        accel_max: 最大加速度 
        vel_max: 最大速度
        total_time: 总时间
    """
    # 时间分段 (假设每段时间相等)
    t_segment = total_time / 7
    t = np.linspace(0, total_time, 1000)
    
    # 初始化各参数数组
    jerk = np.zeros_like(t)
    accel = np.zeros_like(t)
    vel = np.zeros_like(t)
    pos = np.zeros_like(t)
    
    # 分段计算曲线
    for i, ti in enumerate(t):
        if ti < t_segment:  # 1. 加加速度正
            jerk[i] = jerk_max
            accel[i] = jerk_max * ti
            vel[i] = 0.5 * jerk_max * ti**2
            pos[i] = (1/6) * jerk_max * ti**3
            
        elif ti < 2*t_segment:  # 2. 加加速度0
            jerk[i] = 0
            accel[i] = accel_max
            vel[i] = accel_max*(ti-t_segment) + 0.5*jerk_max*t_segment**2
            pos[i] = 0.5*accel_max*(ti-t_segment)**2 + 0.5*jerk_max*t_segment**2*(ti-t_segment) + (1/6)*jerk_max*t_segment**3
            
        elif ti < 3*t_segment:  # 3. 加加速度负
            jerk[i] = -jerk_max
            accel[i] = accel_max - jerk_max*(ti-2*t_segment)
            vel[i] = vel_max - 0.5*jerk_max*(ti-2*t_segment)**2
            pos[i] = vel_max*(ti-2*t_segment) - (1/6)*jerk_max*(ti-2*t_segment)**3 + pos[2*int(t_segment*1000/total_time)]
            
        elif ti < 4*t_segment:  # 4. 匀速段
            jerk[i] = 0
            accel[i] = 0
            vel[i] = vel_max
            pos[i] = vel_max*(ti-3*t_segment) + pos[3*int(t_segment*1000/total_time)]
            
        elif ti < 5*t_segment:  # 5. 加加速度负
            jerk[i] = -jerk_max
            accel[i] = -jerk_max*(ti-4*t_segment)
            vel[i] = vel_max - 0.5*jerk_max*(ti-4*t_segment)**2
            pos[i] = pos[4*int(t_segment*1000/total_time)] + vel_max*(ti-4*t_segment) - (1/6)*jerk_max*(ti-4*t_segment)**3
            
        elif ti < 6*t_segment:  # 6. 加加速度0
            jerk[i] = 0
            accel[i] = -accel_max
            vel[i] = vel_max - accel_max*(ti-5*t_segment) - 0.5*jerk_max*t_segment**2
            pos[i] = pos[5*int(t_segment*1000/total_time)] + vel_max*(ti-5*t_segment) - 0.5*accel_max*(ti-5*t_segment)**2 - 0.5*jerk_max*t_segment**2*(ti-5*t_segment)
            
        else:  # 7. 加加速度正
            jerk[i] = jerk_max
            accel[i] = -accel_max + jerk_max*(ti-6*t_segment)
            vel[i] = 0.5*jerk_max*(ti-6*t_segment)**2
            pos[i] = pos[6*int(t_segment*1000/total_time)] + (1/6)*jerk_max*(ti-6*t_segment)**3

    # 创建图形
    plt.figure(figsize=(10, 8))
    
    # 加加速度图
    plt.subplot(4, 1, 1)
    plt.plot(t, jerk, 'b')
    plt.ylabel('Jerk')
    plt.title('Seven-segment S-curve Profile')
    plt.grid(True)
    
    # 加速度图
    plt.subplot(4, 1, 2)
    plt.plot(t, accel, 'r')
    plt.ylabel('Acceleration')
    plt.grid(True)
    
    # 速度图
    plt.subplot(4, 1, 3)
    plt.plot(t, vel, 'g')
    plt.ylabel('Velocity')
    plt.grid(True)
    
    # 位移图
    plt.subplot(4, 1, 4)
    plt.plot(t, pos, 'k')
    plt.ylabel('Position')
    plt.xlabel('Time (s)')
    plt.grid(True)
    
    plt.tight_layout()
    plt.show()

def main():
    """主函数入口"""
    try:
        plot_s_curve(jerk_max=2.0, accel_max=1.5, vel_max=3.0, total_time=7.0)
    except Exception as e:
        print(f"运行出错: {e}")

if __name__ == "__main__":
    main()