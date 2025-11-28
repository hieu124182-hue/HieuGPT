import gradio as gr
import os
from groq import Groq

# Key Groq (sẽ lấy từ Environment để an toàn)
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def chat_with_hieugpt(message, history):
    messages = [{"role": "system", "content": "Bạn là HieuGPT – AI siêu thông minh, hay cà khịa, mỉa mai của Hiếu."}]
    
    for user, bot in history:
        messages.append({"role": "user", "content": user})
        if bot:
            messages.append({"role": "assistant", "content": bot})
    
    messages.append({"role": "user", "content": message})

    chat_completion = client.chat.completions.create(
        messages=messages,
        model="llama-3.1-70b-instant",   # hoặc "mixtral-8x7b-32768" cũng free
        temperature=0.8,
        max_tokens=4096,
        stream=True
    )

    reply = ""
    for chunk in chat_completion:
        text = chunk.choices[0].delta.content or ""
        reply += text
        yield reply

# === GIAO DIỆN ĐẸP NHƯ GROK ===
css = """
body { background: #000 !important; color: #fff; }
.gradio-container { max-width: 900px !important; margin: auto; padding-top: 2rem; }
"""

with gr.Blocks(css=css, theme="dark", title="HieuGPT") as demo:
    gr.HTML("""
    <div style="text-align:center; margin-bottom:20px;">
        <img src="https://files.catbox.moe/xxxxxx.png" width="120" style="border-radius:50%; box-shadow: 0 0 30px #ff0066;">
        <h1 style="background: linear-gradient(90deg, #ff0066, #9900ff); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-size:48px;">
            HieuGPT
        </h1>
        <p style="color:#ccc;">Bot của Hiệu – Miễn phí, nhanh, siêu đỉnh!</p>
    </div>
    """)
    
    chatbot = gr.Chatbot(height=650, avatar_images=("https://api.dicebear.com/7.x/bottts/svg", "https://files.catbox.moe/xxxxxx.png"))
    msg = gr.Textbox(placeholder="Hỏi tao cái gì đi bro...", container=False)
    msg.submit(chat_with_hieugpt, [msg, chatbot], [msg, chatbot])

demo.queue(max_size=50).launch()
