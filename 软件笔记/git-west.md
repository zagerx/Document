# git
## 新建远程仓库（安装gh）
- `gh auth login`登录
- `gh repo create <仓库名> [选项]`
```PHP
# 创建带描述的公开仓库
gh repo create zgm-002-driver \
  --public \
  -g C \
  -l Apache-2.0 \
  --clone
```


## west.yml
```yml
manifest:
  remotes:
    - name: zagerx
      url-base: https://github.com/zagerx
  
  projects:
    - name: super 
      path: syrius-apps/apps/super
      remote: zagerx
      revision: master

    - name: superlift
      path: syrius-apps/apps/superlift
      remote: zagerx
      revision: master

    - name: CommonLibrary
      path: syrius-apps/apps/CommonLibrary
      remote: zagerx
      revision: master

    - name: motorlib
      path: syrius-apps/apps/CommonLibrary/motorlib
      remote: zagerx
      revision: master

    - name: ProtocolV4
      path: syrius-apps/apps/CommonLibrary/ProtocolV4
      remote: zagerx
      revision: master

    - name: syrius-dts
      path: syrius-dts/
      remote: zagerx
      revision: master
    
    - name: syrius-boards
      path: syrius-boards/ 
      remote: zagerx
      revision: master
```
## 更新子仓库
```
- git submodule init
- git submodule update
```