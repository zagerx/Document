#!/bin/bash

# GitHub仓库创建与初始化脚本
# 作者：您的名字
# 日期：$(date +%Y-%m-%d)

# 配置参数
DEFAULT_USER="zagerx"  # 默认GitHub用户名

# 获取用户输入
read -p "请输入仓库名称: " repo_name
read -p "仓库是否私有? [y/N]: " is_private
read -p "本地目录名称 (留空使用仓库名): " local_dir
read -p "GitHub用户名 [$DEFAULT_USER]: " github_user

# 设置默认值
github_user=${github_user:-$DEFAULT_USER}
local_dir=${local_dir:-$repo_name}

# 创建远程仓库
if [[ $is_private =~ ^[Yy]$ ]]; then
    echo "正在创建私有仓库 $repo_name..."
    gh repo create "$repo_name" --private --confirm
else
    echo "正在创建公开仓库 $repo_name..."
    gh repo create "$repo_name" --public --confirm
fi

# 创建并初始化本地仓库
echo "正在初始化本地仓库..."
mkdir -p "$local_dir" && cd "$local_dir" || exit
git init
echo "# $repo_name Project" > README.md
git add .
git commit -m "Initial commit"

# 关联远程仓库
echo "正在关联远程仓库..."
git remote add origin "git@github.com:$github_user/$repo_name.git"
git push -u origin master

echo "✅ 操作完成!"
echo "本地目录: $(pwd)"
echo "远程仓库: https://github.com/$github_user/$repo_name"