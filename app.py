import gradio as gr
from models.grammar_model import GrammarCorrector
from models.summarizer import StorySummarizer
from models.tone_changer import ToneChanger
from utils.helpers import clean_text

grammar_tool = GrammarCorrector()
summary_tool = StorySummarizer()
tone_tool = ToneChanger()

def enhance_story(text, action, tone):
    text = clean_text(text)
    if action == "Grammar Correction":
        return grammar_tool.correct(text)
    elif action == "Tone Change":
        return tone_tool.change_tone(text, tone.lower())
    elif action == "Summarize":
        return summary_tool.summarize(text)
    else:
        return "Choose a valid action."

with gr.Blocks(css=".gradio-container {max-width: 900px; margin: auto;}") as demo:
    gr.Markdown("## ✨ Story Enhancer AI")
    gr.Markdown("Enhance your writing with **AI-based grammar correction**, **tone transformation**, and **story summarization.**")

    with gr.Row():
        input_text = gr.Textbox(label="📄 Your Story", lines=10, placeholder="Paste or type your story here...")

    with gr.Row():
        action = gr.Radio(["Grammar Correction", "Tone Change", "Summarize"], label="✏️ Choose an Action")
        tone = gr.Radio(["Formal", "Informal"], label="🎭 Select Tone (for Tone Change)", value="Formal")

    output_text = gr.Textbox(label="🧠 AI Response")

    run_button = gr.Button("🚀 Enhance Story")
    run_button.click(fn=enhance_story, inputs=[input_text, action, tone], outputs=output_text)

    gr.Markdown("Made with 💙 by Anu • Powered by Hugging Face & Gradio")

demo.launch()
