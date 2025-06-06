## FOC 过流保护完整实现指南

### 1. 硬件级保护（最高优先级）
- 检测对象：母线电流（DC-Link Current）
- 响应时间：< 100 ns
### 2. 软件瞬时保护
- 检测对象：dq坐标系电流矢量幅值
- 响应时间：1个控制周期 (50-100 μs)
- 伪代码实现：
```C
void FOC_ControlLoop() {
    // 获取dq电流
    I_d = Park_Transform(I_alpha, I_beta, theta);
    I_q = Park_Transform(I_alpha, I_beta, theta);
    
    // 计算电流幅值
    I_mag = sqrt(I_d*I_d + I_q*I_q);
    
    // 瞬时过流保护
    if (I_mag > I_peak_max) {
        PWM_DisableAll();
        SetFaultFlag(OVERCURRENT_FAULT);
        return; // 立即退出控制循环
    }
}
```
### 3. 软件RMS保护
- 检测对象：相电流有效值（RMS）
- 响应时间：10-100 ms
- 伪代码
```C
#define RMS_WINDOW_SIZE 100 // 100个采样点

float I_rms_buffer[RMS_WINDOW_SIZE];
int buffer_index = 0;

void Update_RMS_Protection(float I_mag) {
    // 更新环形缓冲区
    I_rms_buffer[buffer_index] = I_mag * I_mag;
    buffer_index = (buffer_index + 1) % RMS_WINDOW_SIZE;
    
    // 计算RMS
    float sum = 0;
    for(int i=0; i<RMS_WINDOW_SIZE; i++) {
        sum += I_rms_buffer[i];
    }
    float I_rms = sqrt(sum / RMS_WINDOW_SIZE);
    // RMS过流保护
    if (I_rms > I_continuous_max) {
        Reduce_Torque_Reference(); // 降低转矩指令
        if (persistent_flag++ > MAX_PERSISTENT_COUNT) {
            PWM_DisableAll();
        }
    }
}
```

### 保护阈值
| 保护类型       | 检测对象        | 典型阈值         | 响应时间   |
|----------------|----------------|------------------|------------|
| 硬件保护       | 母线电流峰值    | 1.5 × I_rated   | <100 ns    |
| 软件瞬时保护   | dq电流幅值      | 1.2 × I_rated   | 50-100 μs  |
| 软件RMS保护    | 相电流RMS       | 1.0 × I_rated   | 10-100 ms  |

## 