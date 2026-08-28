import gradio as gr

def respond(message, history):
    return f"Hermes Agent response: {message}"

demo = gr.ChatInterface(respond)

# تصدير التطبيق لـ Vercel
app = demo.app
