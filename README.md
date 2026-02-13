# 个人技术名片网站

一个简洁优雅的个人技术名片网站，展示开发者简介、技能、项目经验和联系方式。采用 Python 脚本生成静态 HTML，通过 GitHub Pages 部署。

## 特性

- **简洁美观的设计** - 采用现代 UI 设计语言，带有渐变装饰和微妙动画
- **响应式布局** - 完美适配桌面端和移动端设备
- **滚动动画** - 使用 Intersection Observer 实现的平滑滚动动画效果
- **时间线展示** - 工作经历采用可视化时间线设计
- **易于定制** - 通过修改配置文件即可更新个人信息
- **自动部署** - 推送到 main 分支自动触发 GitHub Actions 部署

## 技术栈

- **前端**: HTML5, CSS3, JavaScript (原生)
- **后端**: Python 3 (用于生成静态页面)
- **版本控制**: Git & GitHub
- **CI/CD**: GitHub Actions
- **托管**: GitHub Pages

## 快速开始

### 克隆项目

```bash
git clone https://github.com/leoomo/my_dev_card.git
cd my_dev_card
```

### 安装依赖

项目使用 uv 管理 Python 环境：

```bash
uv sync
```

### 本地开发

修改 `build_page.py` 中的 `PERSONAL_INFO` 字典，更新个人信息：

```python
PERSONAL_INFO = {
    "name": "你的名字",
    "title": "你的职位",
    "initials": "名字缩写",
    # ... 其他字段
}
```

生成 HTML 页面：

```bash
python build_page.py
```

生成的 `index.html` 可以在浏览器中直接打开预览。

## 项目结构

```
my_dev_card/
├── build_page.py          # Python 生成脚本
├── index.html             # 生成的静态页面
├── .github/
│   └── workflows/
│       └── deploy.yml     # GitHub Actions 部署配置
├── docs/                  # 设计文档
│   ├── spec.md
│   ├── design.md
│   └── product-design.md
└── README.md
```

## 配置说明

### 个人信息字段

| 字段 | 说明 | 示例 |
|------|------|------|
| `name` | 姓名 | Hua Zeng |
| `title` | 职位标题 | Python Developer |
| `initials` | 头像缩写 | HZ |
| `experience` | 总工作年限 | 19 years |
| `python_experience` | Python 经验年限 | 9 years |
| `location` | 所在城市 | Hangzhou |
| `email` | 邮箱地址 | example@email.com |
| `bio` | 个人简介 | ... |

### 技能分类

在 `skills` 字典中添加技能分类，支持的颜色选项：

- `AI/LLM` - 绿色 (#10B981)
- `Backend` - 蓝色 (#3B82F6)
- `RPA` - 橙色 (#F59E0B)
- `Frontend` - 紫色 (#8B5CF6)
- `Database` - 粉色 (#EC4899)
- `DevOps` - 青色 (#06B6D4)

### 项目配置

每个项目支持以下字段：

```python
{
    "name": "项目名称",
    "description": "项目描述",
    "tech": "技术栈",
    "url": "项目链接",  # 可选，设为 None 则不显示链接
    "featured": True   # 设为 True 显示为重点项目
}
```

### 工作经历

每条经历支持以下字段：

```python
{
    "company": "公司名称",
    "position": "职位",
    "period": "在职时间",
    "highlights": ["亮点1", "亮点2"],
    "icon": "图标文字"  # 2-4 个字符的公司缩写
}
```

## 部署到 GitHub Pages

1. Fork 此仓库或推送代码到你的 GitHub 仓库
2. 进入仓库设置 (Settings) → Pages
3. Source 选择 "Deploy from a branch"
4. Branch 选择 "main"，目录选择 "/ (root)"
5. 保存后等待部署完成

或者推送到 main 分支后，GitHub Actions 会自动部署：

```bash
git add .
git commit -m "Update content"
git push origin main
```

访问 `https://<username>.github.io/<repo-name>/` 查看效果。

## 自定义样式

如需修改配色方案，编辑 `build_page.py` 中的 CSS 变量：

```css
:root {
  --primary: #0D9488;        /* 主色调 - 深青色 */
  --primary-dark: #0F766E;   /* 深色变体 */
  --primary-light: #14B8A6;  /* 浅色变体 */
  --gradient-end: #6366F1;   /* 渐变结束色 - 紫色 */
}
```

## 许可证

MIT License

## 作者

- **Hua Zeng** - [GitHub](https://github.com/leoomo)
- 邮箱: leoomo@gmail.com
