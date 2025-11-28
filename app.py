import gradio as gr
from groq import Groq
import os

# Lấy key từ Environment (an toàn 100%)
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Logo + tên mày (thay link logo nếu muốn)
LOGO = "https://files.catbox.moe/t7h8i9.png"  # logo đỏ-tím xoáy của mày nè

def chat_with_hieugpt(message, history):
    messages = [{"role": "system", "content": "Bạn là HieuGPT – AI siêu thông minh, hài hước và cực kỳ bá đạo của Hiệu. Trả lời thật tự nhiên, dí dỏm, dùng tiếng Việt thân thiện như bạn chí cốt."}]
    
    for user, bot in history:
        messages.append({"role": "user", "content": user})
        if bot:
            messages.append({"role": "assistant", "content": bot})
    
    messages.append({"role": "user", "content": message})

    stream = client.chat.completions.create(
        model="llama-3.1-70b-instant",
        messages=messages,
        temperature=0.8,
        max_tokens=4096,
        stream=True
    )

    reply = ""
    for chunk in stream:
        text = chunk.choices[0].delta.content or ""
        reply += text
        yield reply

# GIAO DIỆN SIÊU ĐẸP + TƯƠNG THÍCH RENDER 100%
with gr.Blocks(theme="dark", title="HieuGPT") as demo:
    gr.HTML(f"""
    <div style="text-align:center; padding:20px;">
        <img src="{LOGO}" width="120" style="border-radius:50%; box-shadow: 0 0 30px #ff0066;">
        <h1 style="background: linear-gradient(90deg, #ff0066, #9900ff); -webkit-background-clip: text; -webkit-text-fill-color: transparent; margin:10px 0;">
            HieuGPT
        </h1>
        <p style="color:#aaa;">Bot của Hiệu – Miễn phí • Siêu nhanh • Bá đạo nhất Việt Nam ❤️‍🔥</p>
    </div>
    """)
    
    chatbot = gr.Chatbot(height=650, avatar_images=(None, LOGO))
    msg = gr.Textbox(placeholder="Hỏi tao bất cứ gì đi bro...", container=False, scale=7)
    
    msg.submit(chat_with_hieugpt, [msg, chatbot], [msg, chatbot])

demo.queue(max_size=50).launch()
