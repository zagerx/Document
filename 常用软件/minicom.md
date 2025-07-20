## 查看串口设备
### JLink虚拟串口
- ls /dev/ttyACM*
### 普通USB串口
- ls /dev/ttyUSB*

## 打开串口
- minicom -D /dev/ttyACM0 -b 115200
  - 波特率默认，-b可以取消

## 常用快捷键
- 