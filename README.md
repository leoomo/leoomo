# 个人技术名片

简洁优雅的个人技术名片网站，展示开发者简介、技能、项目和联系方式。

## 特性

- 现代 UI 设计，带渐变装饰和微妙动画
- 响应式布局，适配桌面端和移动端
- 平滑滚动动画效果
- 可视化工作经历时间线
- 修改配置即可更新个人信息
- 推送到 GitHub 自动部署

## 快速开始

### 克隆项目

```bash
git clone https://github.com/leoomo/leoomo.git
cd leoomo
```

### 本地开发

```bash
# 修改 build_page.py 中的 PERSONAL_INFO 字典更新个人信息
python build_page.py
```

生成的 `index.html` 可在浏览器中直接打开预览。

## 项目结构

```
leoomo/
├── build_page.py          # Python 生成脚本
├── index.html             # 生成的静态页面
├── .github/
│   └── workflows/
│       └── deploy.yml     # GitHub Actions 部署配置
└── README.md
```

## 配置说明

### 个人信息

修改 `build_page.py` 中的 `PERSONAL_INFO` 字典：

| 字段 | 说明 |
|------|------|
| `name` | 姓名 |
| `title` | 职位 |
| `initials` | 头像缩写 |
| `experience` | 工作年限 |
| `location` | 所在城市 |
| `email` | 邮箱 |
| `bio` | 个人简介 |

### 技能分类

颜色选项：`AI/LLM`、`Backend`、`RPA`、`Frontend`、`Database`、`DevOps`

### 项目配置

```python
{
    "name": "项目名称",
    "description": "项目描述",
    "tech": "技术栈",
    "url": "项目链接",     # 可选
    "featured": True       # 重点展示
}
```

### 工作经历

```python
{
    "company": "公司名称",
    "position": "职位",
    "period": "在职时间",
    "highlights": ["亮点1", "亮点2"],
    "icon": "缩写"         # 2-4 字符
}
```

## 部署

推送到 GitHub 后，GitHub Actions 自动部署到 GitHub Pages：

```bash
git add .
git commit -m "Update"
git push origin master
```

访问 https://leoomo.github.io/leoomo 查看效果。

## 自定义样式

编辑 `build_page.py` 中的 CSS 变量：

```css
:root {
  --primary: #0D9488;
  --primary-dark: #0F766E;
  --gradient-end: #6366F1;
}
```

## 许可证

MIT License
