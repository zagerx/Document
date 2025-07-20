# MCUBoot
## 参考链接
- [zephyr下使用说明](https://docs.zephyrproject.org/4.1.0/services/device_mgmt/dfu.html)
- [MCUBoot在zephyr下应用官方文档](https://docs.mcuboot.com/readme-zephyr)
## MCUBoot主要功能

- 镜像安全启动及升级
  - 为 MCU 提供 Bootloader 功能，上电后先执行 MCUBoot，再由它校验并跳转至真正应用镜像。
  - 支持 4 种升级策略：Overwrite（直接覆盖）、Swap（镜像回滚）、Direct-XIP（就地执行）以及 RAM-Load（拷贝到 RAM 再执行）
  - 通过 image header + TLV 结构存放版本号、签名、加密信息等元数据，确保镜像完整性与来源可信

- 分区管理
  - 典型将 Flash 划分为 Bootloader 区、Primary Slot（当前运行镜像）、Secondary Slot（待升级镜像）及可选 Scratch 区
  - 升级过程中，Swap 模式会利用 Scratch 区交换两个 Slot 内容，支持回滚；Overwrite 模式则直接把 Secondary Slot 覆盖进 Primary Slot，速度更快但无回滚能力。

- 安全特性
  - 可选 RSA/ECDSA 签名验证 与 AES-CTR/Tinycrypt 加密，通过配置 MCUBOOT_USE_MBED_TLS 或 MCUBOOT_USE_TINYCRYPT 启用
  - 提供命令行工具 imgtool.py 来生成、签名、验证升级镜像


## 在zephyr下对STM32G431CB的配置步骤
- mcuboot的目录
  - 编译bootload固件
    - 进入mcuboot/boot/zephyr目录下，编译
    - prj.conf
      - CONFIG_LOG=y
      - CONFIG_MINIMAL_LIBC=y
      - CONFIG_CBPRINTF_NANO=y
      - CONFIG_FLASH=y
      - 等等
  - CMake文件
    - mcuboot/boot/zephyr目录下面
    - 文件主要功能及涉及到的宏
      - 的的
- BootLoader程序的生成

  明确需求:
  - 不对镜像代码进行校验
  - 不使用交换算法
  - 使用双槽
  - 不开启串口升级
  - 减少一切不必要的开销
