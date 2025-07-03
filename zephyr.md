# zephyr开发流程
## 1.创建本地/远程仓库
```
gh repo create Embedded --public --confirm

mkdir Embedded && cd Embedded
git init
echo "# Embedded Project" > README.md
git add .
git commit -m "Initial commit"

git remote add origin git@github.com:zagerx/Embedded.git
git push -u origin master
```

## 2.创建west.yml文件
在Embedded仓库下创建west.yml文件并**推送**到远程仓库
```
manifest:
  self:
    path: Embedded  # 修正拼写错误

  remotes:
    - name: github
      url-base: https://github.com
    - name: origin 
      url-base: ssh://git@github.com/zagerx  # 改为 SSH 协议

  defaults:
    remote: origin
    revision: master

  projects:
    - name: zephyr
      remote: github
      repo-path: zephyrproject-rtos/zephyr
      revision: v4.1.0
      import:
        name-allowlist:
          - cmsis
          - cmsis-dsp
          - hal_stm32

    - name: syrius-dts
      path: syrius-dts/
      remote: origin  # 改为存在的 remote
      revision: v1.0.0
    
    - name: syrius-boards
      path: syrius-boards/
      remote: origin  # 改为存在的 remote
      revision: v1.0.0
```
## 3.在本地初始化/更新
- `mkdir EmbeddedCodes && cd EmbeddedCodes`
- `west init -m "ssh://git@github.com/zagerx/Embedded.git" && west update`

## 4.目录结构
更新结束之后，目录结构如下
- EmbeddedCodes
    - moudul
        - hal
        - lib
    - apps
    - boards
    - dts
    - zehpyr

目录说明
- apps存放应用代码
- boards存放开发板的基础dts
- dts存放boards对应的bing文件
