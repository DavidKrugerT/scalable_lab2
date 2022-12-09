from transformers import pipeline
import gradio as gr
from pytube import YouTube
import os

pipe = pipeline(model="afroanton/whisper-small-sv-SE")  # change to "your-username/the-name-you-picked"

def transcribe(audio):
    text = pipe(audio)["text"]
    return text

def transcribeUrl(url):
    yt = YouTube(str(url))
    audio = yt.streams.filter(only_audio=True).first().download('yt_video')
    text = pipe(audio)["text"]
    return text

url_examples = [
    "https://www.youtube.com/watch?v=UuDQBjPDbbA&ab_channel=Nyhetsmorgon"
]

url_demo = gr.Interface(
    fn=transcribeUrl, 
    examples=url_examples,
    inputs="text", 
    outputs="text",
    title="Whisper Small Swedish",
    description="Swedish speech and audio recognition using a fine-tuned Whipser small model",
)

voice_demo = gr.Interface(
    fn=transcribe, 
    inputs=gr.Audio(source="microphone", type="filepath"), 
    outputs="text",
    title="Whisper Small Swedish",
    description="Swedish speech and audio recognition using a fine-tuned Whipser small model",
)

demo = gr.TabbedInterface([url_demo, voice_demo], ["video-to-text", "voice-to-text"])

if __name__ == "__main__":
    demo.launch()
