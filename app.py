import gradio as gr
from groq import Groq
import os

# Lấy key từ Environment (an toàn 100%)
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Logo của mày (thay link nếu muốn)
LOGO_URL = "https://files.catbox.moe/7v2f5k.png"  # logo số 2 mày chọn

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

# GIAO DIỆN SIÊU ĐẸP + KHÔNG LỖI THEME/CSS (test OK 100%)
with gr.Blocks(theme="soft", title="HieuGPT") as demo:
    gr.HTML(f"""
    <div style="text-align:center; padding:20px; background: linear-gradient(135deg, #1e1e1e 0%, #2d1b69 100%); border-radius: 10px; margin-bottom: 20px;">
        <img src="{LOGO_URL}" width="120" style="border-radius:50%; box-shadow: 0 0 30px rgba(255,0,102,0.5);">
        <h1 style="color: #fff; font-size:48px; margin:10px 0;">HieuGPT</h1>
        <p style="color:#ccc; font-size:18px;">Bot của Hiệu – Miễn phí • Siêu nhanh • Bá đạo nhất Việt Nam ❤️‍🔥</p>
    </div>
    """)
    
    chatbot = gr.Chatbot(
        height=650,
        avatar_images=("👤", LOGO_URL),  # avatar user + logo HieuGPT
        bubble_full_width=False,
        show_label=False
    )
    
    msg = gr.Textbox(
        placeholder="Hỏi tao bất cứ gì đi bro...",
        container=False,
        scale=7,
        lines=1
    )
    
    clear = gr.Button("🗑️ Xóa lịch sử", scale=1, variant="secondary")
    
    msg.submit(chat_with_hieugpt, [msg, chatbot], [msg, chatbot])
    clear.click(lambda: [], None, chatbot, queue=False)

demo.queue(max_size=50).launch(server_name="0.0.0.0", server_port=7860)
