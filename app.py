from src.agents.agent import GeminiAgent
import gradio as gr

def get_gemini_response(iso_image=None, top_image=None):
    if not iso_image and not top_image:
        return gr.Markdown("Please upload atleast one Image of a component")

    images = []
    if iso_image:
        images.append(iso_image)
    if top_image:
        images.append(top_image)

    agent = GeminiAgent(images)
    response_text = agent.generate_image_content()
    
    return response_text


TITLE = """<h1 align="center" id="space-title"> Gemini Image Analysis Tool ⚖️⚡</h1>"""


synera_app = gr.Blocks()
with synera_app:

    gr.HTML(TITLE)

    with gr.Row():
        with gr.Column():
            isometric_image = gr.Image(
                type="pil",  # Ensure PIL image type
                sources=["upload", "clipboard"],  # Allow uploads & clipboard paste
                label="Upload Isometric Image 📐📷"
            )
            
        with gr.Column():
            top_image = gr.Image(
                type="filepath" ,
                sources=["upload", "clipboard"],
                label="Upload Top Image 📸🔼"
            )

    with gr.Row():
        process = gr.Button(value="Analyze Image(s) 🚀🤖")      

    with gr.Row():
        output_text = gr.Textbox(label="Analysis Report 📊📖")

    process.click(
        get_gemini_response,
        [isometric_image, top_image],
        [output_text],
        queue=True
    )


synera_app.launch()