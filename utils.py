def render_report(data):
    swot = data['SWOT']
    return f"""
### 🪧 产品定位：
{data['定位']}

### 🧩 功能描述：
{data['功能']}

### 💰 商业模式：
{data['商业模式']}

### 🎨 交互设计：
{data['交互设计']}

### 🧠 优化建议：
{data['优化建议']}

### 🧭 SWOT分析：
- Strength：{swot['S']}
- Weakness：{swot['W']}
- Opportunity：{swot['O']}
- Threat：{swot['T']}
"""
