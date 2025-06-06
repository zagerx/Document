# ADC配置
1. 单次转换模式（Single Conversion Mode）
    - 特点：ADC在接收到触发信号后，仅执行一次转换（单个通道或扫描多个通道），完成后自动停止并等待下次触发。
    - 应用场景：适用于需要低功耗或非连续采样的场景，例如按键触发读取传感器数据。
2. 连续转换模式（Continuous Conversion Mode）
    - 特点：ADC在启动后不间断工作，自动重新触发转换（无需外部信号），可配置为单通道或多通道扫描。
    - 应用场景：适合需要实时监控的场合，如持续采集温度、电压等动态信号。
3. 扫描模式（Scan Mode）
    - 特点：ADC按预设顺序自动转换多个通道（需配置通道序列），**可与单次或连续模式结合使用**。
    - 单次扫描：触发一次后转换所有配置的通道，然后停止。
    - 连续扫描：持续循环转换所有通道。
    - 应用场景：多用于巡回检测多个传感器，如同时采集多个模拟输入信号。
4. 间断模式（Discontinuous Mode）
    - 特点：将多个通道分成若干子组（通过配置子组长度），每次触发仅转换一个子组的通道，需多次触发才能完成全部通道转换。
    - 应用场景：适用于需要灵活控制转换顺序和频率的场景，例如分时复用ADC资源或降低瞬时功耗


## 多通道+规则通道+轮询+无DMA+软件触发
在这种条件下，只能使用如下的配置模式。
- 扫描模式关闭
- 单次转化
- 及时获取DR寄存器

读取代码块如下：
```C
void adc1_read(void)//300ms处理一次
{
  // 启动规则组转换
  LL_ADC_REG_StartConversion(ADC1);
  // 等待转换完成
  while(!LL_ADC_IsActiveFlag_EOC(ADC1));
  // 读取通道14的值（规则组第1个通道）
  uint32_t ch14_value = LL_ADC_REG_ReadConversionData16(ADC1);
  USER_DEBUG_NORMAL("ch14_value :%d  \r\n",ch14_value);
  // 等待转换完成
  while(!LL_ADC_IsActiveFlag_EOC(ADC1));
  // 读取通道18的值（规则组第2个通道）
  uint32_t ch18_value = LL_ADC_REG_ReadConversionData16(ADC1);
  // 清除标志位
  LL_ADC_ClearFlag_EOC(ADC1);
  USER_DEBUG_NORMAL("ch18_value %d \r\n",ch18_value);
}
```
## 多通道+规则通道+轮询模式+DMA+软件处罚
- 扫描模式开启（连续转换多个通道）
- 配置连续模式（只需一次触发）
- 配置软件触发
- 启动数据覆盖
- 使能ADC模块
- 中断中读取数据
