import whisper
import subprocess
from pathlib import Path

_model = whisper.load_model("base") 

def transcribe_video(path: str) -> str:
    audio_path = extract_audio(path)
    result = _model.transcribe(audio_path)
    return result["text"]

def extract_audio(video_path: str) -> str:
    video = Path(video_path)
    audio_path = video.with_suffix(".mp3")

    subprocess.run([
        "ffmpeg",
        "-i", str(video),
        "-vn",
        "-acodec", "mp3",
        str(audio_path)
    ], check=True)

    return str(audio_path)