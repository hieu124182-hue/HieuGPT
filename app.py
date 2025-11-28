import gradio as gr
from huggingface_hub import InferenceClient

client = InferenceClient("Qwen/Qwen2.5-7B-Instruct")

def chat(message, history):
    messages = []
    for h in history:
        messages.append({"role": "user", "content": h[0]})
        messages.append({"role": "assistant", "content": h[1]})
    messages.append({"role": "user", "content": message})
    
    resp = client.chat_completion(messages, max_tokens=1024)
    return resp.choices[0].message.content

with gr.Blocks() as demo:
    gr.Markdown("# HieuGPT ")
    chatbot = gr.Chatbot(height=600)
    txt = gr.Textbox(placeholder="Hỏi gì tao cũng trả lời ngon lành...", label="Tin nhắn")
    
    txt.submit(lambda msg, hist: ("", hist + [[msg, chat(msg, hist)]]), [txt, chatbot], [txt, chatbot])

demo.launch(server_name="0.0.0.0", server_port=7860)
