import gradio as grd
import whisper
from translate import Translator
from dotenv import dotenv_values
from elevenlabs.client import ElevenLabs
from elevenlabs import VoiceSettings

config = dotenv_values(".env")

ELEVEN_LABS_API_KEY = config["ELEVEN_LABS_API_KEY"]

def translator_function(audio_file):
    #transcript the audio to text
    try:
      model = whisper.load_model("base")
      result = model.transcribe(audio_file, language="Spanish", fp16= False)
      audio_transciption = result["text"]

    except Exception as e:
      raise grd.Error(f"An error ocurred when transcripting the audio to text {str(e)}")
    
    #Translate the text
    try:
      en_transcription = Translator(from_lang="es", to_lang="en").translate(audio_transciption)
      fr_transcription = Translator(from_lang="es", to_lang="fr").translate(audio_transciption)
      de_transcription = Translator(from_lang="es", to_lang="de").translate(audio_transciption)
      ja_transcription = Translator(from_lang="es", to_lang="ja").translate(audio_transciption)

    except Exception as e:
      raise grd.Error(f"An error ocurred when translating the text {str(e)}")
    
    en_file_path = transcription_to_audio(en_transcription, "en")
    fr_file_path = transcription_to_audio(fr_transcription, "fr")
    de_file_path = transcription_to_audio(de_transcription, "de")
    ja_file_path = transcription_to_audio(ja_transcription, "ja")

    return en_file_path, fr_file_path, de_file_path, ja_file_path

def transcription_to_audio(text: str, language: str) -> str:
    #Generate translated audio
    try:
      client = ElevenLabs(api_key= ELEVEN_LABS_API_KEY)
      response = client.text_to_speech.convert(
        voice_id= "ErXwobaYiN019PkySvjV", #Chris voice
        optimize_streaming_latency= "0",
        output_format= "mp3_22050_32",
        text= text,
        model_id= "eleven_turbo_v2",
        voice_settings= VoiceSettings(
          stability= 0.0,
          similarity_boost= 1.0,
          style= 0.0,
          use_speaker_boost=True
        ),
      )

      file_path = f"audios/{language}.mp3"

      with open(file_path, "wb") as f:  #wb cose we save it in text and binary format
        for chunk in response:
          if chunk:
            f.write(chunk)
    except Exception as e:
      raise grd.Error(f"An error ocurred when transforming the translation to audio {str(e)}")

    return file_path

app = grd.Interface(
   fn= translator_function,
   inputs=grd.Audio(
       sources=["microphone"],
       type="filepath",
       label= "Spanish"
   ),
   outputs=[
     grd.Audio(label="English"),
     grd.Audio(label="French"),
     grd.Audio(label="German"),
     grd.Audio(label="Japanese")
     ],
   title="Translator",
   description="AI translator from spanish to different languages"
)

app.launch()