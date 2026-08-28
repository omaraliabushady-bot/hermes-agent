import gradio as gr

def respond(message, history):
    return f"Hermes Agent response: {message}"

demo = gr.ChatInterface(respond)

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
