# FOC控制器
## 仓库：
- 控制器硬件仓库
  - 控制板仓库(HW_ConctrolBoard)
  - 驱动板仓库(HW_DriverBoard)
  - 编码器仓库(HW_EncodeBoard)
- Kicad元件库/封装库/3D模型库
- 机械模型仓库
  - 3D模型
  - 2D图形库
## 目录
- SBTContorlDevice
  - SBT_Project_Resp_Manage
    - Doc及其他
    - .west
  - HardWare
    - HW_ContorlBoard
      - KicadLibrary(子仓库)
    - HW_DriverBoard
      - KicadLibrary(子仓库)
    - HW_EncoderBoard
      - KicadLibrary(子仓库)
  - Mechine
  - SoftWare
    - app
    - boards
    - moudul
    - bootload
    - zephyr

## 设计目标
- 控制板+驱动板+编码器板
  1. 尺寸尽量紧凑(50*50)mm
  2. 4层板

### 控制板
- 电源

  输入12V转5v，3.3v，预留单独供电接口。
  正常情况由驱动器部分提供12V电源

- 对外接口
  1. can通信接口（4）
    - Rx,Tx(4)
  2. 控制信号对驱动板（16）
     - PWM_CH1,1N
     - CH2,2N
     - CH3 ,3N
     - break
     - CH4(预留)
  3. 反馈信号来自驱动板（8）
     - 母线电压，
     - 母线电流
     - 三相电流
       - ia
       - ib
       - ic
  4. 编码器信号来自编码器板(8)
     - SPI_CS
     - SPI_CK
     - SPI_MISO
     - SPI_MOSI
     - ABZ/HALL
  5. debug接口(4)
     - CLK
     - SWD
     - UART_RX
     - UART_TX

### 驱动板

- 预驱电路
- 三相桥电路
- 运放

### 编码板
- AS5047





