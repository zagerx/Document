## 配置
- ubunt系统，配置文件位于`~/.config/Code/User/`目录下

## Clangd及Clangd-format用法
**_特别注意_**
- clangd和Clangd-format的版本注意保持一致

### Clangd-format基础用法
- 创建 clang-format 配置文件
在项目根目录打开终端：
```
# 生成默认配置 (LLVM 风格)
clang-format -style=llvm -dump-config > .clang-format
```
- 自定义规则
编辑`.clang-format文`件
```
BasedOnStyle: Google  # 基础风格
Language: Cpp         # 语言
IndentWidth: 4        # 缩进4个空格
ColumnLimit: 100      # 最大行宽100
PointerAlignment: Left # 指针靠左: int* ptr;
SortIncludes: true    # 自动排序#include

# 大括号换行风格
BreakBeforeBraces: Custom
BraceWrapping:
  AfterClass: true
  AfterFunction: true
  AfterStruct: true
```
- 配置VSCode(settings.json用户级配置目录)
```
{
  // 核心设置
  "clangd.path": "clangd", // 自动查找路径
  "clangd.format.enable": true,
  "editor.formatOnSave": true,
  
  // 语言特定设置
  "[c]": {
    "editor.defaultFormatter": "llvm-vs-code-extensions.vscode-clangd"
  },
  "[cpp]": {
    "editor.defaultFormatter": "llvm-vs-code-extensions.vscode-clangd"
  },
  
  // 性能优化
  "clangd.arguments": [
    "--background-index",
    "--clang-tidy",
    "--header-insertion=iwyu"
  ],
}
```
### Clangd-format高级用法

