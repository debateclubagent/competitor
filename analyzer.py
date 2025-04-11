from transformers import pipeline
import os

hf_token = os.getenv("HUGGINGFACEHUB_API_TOKEN")

summarizer = pipeline(
    "summarization",
    model="sshleifer/distilbart-cnn-12-6",
    use_auth_token=hf_token
)

def analyze_product(product):
    desc = product['description']
    summary = summarizer(desc, max_length=100, min_length=20, do_sample=False)[0]['summary_text']

    return {
        "定位": f"{product['tagline']}",
        "功能": summary,
        "商业模式": "订阅制 / 免费基础功能 + 高级付费",
        "交互设计": "界面现代，交互流程清晰，适合快速上手",
        "优化建议": "可以增加多语言支持 + 更多风格模板",
        "SWOT": {
            "S": "操作简单，易于集成",
            "W": "功能单一，易被模仿",
            "O": "AI内容生成市场快速增长",
            "T": "竞争者众多，技术门槛降低"
        }
    }
