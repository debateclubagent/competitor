import random

mock_products = [
    {
        "name": "AI Notetaker",
        "tagline": "自动生成会议纪要的助手",
        "url": "https://www.producthunt.com/posts/ai-notetaker",
        "description": "AI Notetaker 能帮你实时转录会议内容，自动整理要点，生成行动项。支持Zoom、Meet、Teams等平台。",
    },
    {
        "name": "ArtifyAI",
        "tagline": "把照片变成艺术品的AI工具",
        "url": "https://www.producthunt.com/posts/artifyai",
        "description": "ArtifyAI 支持上传照片并选择艺术风格模板，如梵高、莫奈、油画风等，3秒生成风格图像。支持商用。",
    },
]
def fetch_random_ai_product():
    return random.choice(mock_products)
