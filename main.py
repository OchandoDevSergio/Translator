import gradio as grd

def translatorFunction():
    pass

app = grd.Interface(
   fn= translatorFunction,
   inputs=grd.Audio(
       sources=["microphone"],
       type="filepath"
   ),
   outputs=[],
   title="Translator",
   description="AI translator to different languages"
)

app.launch()