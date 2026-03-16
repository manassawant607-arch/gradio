import gradio as gr

def detect_tb(image):
    return "TB Detection Model Running"

app = gr.Interface(
    fn=detect_tb,
    inputs=gr.Image(),
    outputs="text",
    title="TB X-ray Detector AI"
)

app.launch()
