# analyzer.py
import streamlit as st
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

hf_token = st.secrets["HUGGINGFACEHUB_API_TOKEN"]

model_id = "HuggingFaceH4/zephyr-7b-beta"
tokenizer = AutoTokenizer.from_pretrained(model_id, use_auth_token=hf_token)
model = AutoModelForCausalLM.from_pretrained(model_id, torch_dtype=torch.float16, device_map="auto", use_auth_token=hf_token)

def analyze_product(product):
    desc = product['description']
    prompt = f"你是一个AI产品分析专家。以下是一个AI产品的描述，请你总结它的功能模块。

产品描述：{desc}

功能模块总结："

    try:
        inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
        outputs = model.generate(
            **inputs,
            max_new_tokens=150,
            do_sample=True,
            temperature=0.7,
            top_p=0.9
        )
        summary = tokenizer.decode(outputs[0], skip_special_tokens=True).split("功能模块总结：")[-1].strip()
    except Exception as e:
        summary = f"❌ Zephyr模型分析失败：{str(e)}"

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
