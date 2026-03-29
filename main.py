from gtts import gTTS
from moviepy.editor import *

def run():
    topic = "Amazing AI Facts"

    script = "AI is changing the world faster than you think!"

    tts = gTTS(script)
    tts.save("voice.mp3")

    clip = ImageClip("https://picsum.photos/720/1280").set_duration(10)
    audio = AudioFileClip("voice.mp3")

    video = clip.set_audio(audio)
    video.write_videofile("output.mp4", fps=24)

if __name__ == "__main__":
    run()
