# MCUBoot
## 参考链接
- [zephyr下使用说明](https://docs.zephyrproject.org/4.1.0/services/device_mgmt/dfu.html)
- [MCUBoot在zephyr下应用官方文档](https://docs.mcuboot.com/readme-zephyr)
## MCUBoot主要功能
### bootload程序的生成
  - 进入mcuboot/boot/zephyr目录下，编译
  - prj.conf bootload的配置文件
    ```
    ########################################################
    #                  基础系统配置                         #
    ########################################################
    # 启用日志系统
    CONFIG_LOG=y
    # 使用精简版C库以节省空间
    CONFIG_MINIMAL_LIBC=y
    # 使用最小化的printf实现
    CONFIG_CBPRINTF_NANO=y
    # 启用闪存支持
    CONFIG_FLASH=y

    ########################################################
    #                  Bootloader 配置                     #
    ########################################################
    # 启用仅升级模式（无交换）
    CONFIG_BOOT_UPGRADE_ONLY=y
    # 禁用移动交换算法
    CONFIG_BOOT_SWAP_USING_MOVE=n
    # 禁用暂存区交换
    CONFIG_BOOT_SWAP_USING_SCRATCH=n
    # 禁用偏移交换
    CONFIG_BOOT_SWAP_USING_OFFSET=n
    # 禁用自动扇区计算
    CONFIG_BOOT_MAX_IMG_SECTORS_AUTO=n
    # 手动设置最大镜像扇区数
    CONFIG_BOOT_MAX_IMG_SECTORS=24

    # 验证和签名配置
    # 禁用ECDSA-P256签名
    CONFIG_BOOT_SIGNATURE_TYPE_ECDSA_P256=n
    # 禁用所有签名验证
    CONFIG_BOOT_SIGNATURE_TYPE_NONE=y
    # 禁用主槽验证
    CONFIG_BOOT_VALIDATE_SLOT0=n
    # 注释掉的密钥路径
    # CONFIG_BOOT_SIGNATURE_KEY_FILE="root-ec-p256.pem"

    # 加密配置
    # 禁用镜像加密
    CONFIG_BOOT_ENCRYPT_IMAGE=n
    # 禁用加密TLV保存
    CONFIG_BOOT_SWAP_SAVE_ENCTLV=n
    # 禁用引导加载程序自举
    CONFIG_BOOT_BOOTSTRAP=n

    ########################################################
    #                 外设和模块配置                        #
    ########################################################
    # 禁用电源管理
    CONFIG_PM=n
    # 禁用蓝牙
    CONFIG_BT=n
    # 禁用I2C总线
    CONFIG_I2C=n

    ########################################################
    #                 内存优化配置                          #
    ########################################################
    # 主栈大小设为2KB
    CONFIG_MAIN_STACK_SIZE=2048
    # 禁用堆内存分配
    CONFIG_HEAP_MEM_POOL_SIZE=0
    # 启用编译尺寸优化
    CONFIG_SIZE_OPTIMIZATIONS=y

    ########################################################
    #                 日志和调试配置                        #
    ########################################################
    # MCUboot调试日志级别
    CONFIG_MCUBOOT_LOG_LEVEL_DBG=y
    # 系统默认日志级别(错误级)
    CONFIG_LOG_DEFAULT_LEVEL=1
    # 禁用启动横幅
    CONFIG_BOOT_BANNER=n

    ########################################################
    #                 加密库配置                            #
    ########################################################
    # 禁用TinyCrypt加密库
    CONFIG_TINYCRYPT=n
    # 禁用ECC DSA支持
    CONFIG_TINYCRYPT_ECC_DSA=n
    # 禁用SHA256支持
    CONFIG_TINYCRYPT_SHA256=n
    # 禁用mbedTLS加密库
    CONFIG_MBEDTLS=n
    ```
  - dts文件
    ```
    &flash0 {

      partitions {
        compatible = "fixed-partitions";
        #address-cells = <1>;
        #size-cells = <1>;

        boot_partition: partition@0 {
          label = "mcuboot";
          reg = <0x00000000 DT_SIZE_K(42)>;
        };
        slot0_partition: partition@A800 {
          label = "image-0";
          reg = <0x0000A800 DT_SIZE_K(44)>;
        };
        slot1_partition: partition@15800 {
          label = "image-1";
          reg = <0x00015800 DT_SIZE_K(42)>;
        };
      };
    };

    ```
  - CMake文件(提供有哪些源文件会被编译)
    - mcuboot/boot/zephyr目录下面
  
- BootLoader程序的生成

  - `west build -b zgm_001 ./ -- -DBOARD_ROOT=$HOME/worknote/EmbeddedCode/EulerProject/syrius-boards`

### APP程序的生成
- APP程序的生成
  - prj.conf
    ```
    CONFIG_GPIO=y
    CONFIG_LOG=y
    # 禁用 UART 控制台输出
    CONFIG_UART_CONSOLE=y

    # 启用 RTT 控制台
    CONFIG_RTT_CONSOLE=n

    # 启用 SEGGER RTT 通信协议
    CONFIG_TRACING=n
    CONFIG_SEGGER_SYSTEMVIEW=n
    CONFIG_USE_SEGGER_RTT=n

    CONFIG_FPU=y
    CONFIG_FPU_SHARING=y

    CONFIG_BOOTLOADER_MCUBOOT=y    
    ```
  - 对生产的.bin文件进行加签
    - 安装工具`pip install imgtool`
    - 生成密钥
      - `imgtool keygen -k mykey.pem -t rsa-2048`
    - 开始加签
      ```
        imgtool sign \
        --key mykey.pem \
        --header-size 512 \
        --align 8 \
        --version 1.0.0 \
        --slot-size $slot_size \
        --load-addr 0xA800 \
        zephyr.bin \
        signed.bin
    ```
### 程序验证
- 对生成的bootload及app程序进行正确性确认
  使用JFlash工具，分别将两个文件下载到MCU，运行观察

## 使用串口升级
- bootload进入升级模式

  - 修改bootload的prj.conf文件
    ```
    CONFIG_MCUBOOT_SERIAL=y
    CONFIG_BOOT_SERIAL_UART=y
    CONFIG_UART_CONSOLE=n
    CONFIG_MCUBOOT_SERIAL_DIRECT_IMAGE_UPLOAD=y
    CONFIG_USE_SEGGER_RTT=y
    CONFIG_RTT_CONSOLE=y
    ```
  - 此时会默认使用button启动，配置相关按键即可
    ```
    gpio_keys {
      compatible = "gpio-keys";
      button0: mcuboot_button0 {
        label = "User";
        gpios = <&gpioc 10 GPIO_ACTIVE_HIGH>;
        status = "okay";
      };
    };

    aliases {
      led0 = &green_led;
      watchdog0 = &iwdg;
      can0 = &fdcan1;
      mcuboot-button0 = &button0;
    };
    ```
- 按下按键并复位，此时进入“串行恢复模式”
- 使用mcumgr工具，对新的APP程序进行下载
  - 上传固件

    `mcumgr --conntype serial --connstring "dev=/dev/ttyACM0,baud=115200" image upload signed.bin`

  - 重启设备

    `mcumgr --conntype serial --connstring "dev=/dev/ttyACM0,baud=115200" reset`
- 观察现象


### mcumgr工具
#### 安装 Go 环境
`sudo apt install golang-go`
`echo 'export GOPATH=$HOME/go' >> ~/.bashrc`
`echo 'export PATH=$PATH:$GOPATH/bin' >> ~/.bashrc`
`source ~/.bashrc`

#### 安装 mcumgr
`go env -w GOPROXY=https://goproxy.cn,direct  # 国内用户使用`
`go install github.com/apache/mynewt-mcumgr-cli/mcumgr@latest`

#### 验证安装
`mcumgr version`
